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
        plugins={"root": "Naruto.plugins"},
    )

    # Load the database and plugins
    load_db(app)

    # Send a message to the support chat upon bot startup
    try:
        with app:
            app.send_message(SUPPORT_CHAT, "Naruto Bot has started!\nDev: @SexyNano")
            print("Bot deployed successfully.")
    except Exception as e:
        print(f"Error sending startup message: {e}")
     
    app.run()
