from pyrogram import Client, filters
from utils import LOGGER
from miscs.mybtn import my_buttons
from bot import bot
from config import COMMAND_PREFIX

@bot.on_message(filters.command("my", prefixes=COMMAND_PREFIX.split("|")))
async def my_command(bot: Client, message):
    LOGGER.info("My command received")
    await message.reply_text(
        "**📚 Your Channels and Groups**\n\n"
        "🔧 **How to Use?**\n"
        "1️⃣ Click the buttons below to share your channel or group.\n"
        "2️⃣ Receive the unique ID instantly.\n\n"
        "> 🛠 Made with ❤️ By @TheSmartDev",
        reply_markup=my_buttons
    )