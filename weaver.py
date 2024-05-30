from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')

if not api_id or not api_hash:
    raise ValueError("TELEGRAM_API_ID and TELEGRAM_API_HASH must be set in the .env file")

# Initialize the Telethon client
client = TelegramClient('anon', api_id, api_hash)

def export_chats():
    # Ensure the user is logged in to Telethon
    with client:
        result = client(GetDialogsRequest(
            offset_date=None,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=100,
            hash=0
        ))

    chat_data = []
    for chat in result.chats:
        if hasattr(chat, 'title'):
            title = chat.title
        else:
            title = "Private Chat"
        chat_data.append([title])

    # Create a DataFrame and save to CSV
    df = pd.DataFrame(chat_data, columns=['Chat Title'])
    csv_path = 'chat_list.csv'
    df.to_csv(csv_path, index=False)

    print(f'Chat list has been exported to {csv_path}. You can upload this file to Google Sheets.')

if __name__ == '__main__':
    export_chats()

