import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Your Finnhub API key
FINNHUB_APIKEY: str = os.getenv('FINNHUB_APIKEY', 'your_finnhub_apikey')
assert FINNHUB_APIKEY != 'your_finnhub_apikey', "Please set your FINNHUB_APIKEY in .env"

# Your Discord bot token
DISCORD_BOT_TOKEN: str = os.getenv('DISCORD_BOT_TOKEN', 'your_discord_bot_token')
assert DISCORD_BOT_TOKEN != 'your_discord_bot_token', "Please set your DISCORD_BOT_TOKEN in .env"

# Discord channel IDs (comma-separated in .env)
DISCORD_BOT_CHANNEL_IDS: list = [int(_id.strip()) for _id in
                                 os.getenv('DISCORD_BOT_CHANNEL_IDS', '').split(",") if _id.strip()]
assert len(DISCORD_BOT_CHANNEL_IDS) > 0, "Please set at least one Discord channel ID in .env"

# Time period for checking IPO statuses (in seconds)
IPO_POLLING_PERIOD = 30