import asyncio
from pyrogram import Client
from Naruto.config.config import API_ID, API_HASH, BOT_TOKEN, DOWNLOAD_DIRECTORY, SUPPORT_CHAT
from Naruto.database.database import load_db

async def load_start():
    # Your existing code for loading and starting
    pass

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
        plugins={"root": "Naruto.plugins"},  # Specify the correct path to your plugins
    )

    # Load the database and plugins
    load_db(app)
    
    # Send a message to the support chat upon bot startup
    async def send_startup_message():
        try:
            async with app:
                await app.send_message(SUPPORT_CHAT, "Naruto Bot has started!\nDev: @SexyNano")
                print("Bot has been deployed successfully!")
        except Exception as e:
            print(f"Error sending startup message: {e}")
     
    loop.run_until_complete(send_startup_message())
    app.run()
