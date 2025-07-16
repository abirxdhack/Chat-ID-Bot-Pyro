from pyrogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    RequestPeerTypeUser,
    RequestPeerTypeChannel,
    RequestPeerTypeChat
)
from utils import LOGGER

menu_buttons = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(
                "👤 User Info",
                request_user=RequestPeerTypeUser(
                    button_id=1,
                    is_bot=False,
                    max=1,
                    is_name_requested=True,
                    is_username_requested=True,
                    is_photo_requested=True
                )
            )
        ],
        [
            KeyboardButton(
                "👥 Public Group",
                request_chat=RequestPeerTypeChat(
                    button_id=7,
                    is_username=True,
                    max=1,
                    is_name_requested=True,
                    is_username_requested=True,
                    is_photo_requested=True
                )
            ),
            KeyboardButton(
                "🔒 Private Group",
                request_chat=RequestPeerTypeChat(
                    button_id=6,
                    is_username=False,
                    max=1,
                    is_name_requested=True,
                    is_username_requested=True,
                    is_photo_requested=True
                )
            )
        ],
        [
            KeyboardButton(
                "📢 Public Channel",
                request_chat=RequestPeerTypeChannel(
                    button_id=5,
                    is_username=True,
                    max=1,
                    is_name_requested=True,
                    is_username_requested=True,
                    is_photo_requested=True
                )
            ),
            KeyboardButton(
                "🔒 Private Channel",
                request_chat=RequestPeerTypeChannel(
                    button_id=4,
                    is_username=False,
                    max=1,
                    is_name_requested=True,
                    is_username_requested=True,
                    is_photo_requested=True
                )
            )
        ],
        [
            KeyboardButton(
                "🤖 Bot",
                request_user=RequestPeerTypeUser(
                    button_id=2,
                    is_bot=True,
                    max=1,
                    is_name_requested=True,
                    is_username_requested=True,
                    is_photo_requested=True
                )
            ),
            KeyboardButton(
                "🌟 Premium Users",
                request_user=RequestPeerTypeUser(
                    button_id=3,
                    is_bot=False,
                    is_premium=True,
                    max=1,
                    is_name_requested=True,
                    is_username_requested=True,
                    is_photo_requested=True
                )
            )
        ]
    ],
    resize_keyboard=True,
    placeholder="Choose a chat type"
)

LOGGER.info("Menu buttons initialized")