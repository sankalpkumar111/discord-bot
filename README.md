# Discord Bot

A multi-purpose Discord bot built with Python using the `discord.py` library. This bot can handle **moderation, role management, fun commands, polls, reminders, and more**.

---

## Features

### 🎉 Member Interaction

* **Welcome New Members**: Sends a welcome message to new users when they join the server.
* **Message Responses**: Responds to keywords like `hello` or `bye` and automatically deletes inappropriate messages (e.g., `shit`).
* **Direct Messaging**: DM yourself with `!dm <message>`.

### 🧑‍💻 Role Management

* `!assign` — Assign yourself the `member` role.
* `!remove` — Remove the `member` role.
* `!secret` — Access members-only commands.

### ⚙️ Moderation

* `!clear <n>` — Delete the last `n` messages.
* `!mute <@user> <minutes>` — Temporarily mute a member.
* `!unmute <@user>` — Unmute a member.
* `!warns <@user>` — Show warnings (placeholder for future implementation).

### 🎮 Fun & Games

* `!roll` 🎲 — Roll a dice (1–6).
* `!flip` 🪙 — Flip a coin.
* `!joke` 😂 — Get a random joke.
* `!fact` 💡 — Get a random fact.
* `!compliment [@user]` 🌟 — Send a compliment to yourself or another user.

### 📊 Info & Utility

* `!userinfo [@user]` — Show user information.
* `!serverinfo` — Display server details.
* `!poll <question>` — Create a Yes/No poll.
* `!announce <text>` — Send announcements.
* `!reminder <minutes> <task>` — Set a reminder.

### ✅ Miscellaneous

* `!ping` — Check if the bot is online.
* Friendly error handling for missing roles.

---

## Requirements

* Python 3.8 or higher
* [discord.py](https://discordpy.readthedocs.io/en/stable/)
* [python-dotenv](https://pypi.org/project/python-dotenv/)

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Setup

1. Clone the repository:

```bash
git clone https://github.com/sankalpkumar111/discord-bot
cd discord-bot
```

2. Create a `.env` file in the root directory:

```env
DISCORD_TOKEN=your-bot-token-here
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the bot:

```bash
python bot.py
```

---

## Commands Overview

| Category      | Command                      | Description                       |
| ------------- | ---------------------------- | --------------------------------- |
| 🎉 Member     | `!hello`                     | Sends a greeting.                 |
| 🧑‍💻 Role    | `!assign`                    | Get the `member` role.            |
| 🧑‍💻 Role    | `!remove`                    | Remove the `member` role.         |
| 🧑‍💻 Role    | `!secret`                    | Members-only command.             |
| ⚙️ Moderation | `!clear <n>`                 | Delete last `n` messages.         |
| ⚙️ Moderation | `!mute <@user> <minutes>`    | Temporarily mute a user.          |
| ⚙️ Moderation | `!unmute <@user>`            | Unmute a user.                    |
| ⚙️ Moderation | `!warns <@user>`             | Show warning count (placeholder). |
| 🎮 Fun        | `!roll`                      | Roll a dice.                      |
| 🎮 Fun        | `!flip`                      | Flip a coin.                      |
| 🎮 Fun        | `!joke`                      | Random joke.                      |
| 🎮 Fun        | `!fact`                      | Random fact.                      |
| 🎮 Fun        | `!compliment [@user]`        | Send a compliment.                |
| 📊 Info       | `!userinfo [@user]`          | Show user info.                   |
| 📊 Info       | `!serverinfo`                | Show server info.                 |
| 📊 Utility    | `!poll <question>`           | Create a poll.                    |
| 📊 Utility    | `!announce <text>`           | Send announcement.                |
| ⏰ Utility     | `!reminder <minutes> <task>` | Set a personal reminder.          |

---

## Logging

* Events and errors are logged to `discord.log`.
* Add `discord.log` to `.gitignore` to avoid uploading logs.

---

