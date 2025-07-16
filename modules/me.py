from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils import LOGGER
from bot import bot
import os

@bot.on_message(filters.command("me"))
async def me_command(bot: Client, message):
    LOGGER.info(f"Me command received for user {message.from_user.id}")
    user = message.from_user
    user_id = user.id
    first_name = user.first_name
    last_name = user.last_name or ""
    username = f"@{user.username}" if user.username else "No username"
    
    text = (
        "**Your Info**\n"
        f"Type: `User`\n"
        f"ID: `{user_id}`\n"
        f"Name: `{first_name} {last_name}`\n"
        f"Username: `{username}`"
    )
    
    reply_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=f"{first_name} {last_name}".strip(),
                    copy_text=str(user_id)
                )
            ]
        ]
    )
    
    if user.photo:
        loading_msg = await message.reply_text("`Processing Your Info`")
        try:
            photo_file = await bot.download_media(user.photo.big_file_id)
            await message.reply_photo(photo=photo_file, caption=text, reply_markup=reply_markup)
            LOGGER.info(f"Sent user photo with file_id for user {user_id}")
            await loading_msg.delete()
            if os.path.exists(photo_file):
                os.remove(photo_file)
        except Exception as e:
            LOGGER.error(f"Failed to send user photo with file_id for user {user_id}: {e}")
            await loading_msg.delete()
            await message.reply_text(text, reply_markup=reply_markup)
    else:
        LOGGER.info(f"No photo object available for user {user_id}")
        await message.reply_text(text, reply_markup=reply_markup)