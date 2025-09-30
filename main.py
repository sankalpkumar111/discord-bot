import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import logging

load_dotenv()

token = os.getenv("DISCORD_TOKEN")
hnadler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
hnadler.setLevel(logging.INFO)
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot=commands.Bot(command_prefix="!", intents=intents)

secret_role="member"
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user.name}')
    
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='general')
    if channel:
        await channel.send(f'Welcome to the server, {member.name}!')
    # logging.info(f'Member joined: {member.name}#{member.discriminator} (ID: {member.id})')
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if 'hello' in message.content.lower():
        await message.channel.send(f'Hello, {message.author.name}!')
    elif 'shit' in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} you are not allowed to say that!")
        
    await bot.process_commands(message)
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')
    
@bot.command()
async def assgin(ctx):
    role=discord.utils.get(ctx.guild.roles, name=secret_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f'{ctx.author.mention} You have been assigned the {secret_role} role.')
    else:
        await ctx.send(f'The {secret_role} role does not exist.')

@bot.command()
async def remove(ctx):
    role=discord.utils.get(ctx.guild.roles, name=secret_role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f'{ctx.author.mention} You have been removed from the {secret_role} role.')
    else:
        await ctx.send(f'The {secret_role} role does not exist.')


@bot.command()
async def dm(ctx, *, msg):
    await ctx.author.send(f"You said {msg}")
    
@bot.command()
async def reply(ctx):
    await ctx.reply("This is a reply to your message.")
        
@bot.command()
@commands.has_role(secret_role)
async def secret(ctx):
    await ctx.send(f'Welcome to th secret club, {ctx.author.mention}!')

@bot.command()
async def poll(ctx,*,question):
    embed=discord.Embed(title="New Poll", description=question, color=discord.Color.blue())
    # poll_message=await ctx.send(embed=embed)
    message=await ctx.send(embed=embed)
    await message.add_reaction('✅')
    await message.add_reaction('❌')

@secret.error
async def secret_error(ctx, error):
    if isinstance(error, commands.MissingRole):
         await ctx.send(f'Sorry {ctx.author.mention}, you do not have the required role to access this command.')


bot.run(token,log_handler=hnadler,log_level=logging.DEBUG)


