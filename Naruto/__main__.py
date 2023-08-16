import asyncio
from pyrogram import Client
from Naruto.config import API_ID, API_HASH, BOT_TOKEN, DOWNLOAD_DIRECTORY
from Naruto.database import load_db
from Naruto.plugins import load_plugins

async def load_start():
    # Your existing code for loading and starting goes here
    print("Loading and starting process...")

if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(load_start())

    app = Client(
        "NarutoBot",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
        workdir=DOWNLOAD_DIRECTORY,
        sleep_threshold=60,
    )

    # Load the database and plugins
    load_db(app)
    load_plugins(app)

    app.run()

