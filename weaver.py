from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read API ID and Hash from environment variables
api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')

# Check if the credentials are set
if not api_id or not api_hash:
    raise ValueError("TELEGRAM_API_ID and TELEGRAM_API_HASH must be set in the .env file")

# Initialize the Telethon client with your credentials
client = TelegramClient('anon', api_id, api_hash)

def export_chats():
    # Ensure the user is logged in to Telethon
    with client:
        all_chats = []
        last_date = None
        chunk_size = 100
        while True:
            result = client(GetDialogsRequest(
                offset_date=last_date,
                offset_id=0,
                offset_peer=InputPeerEmpty(),
                limit=chunk_size,
                hash=0
            ))
            if not result.chats:
                break
            all_chats.extend(result.chats)
            last_date = min(msg.date for msg in result.messages)

    chat_data = []
    seen_chat_ids = set()
    for chat in all_chats:
        if chat.id not in seen_chat_ids:
            seen_chat_ids.add(chat.id)
            if hasattr(chat, 'title'):
                title = chat.title
            else:
                title = "Private Chat"
            chat_data.append([title])

    # Create a DataFrame and save it to CSV
    df = pd.DataFrame(chat_data, columns=['Chat Title'])
    csv_path = 'chat_list.csv'
    df.to_csv(csv_path, index=False)

    print(f'Chat list has been exported to {csv_path}. You can upload this file to Google Sheets.')

if __name__ == '__main__':
    export_chats()
