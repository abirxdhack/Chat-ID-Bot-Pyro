from pyrogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    RequestPeerTypeChannel,
    RequestPeerTypeChat,
    ChatPrivileges
)
from utils import LOGGER

admin_buttons = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(
                "📢 Channels",
                request_chat=RequestPeerTypeChannel(
                    button_id=10,
                    user_privileges=ChatPrivileges(
                        can_manage_chat=True,
                        can_delete_messages=True,
                        can_manage_video_chats=True,
                        can_restrict_members=True,
                        can_promote_members=True,
                        can_change_info=True,
                        can_post_messages=True,
                        can_edit_messages=True,
                        can_invite_users=True,
                        can_pin_messages=True,
                        can_manage_topics=True,
                        can_post_stories=True,
                        can_edit_stories=True,
                        can_delete_stories=True
                    ),
                    max=1,
                    is_name_requested=True,
                    is_username_requested=True,
                    is_photo_requested=True
                )
            ),
            KeyboardButton(
                "👥 Groups",
                request_chat=RequestPeerTypeChat(
                    button_id=11,
                    user_privileges=ChatPrivileges(
                        can_manage_chat=True,
                        can_delete_messages=True,
                        can_manage_video_chats=True,
                        can_restrict_members=True,
                        can_promote_members=True,
                        can_change_info=True,
                        can_invite_users=True,
                        can_pin_messages=True,
                        can_manage_topics=True
                    ),
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

LOGGER.info("Admin buttons initialized")