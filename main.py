import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import logging
import random
import asyncio

# ✅ Load environment variables
load_dotenv()
token = os.getenv("DISCORD_TOKEN")

# ✅ Logging setup
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setLevel(logging.INFO)

# ✅ Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# ✅ Bot setup
bot = commands.Bot(command_prefix="!", intents=intents)
secret_role = "member"

# 🚀 Events
@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user.name}')

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='general')
    if channel:
        await channel.send(f'🎉 Welcome to the server, {member.name}!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower()
    
    if 'hello' in content:
        await message.channel.send(f'👋 Hello, {message.author.name}!')
    elif 'shit' in content:
        await message.delete()
        await message.channel.send(f"🚫 {message.author.mention}, watch your language!")
    elif 'bye' in content or 'by' in content:
        await message.channel.send(f'👋 Goodbye, {message.author.name}!')
    elif 'help' in content:
        help_text = """
📜 **Available Commands**
> 🧩 Basic
`!assign` — Get the 'member' role  
`!remove` — Remove your 'member' role  
`!ping` — Check if bot is online  
`!help` — Show this message  

> 🧑‍💻 Communication
`!dm <message>` — DM yourself  
`!reply` — Bot replies to you  
`!announce <text>` — Post announcements  
`!poll <question>` — Create Yes/No poll  

> ⚙️ Moderation
`!clear <n>` — Delete last n messages  
`!mute <@user> <minutes>` — Temporarily mute a member  
`!unmute <@user>` — Unmute member  
`!warns <@user>` — Check user warnings (placeholder)  

> 🎮 Fun & Games
`!roll` 🎲 | `!flip` 🪙 | `!joke` 😂 | `!fact` 💡 | `!compliment [@user]` 🌟  

> 🔒 Secret
`!secret` — Members-only command  

> ℹ️ Info
`!userinfo [@user]` — View user info  
`!serverinfo` — View server info  

> ⏰ Utility
`!reminder <minutes> <task>` — Set reminders
"""
        await message.channel.send(help_text)
    
    await bot.process_commands(message)

# 🧩 Role Management
@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=secret_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f'✅ {ctx.author.mention}, you have been given the **{secret_role}** role.')
    else:
        await ctx.send(f'⚠️ Role `{secret_role}` does not exist.')

@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name=secret_role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f'🗑️ {ctx.author.mention}, your **{secret_role}** role was removed.')
    else:
        await ctx.send(f'⚠️ Role `{secret_role}` does not exist.')

# 💬 Communication
@bot.command()
async def dm(ctx, *, msg):
    await ctx.author.send(f"📩 You said: {msg}")

@bot.command()
async def reply(ctx):
    await ctx.reply("🤖 Here's my reply!")

@bot.command()
async def announce(ctx, *, announcement):
    embed = discord.Embed(title="📢 Announcement", description=announcement, color=discord.Color.green())
    await ctx.send(embed=embed)

@bot.command()
async def poll(ctx, *, question):
    embed = discord.Embed(title="📊 Poll", description=question, color=discord.Color.blue())
    message = await ctx.send(embed=embed)
    await message.add_reaction('✅')
    await message.add_reaction('❌')

# ⚙️ Moderation
@bot.command()
async def ping(ctx):
    await ctx.send('🏓 Pong!')

@bot.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'🧹 Cleared {amount} messages.', delete_after=3)

@bot.command()
async def warns(ctx, member: discord.Member):
    await ctx.send(f'⚠️ {member.name} has **0 warnings** (placeholder).')

@bot.command()
async def mute(ctx, member: discord.Member, duration: int):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    if role:
        await member.add_roles(role)
        await ctx.send(f'🔇 {member.mention} muted for {duration} minutes.')
        await asyncio.sleep(duration * 60)
        await member.remove_roles(role)
        await ctx.send(f'🔈 {member.mention} has been unmuted.')
    else:
        await ctx.send('⚠️ Muted role not found.')

@bot.command()
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    if role:
        await member.remove_roles(role)
        await ctx.send(f'🔈 {member.mention} has been unmuted.')
    else:
        await ctx.send('⚠️ Muted role not found.')

# 🎮 Fun Commands
@bot.command()
async def roll(ctx):
    number = random.randint(1, 6)
    await ctx.send(f'🎲 You rolled a **{number}**, {ctx.author.mention}!')

@bot.command()
async def flip(ctx):
    result = random.choice(["Heads", "Tails"])
    await ctx.send(f'🪙 {ctx.author.mention}, it’s **{result}**!')

@bot.command()
async def joke(ctx):
    jokes = [
        "Why don’t skeletons fight? They don’t have the guts!",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the math book look sad? Too many problems."
    ]
    await ctx.send(f'😂 {random.choice(jokes)}')

@bot.command()
async def fact(ctx):
    facts = [
        "Bananas are berries, strawberries aren’t!",
        "A day on Venus is longer than its year.",
        "Your brain produces 20 watts of power."
    ]
    await ctx.send(f'💡 {random.choice(facts)}')

@bot.command()
async def compliment(ctx, member: discord.Member = None):
    compliments = [
        "You're awesome! 🌟",
        "You light up the server! 💫",
        "You're as cool as a bug-free bot 😎"
    ]
    target = member.mention if member else ctx.author.mention
    await ctx.send(f'{target}, {random.choice(compliments)}')

# 🔒 Secret Command
@bot.command()
@commands.has_role(secret_role)
async def secret(ctx):
    await ctx.send(f'🔐 Welcome to the secret club, {ctx.author.mention}!')

@secret.error
async def secret_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send(f'❌ {ctx.author.mention}, you need the `{secret_role}` role!')

# 📊 Info Commands
@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send(f'👤 {member.name}#{member.discriminator} (ID: {member.id})')

@bot.command()
async def serverinfo(ctx):
    guild = ctx.guild
    await ctx.send(f'🏠 Server: {guild.name}\n👥 Members: {guild.member_count}\n🆔 ID: {guild.id}')

# ⏰ Reminder
@bot.command()
async def reminder(ctx, time: int, *, task):
    await ctx.send(f'⏰ Reminder set for {time} minutes: {task}')
    await asyncio.sleep(time * 60)
    await ctx.send(f'🔔 {ctx.author.mention}, reminder: {task}')

# 🚀 Run Bot
bot.run(token, log_handler=handler, log_level=logging.DEBUG)
