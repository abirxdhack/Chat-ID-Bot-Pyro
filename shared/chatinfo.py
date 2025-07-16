#Copyright @ISmartCoder 
#Updates Channel t.me/TheSmartDev
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils import LOGGER
from bot import bot

@bot.on_message(filters.private)
async def handle_message(bot: Client, message):
    LOGGER.info("Handling shared chat/user message")
    if getattr(message, "chats_shared", None):
        if hasattr(message.chats_shared, "chats") and message.chats_shared.chats:
            for chat in message.chats_shared.chats:
                chat_id = chat.chat_id
                chat_name = chat.name or "Unnamed Chat"
                chat_type = str(chat.chat_type).replace("ChatType.", "").capitalize()
                username = f"@{chat.username}" if chat.username else "No username"
                text = (
                    "**Shared Chat Info**\n"
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
                if hasattr(chat, "photo") and chat.photo:
                    await message.reply_photo(photo=chat.photo.file_id, caption=text, reply_markup=reply_markup)
                else:
                    await message.reply_text(text, reply_markup=reply_markup)
        elif hasattr(message.chats_shared, "users") and message.chats_shared.users:
            for user in message.chats_shared.users:
                user_id = user.user_id
                first_name = user.first_name
                last_name = user.last_name or ""
                username = f"@{user.username}" if user.username else "No username"
                user_type = "Bot" if user.username and user.username.lower().endswith("bot") else "User"
                text = (
                    f"**Shared {user_type} Info**\n"
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
                if hasattr(user, "photo") and user.photo:
                    await message.reply_photo(photo=user.photo.file_id, caption=text, reply_markup=reply_markup)
                else:
                    await message.reply_text(text, reply_markup=reply_markup)
