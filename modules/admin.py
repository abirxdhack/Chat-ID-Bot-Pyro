#Copyright @ISmartCoder 
#Updates Channel t.me/TheSmartDev
from pyrogram import Client, filters
from utils import LOGGER
from miscs.adbtn import admin_buttons
from bot import bot
from config import COMMAND_PREFIX

@bot.on_message(filters.command("admin", prefixes=COMMAND_PREFIX.split("|")))
async def admin_command(bot: Client, message):
    LOGGER.info("Admin command received")
    await message.reply_text(
        "**🛡️ Channels and Groups Where You Are Admin**\n\n"
        "🔧 **How to Use?**\n"
        "1️⃣ Click the buttons below to share a channel or group where you have admin privileges.\n"
        "2️⃣ Receive the unique ID instantly.\n\n"
        "> 🛠 Made with ❤️ By @TheSmartDev",
        reply_markup=admin_buttons
    )