# Weaver

Weaver is a simple script to export your Telegram chat titles to a CSV file using the Telethon library. This project uses environment variables to securely manage your Telegram API credentials.

## Prerequisites

- Python 3.x
- Telegram account
- Telegram API ID and API Hash (obtain these from [my.telegram.org](https://my.telegram.org))

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/weaver.git
   cd weaver
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory and add your Telegram API credentials:
   ```plaintext
   TELEGRAM_API_ID=YOUR_API_ID
   TELEGRAM_API_HASH=YOUR_API_HASH
   ```

## Usage

1. Ensure your environment variables are set in the `.env` file.
2. Run the script to export your chat titles to a CSV file:
   ```bash
   python export_chats.py
   ```
3. The script will generate a `chat_list.csv` file in the project directory, which you can upload to Google Sheets.

## Project Structure

weaver/
│
├── .env # Environment variables (not included in the repo)
├── .gitignore # Git ignore file
├── export_chats.py # Main script to export chats
├── README.md # Project README file
├── requirements.txt # Python dependencies
└── venv/ # Virtual environment directory (optional)

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
