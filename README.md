# Discord Bot

This is a simple Discord bot built with Python using the `discord.py` library. The bot can perform a variety of tasks such as welcoming new members, responding to messages, managing roles, sending direct messages, and even creating polls.

## Features

* **Welcome New Members**: Sends a welcome message to new members when they join the server.
* **Message Responses**: Responds to certain words (e.g., "hello") in messages and deletes inappropriate ones (e.g., "shit").
* **Role Management**: Allows users to assign or remove a specific role.
* **Direct Messaging**: The bot can DM users when requested.
* **Command Prefix**: All bot commands use `!` as the command prefix.
* **Polls**: Users can create polls with custom questions.
* **Secret Role Access**: Only users with a specific role (`member`) can access certain commands.

## Requirements

Before you start, ensure you have the following installed:

* Python 3.8 or higher
* [discord.py](https://discordpy.readthedocs.io/en/stable/) library
* [python-dotenv](https://pypi.org/project/python-dotenv/) for loading environment variables
* A `.env` file containing your Discord bot token

You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/sankalpkumar111/discord-bot
   cd discord-bot
   ```

2. Create a `.env` file in the root of the project and add your bot token:

   ```env
   DISCORD_TOKEN=your-bot-token-here
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the bot:

   ```bash
   python bot.py
   ```

## Commands

* `!hello`: Sends a greeting to the user.
* `!assign`: Assigns the `member` role to the user.
* `!remove`: Removes the `member` role from the user.
* `!dm <message>`: Sends a DM to the user with the specified message.
* `!reply`: Replies with a default message.
* `!secret`: Sends a message only if the user has the `member` role.
* `!poll <question>`: Creates a poll with the provided question.

## Error Handling

* The bot checks for missing roles on the `!secret` command and sends a friendly message if the user doesn't have the required role.

## Logging

The bot uses a file handler to log events and errors to `discord.log`. This log file is set to be ignored by Git by default.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

