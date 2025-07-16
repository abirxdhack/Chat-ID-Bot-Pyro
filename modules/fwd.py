from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils import LOGGER
from bot import bot
import os

@bot.on_message(filters.private & filters.forwarded)
async def handle_forwarded_message(bot: Client, message):
    LOGGER.info("Handling forwarded message")
    try:
        if hasattr(message, "forward_origin") and message.forward_origin:
            origin = message.forward_origin
            if hasattr(origin, "sender_user") and origin.sender_user:
                user = origin.sender_user
                user_id = user.id
                first_name = user.first_name
                last_name = user.last_name or ""
                username = f"@{user.username}" if user.username else "No username"
                user_type = "Bot" if user.username and user.username.lower().endswith("bot") else "User"
                text = (
                    f"**Forwarded {user_type} Info**\n"
                    f"Type: `{user_type}`\n"
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
                if hasattr(user, "photo") and user.photo and hasattr(user.photo, "big_file_id"):
                    loading_msg = await message.reply_text("`Getting User Profile Info`")
                    try:
                        photo_file = await bot.download_media(user.photo.big_file_id)
                        await message.reply_photo(photo=photo_file, caption=text, reply_markup=reply_markup)
                        await loading_msg.delete()
                        if os.path.exists(photo_file):
                            os.remove(photo_file)
                    except Exception as e:
                        LOGGER.error(f"Failed to send photo with big_file_id: {e}")
                        await loading_msg.delete()
                        await message.reply_text(text, reply_markup=reply_markup)
                else:
                    await message.reply_text(text, reply_markup=reply_markup)
            elif hasattr(origin, "chat") and origin.chat:
                chat = origin.chat
                chat_id = chat.id
                chat_name = chat.title or "Unnamed Chat"
                chat_type = str(chat.type).replace("ChatType.", "").capitalize()
                username = f"@{chat.username}" if chat.username else "No username"
                text = (
                    "**Forwarded Chat Info**\n"
                    f"Type: `{chat_type}`\n"
                    f"ID: `{chat_id}`\n"
                    f"Name: `{chat_name}`\n"
                    f"Username: `{username}`"
                )
                reply_markup = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text=chat_name,
                                copy_text=str(chat_id)
                            )
                        ]
                    ]
                )
                if hasattr(chat, "photo") and chat.photo and hasattr(chat.photo, "big_file_id"):
                    loading_msg = await message.reply_text("`Getting User Profile Info`")
                    try:
                        photo_file = await bot.download_media(chat.photo.big_file_id)
                        await message.reply_photo(photo=photo_file, caption=text, reply_markup=reply_markup)
                        await loading_msg.delete()
                        if os.path.exists(photo_file):
                            os.remove(photo_file)
                    except Exception as e:
                        LOGGER.error(f"Failed to send photo with big_file_id: {e}")
                        await loading_msg.delete()
                        await message.reply_text(text, reply_markup=reply_markup)
                else:
                    await message.reply_text(text, reply_markup=reply_markup)
            elif hasattr(origin, "sender_user_name") and origin.sender_user_name:
                text = (
                    f"**Forwarded User Info**\n"
                    f"Name: `{origin.sender_user_name}`"
                )
                reply_markup = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text=origin.sender_user_name,
                                copy_text=origin.sender_user_name
                            )
                        ]
                    ]
                )
                await message.reply_text(text, reply_markup=reply_markup)
            else:
                text = (
                    "**Forwarded User Info**\n"
                    "Name: `Unknown`"
                )
                reply_markup = InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="Unknown",
                                copy_text="Unknown"
                            )
                        ]
                    ]
                )
                await message.reply_text(text, reply_markup=reply_markup)
        else:
            text = (
                "**Forwarded User Info**\n"
                "Name: `Unknown`"
            )
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Unknown",
                            copy_text="Unknown"
                        )
                    ]
                ]
            )
            await message.reply_text(text, reply_markup=reply_markup)
    except Exception as e:
        LOGGER.error(f"Error handling forwarded message: {e}")
        text = (
            "**Forwarded User Info**\n"
            "Name: `Unknown`"
        )
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Unknown",
                        copy_text="Unknown"
                    )
                ]
            ]
        )
        await message.reply_text(text, reply_markup=reply_markup)