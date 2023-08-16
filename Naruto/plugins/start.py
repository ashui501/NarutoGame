from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Naruto.database.database import add_user, get_user
from Naruto.config.config import SUPPORT_CHAT

@Client.on_message(filters.command("start"))
async def start_command(client, message):
    user_id = message.from_user.id
    username = message.from_user.username
    existing_user = get_user(user_id)
    
    if not existing_user:
        add_user(user_id, username)
        await message.reply("Welcome to Naruto Bot! You've been added to our database.")
    else:
        welcome_back_message = f"Welcome back, {username}!"
        
        # Create an inline keyboard with a button to contact support
        inline_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("Contact Support", url=f"https://t.me/{SUPPORT_CHAT}")]
        ])
        
        await message.reply_text(welcome_back_message, reply_markup=inline_keyboard)

# You can add more commands or functionality to this plugin as needed

