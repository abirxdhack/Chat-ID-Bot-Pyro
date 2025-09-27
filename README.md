# Chat ID Bot Pyro

![Chat ID Echo Bot](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram)  
An Advanced and efficient Telegram bot that helps you fetch chat IDs for users, groups, channels, and bots instantly.

## 📖 Overview

The **Chat ID Bot Pyro** is a Telegram bot built with Python and the Pyrofork library. It allows users to quickly retrieve the unique IDs of Telegram entities (users, groups, channels, and bots) by sharing them through a user-friendly keyboard interface. Whether you're a developer needing chat IDs for Telegram API interactions or a user managing groups and channels, this bot makes the process seamless.

This project is maintained by [abirxdhack](https://github.com/abirxdhack) 

## ✨ Features

- **Fetch Chat IDs Instantly**: Retrieve IDs for users, bots, private/public groups, and private/public channels.
- **User-Friendly Interface**: Interactive keyboard with buttons to share different types of Telegram entities.
- **Reliable and Fast**: Built with Telethon for efficient Telegram API interactions.
- **Logging Support**: Includes detailed logging for debugging and monitoring.
- **Open Source**: Feel free to contribute or customize the bot for your needs!

## 📋 Prerequisites

Before setting up the bot, ensure you have the following:

- **Python 3.9+**: The bot is written in Python.
- **Telegram API Credentials**: You’ll need an `API_ID` and `API_HASH` from [my.telegram.org](https://my.telegram.org).
- **Bot Token**: Create a bot via [BotFather](https://t.me/BotFather) on Telegram to get a `BOT_TOKEN`.
- **Pyrofork Library**: The bot uses Pyrofork to interact with Telegram’s API.

## 🛠 Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/abirxdhack/Chat-ID-Pyro-Bot.git
   cd Chat-ID-Pyro-Bot
   ```

2. **Install Dependencies**:
   Install the required Python packages using `pip`:
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Set Up Your Credentials**:
   Open `config.py` and replace the placeholder credentials with your own:
   ```python
   #Copyright @ISmartCoder 
   #Updates Channel t.me/TheSmartDev
   API_ID = "28xx10"  
   API_HASH = "7fc5b2xxb5eca3"  
   BOT_TOKEN = "800xxxxwowmU"  
   COMMAND_PREFIX = "#|.|/|!,"
   ADMIN_ID = 7666341631
   ```

## 🚀 Usage

1. **Run the Bot**:
   Start the bot by running the script:
   ```bash
   python3 main.py
   ```
   You should see:
   ```
   Bot Started Successfully 💥
   ```

2. **Interact with the Bot**:
   - Open Telegram and start a chat with your bot (find it using the username you set via BotFather).
   - Send the `/start` command to see the welcome message and keyboard.
   - Send the `/help` command to see the all commands and explain and help

## 🤝 Contributing

Contributions are welcome! If you have ideas for new features or improvements, feel free to:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## 📧 Contact

For questions, suggestions, or support, reach out to [abirxdhack](https://github.com/abirxdhack) via GitHub Issues.

