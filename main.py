import logging
from pyrogram import Client, filters
from pyrogram.raw.functions.messages import SendMessage
from pyrogram.raw.types import (
    ReplyKeyboardMarkup as RawReplyKeyboardMarkup,
    KeyboardButtonRow,
    KeyboardButtonRequestPeer,
    RequestPeerTypeUser,
    RequestPeerTypeChat,
    RequestPeerTypeBroadcast,
    InputPeerUser,
    PeerUser,
    PeerChat,
    PeerChannel,
    UpdateNewMessage,
    MessageService,
    MessageActionRequestedPeer
)
from pyrogram.enums import ParseMode
from config import API_ID, API_HASH, BOT_TOKEN

# LOGGER SETUP
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Initialize the Pyrogram client
app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Handle /start command
@app.on_message(filters.command("start"))
async def handle_new_message(client, message):
    chat_id = message.chat.id
    text = message.text

    logging.info(f"Received /start message: text='{text}', chat_id={chat_id}")

    welcome_text = (
        "👋 Welcome to Chat ID Finder Bot! 🆔\n\n"
        "✅ Fetch Any Chat ID Instantly!\n\n"
        "🔧 How to Use?\n"
        "1️⃣ Click the buttons below to share a chat or user.\n"
        "2️⃣ Receive the unique ID instantly.\n\n"
        "💎 Features:\n"
        "✅ Supports users, bots, groups & channels\n"
        "⚡ Fast and reliable\n\n"
        "🛠 Made with ❤️ by @TheSmartDev"
    )

    # Define the keyboard rows using raw types
    rows = [
        KeyboardButtonRow(buttons=[
            KeyboardButtonRequestPeer(
                text='👤 User',
                button_id=1,
                peer_type=RequestPeerTypeUser(bot=False)
            )
        ]),
        KeyboardButtonRow(buttons=[
            KeyboardButtonRequestPeer(
                text='🔒 Private Channel',
                button_id=2,
                peer_type=RequestPeerTypeBroadcast(has_username=False)
            ),
            KeyboardButtonRequestPeer(
                text='🌐 Public Channel',
                button_id=3,
                peer_type=RequestPeerTypeBroadcast(has_username=True)
            )
        ]),
        KeyboardButtonRow(buttons=[
            KeyboardButtonRequestPeer(
                text='🔒 Private Group',
                button_id=4,
                peer_type=RequestPeerTypeChat(has_username=False)
            ),
            KeyboardButtonRequestPeer(
                text='🌐 Public Group',
                button_id=5,
                peer_type=RequestPeerTypeChat(has_username=True)
            )
        ]),
        KeyboardButtonRow(buttons=[
            KeyboardButtonRequestPeer(
                text='🤖 Bot',
                button_id=6,
                peer_type=RequestPeerTypeUser(bot=True)
            ),
            KeyboardButtonRequestPeer(
                text='Premium 🌟',
                button_id=7,
                peer_type=RequestPeerTypeUser(premium=True)
            )
        ])
    ]

    # Create the raw reply markup
    reply_markup = RawReplyKeyboardMarkup(
        rows=rows,
        resize=True,
        single_use=False,
        selective=False
    )

    # Resolve the chat_id to an InputPeer
    peer = InputPeerUser(user_id=chat_id, access_hash=0)

    # Parse the text and extract entities correctly
    parsed = await client.parser.parse(welcome_text, ParseMode.HTML)
    _, entities = parsed.values()

    # Use invoke to send the message with raw reply markup
    await client.invoke(
        SendMessage(
            peer=peer,
            message=welcome_text,
            random_id=client.rnd_id(),
            reply_markup=reply_markup,
            entities=entities
        )
    )
    logging.info("Sent welcome message with keyboard")

# Raw update handler to process peer-sharing updates
@app.on_raw_update()
async def raw_update_handler(client, update, users, chats):
    logging.info(f"[RAW UPDATE] Received update: {update}")

    # Check if this update is a new message with a peer-sharing action
    if isinstance(update, UpdateNewMessage) and isinstance(update.message, MessageService):
        message = update.message
        if isinstance(message.action, MessageActionRequestedPeer):
            chat_id = message.peer_id.user_id  # The chat where the message was sent (user's chat)
            request_id = message.action.button_id  # The button ID (matches keyboard)
            peer = message.action.peer  # The shared peer

            # Map request_id to peer type
            types = {
                1: 'User',
                2: 'Private Channel',
                3: 'Public Channel',
                4: 'Private Group',
                5: 'Public Group',
                6: 'Bot',
                7: 'Premium User'
            }
            type_ = types.get(request_id, 'Unknown')

            # Extract the peer ID based on peer type
            if isinstance(peer, PeerUser):
                peer_id = peer.user_id
                user = users.get(peer_id)
                is_bot = user.is_bot if user else False
                if request_id == 6 and not is_bot:
                    type_ = 'Bot (but not a bot)'
                response = f"👤 <b>Shared {type_} Info</b>\n🆔 ID: <code>{peer_id}</code>"
                await client.send_message(chat_id, response, parse_mode=ParseMode.HTML)
                logging.info(f"Sent user ID: {peer_id}")
            elif isinstance(peer, (PeerChat, PeerChannel)):
                # Extract the raw chat/channel ID
                raw_peer_id = peer.chat_id if isinstance(peer, PeerChat) else peer.channel_id
                # Format the ID with -100 prefix for channels and supergroups
                peer_id = int(f"-100{raw_peer_id}")
                # Try to get chat details from chats dict or fetch manually
                chat = chats.get(raw_peer_id)
                if not chat:
                    try:
                        # Fetch chat details manually using the formatted ID
                        chat = await client.get_chat(peer_id)
                        logging.info(f"Fetched chat details: {chat}")
                    except Exception as e:
                        logging.error(f"Failed to fetch chat details: {e}")
                        chat = None
                if chat:
                    chat_type = chat.type
                    if chat_type in ["group", "supergroup"]:
                        type_ = "Group" if type_ == "Unknown" else type_
                    elif chat_type == "channel":
                        type_ = "Channel" if type_ == "Unknown" else type_
                    response = f"💬 <b>Shared {type_} Info</b>\n🆔 ID: <code>{peer_id}</code>"
                    await client.send_message(chat_id, response, parse_mode=ParseMode.HTML)
                    logging.info(f"Sent chat ID: {peer_id}")
                else:
                    # If we can't fetch chat details, still send the ID
                    response = f"💬 <b>Shared {type_} Info</b>\n🆔 ID: <code>{peer_id}</code>"
                    await client.send_message(chat_id, response, parse_mode=ParseMode.HTML)
                    logging.info(f"Sent chat ID (without details): {peer_id}")
            else:
                logging.info("Unknown peer type in MessageActionRequestedPeer")
                await client.send_message(
                    chat_id,
                    "<b>Looks Like I Don't Have Control Over The User</b>",
                    parse_mode=ParseMode.HTML
                )
            return

    logging.info("Raw update did not contain peer-sharing data")

# Run the bot
print("✅ Bot Is Up And Running On Pyrogram Stable")
app.run()
