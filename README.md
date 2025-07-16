# Chat ID Bot Pyro

![Chat ID Echo Bot](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram)  
A simple and efficient Telegram bot that helps you fetch chat IDs for users, groups, channels, and bots instantly.

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
- **pyrofork Library**: The bot uses pyrofork to interact with Telegram’s API.

## 🛠 Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/abirxdhack/Chat-ID-Bot-Pyro.git
   cd Chat-ID-Bot-Pyro
   ```

2. **Install Dependencies**:
   Install the required Python packages using `pip`:
   ```bash
   pip install pyrofork
   ```

3. **Set Up Your Credentials**:
   Open `config.py` and replace the placeholder credentials with your own:
   ```python
   API_ID = 28239710  # Replace with your API ID
   API_HASH = '7fc5b35692454973318b86481ab5eca3'  # Replace with your API Hash
   BOT_TOKEN = '7671261830:AAEW7B_Wd406rBvbEwUiW4uPlHJumUokXaY'  # Replace with your Bot Token
   ```

## 🚀 Usage

1. **Run the Bot**:
   Start the bot by running the script:
   ```bash
   python3 main.py
   ```
   You should see:
   ```
   Bot Successfully Started
   ```

2. **Interact with the Bot**:
   - Open Telegram and start a chat with your bot (find it using the username you set via BotFather).
   - Send the `/start` command to see the welcome message and keyboard.
   - Click a button (e.g., "👤 User", "🔒 Private Group", or "🌐 Public Channel") and share the requested entity.


## 📜 Code Structure

- **`quickinfo.py`**: The main script containing the bot logic, including the event handlers for `/start` and peer sharing.
- **Logging**: The bot uses Python’s `logging` module to log events, making it easy to debug issues.

## 🤝 Contributing

Contributions are welcome! If you have ideas for new features or improvements, feel free to:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📧 Contact

For questions, suggestions, or support, reach out to [abirxdhack](https://github.com/abirxdhack) via GitHub Issues or Telegram (@TheSmartDev).
