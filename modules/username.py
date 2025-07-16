#Copyright @ISmartCoder 
#Updates Channel t.me/TheSmartDev
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatType
from utils import LOGGER
from bot import bot
import os

@bot.on_message(filters.private & filters.regex(r"^@[A-Za-z0-9_]{5,}$"))
async def username_command(bot: Client, message):
    LOGGER.info(f"Username message received from user {message.from_user.id}")
    loading_message = await message.reply_text("`Processing Username To Info..`")
    username = message.text.strip()
    try:
        chat = await bot.get_chat(username)
        chat_id = chat.id
        chat_type = (
            "User" if chat.type == ChatType.PRIVATE else
            "Bot" if chat.type == ChatType.BOT else
            "Group" if chat.type in [ChatType.GROUP, ChatType.SUPERGROUP] else
            "Channel"
        )
        name = (
            f"{chat.first_name} {chat.last_name or ''}".strip() if chat_type in ["User", "Bot"]
            else chat.title or "Unnamed Chat"
        )
        username = f"@{chat.username}" if chat.username else "No username"
        text = (
            f"**{chat_type} Info** 🌟\n\n"
            f"Type: `{chat_type}`\n"
            f"ID: `{chat_id}`\n"
            f"Name: `{name}`\n"
            f"Username: `{username}`\n\n"
            "> 🛠 Crafted with ❤️ By @TheSmartDev"
        )
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=name,
                        copy_text=str(chat_id)
                    )
                ]
            ]
        )
        if chat.photo:
            try:
                photo_file = await bot.download_media(chat.photo.big_file_id)
                await message.reply_photo(photo=photo_file, caption=text, reply_markup=reply_markup)
                LOGGER.info(f"Sent {chat_type.lower()} photo for chat {chat_id}")
                try:
                    await loading_message.delete()
                except Exception as e:
                    LOGGER.error(f"Failed to delete loading message for user {message.from_user.id}: {e}")
                if os.path.exists(photo_file):
                    os.remove(photo_file)
                    LOGGER.info(f"Cleaned up temporary photo file: {photo_file}")
            except Exception as e:
                LOGGER.error(f"Failed to send {chat_type.lower()} photo for chat {chat_id}: {e}")
                try:
                    await loading_message.delete()
                except Exception as e:
                    LOGGER.error(f"Failed to delete loading message for user {message.from_user.id}: {e}")
                await message.reply_text(text, reply_markup=reply_markup)
        else:
            LOGGER.info(f"No photo object available for chat {chat_id}")
            try:
                await loading_message.delete()
            except Exception as e:
                LOGGER.error(f"Failed to delete loading message for user {message.from_user.id}: {e}")
            await message.reply_text(text, reply_markup=reply_markup)
    except Exception as e:
        LOGGER.error(f"Error fetching chat {username} for user {message.from_user.id}: {e}")
        try:
            await loading_message.delete()
        except Exception as e:
            LOGGER.error(f"Failed to delete loading message for user {message.from_user.id}: {e}")
        await message.reply_text("**Error!** Couldn’t find that chat. Check the username or privacy settings! 😕")
