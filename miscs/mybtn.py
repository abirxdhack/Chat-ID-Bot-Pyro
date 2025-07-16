#Copyright @ISmartCoder 
#Updates Channel t.me/TheSmartDev
from pyrogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    RequestPeerTypeChannel,
    RequestPeerTypeChat
)
from utils import LOGGER

my_buttons = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(
                "📢 Your Channel",
                request_chat=RequestPeerTypeChannel(
                    button_id=9,
                    is_creator=True,
                    max=1,
                    is_name_requested=True,
                    is_username_requested=True,
                    is_photo_requested=True
                )
            ),
            KeyboardButton(
                "👥 Your Group",
                request_chat=RequestPeerTypeChat(
                    button_id=8,
                    is_creator=True,
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

LOGGER.info("My buttons initialized")
