# money.py

from pyrogram import Client, filters
from Naruto.database.database import get_user, update_money
from Naruto.config.config import SUPPORT_CHAT

@Client.on_message(filters.command("checkmoney"))
async def check_money(client, message):
    user_id = message.from_user.id
    username = message.from_user.username
    user = get_user(user_id, username)
    
    if user:
        money = user.get("money", 0)
        await message.reply(f"Your current money: {money}")
    else:
        await message.reply("You are not registered in the game.")

# Add more money-related commands or functionality to this plugin as needed


@Client.on_message(filters.command("earnmoney"))
async def earn_money(client, message):
    user_id = message.from_user.id
    username = message.from_user.username
    user = get_user(user_id, username)
    
    if user:
        username = user.get("username")
        # Simulate earning money (for demonstration purposes)
        earned_money = 50
        update_money(user_id, earned_money)
        await message.reply(f"{username}, you earned {earned_money} money!")
    else:
        await message.reply("You are not registered in the game.")

@Client.on_message(filters.command("spendmoney"))
async def spend_money(client, message):
    user_id = message.from_user.id
    username = message.from_user.username
    user = get_user(user_id, username)
    
    if user:
        username = user.get("username")
        money = user.get("money", 0)
        
        if money >= 30:
            spent_money = 30
            update_money(user_id, -spent_money)
            await message.reply(f"{username}, you spent {spent_money} money. Your remaining money: {money - spent_money}")
        else:
            await message.reply("You don't have enough money to spend.")
    else:
        await message.reply("You are not registered in the game.")

@Client.on_message(filters.command("donate"))
async def donate_money(client, message):
    user_id = message.from_user.id
    username = message.from_user.username
    user = get_user(user_id, username)
    
    if user:
        username = user.get("username")
        money = user.get("money", 0)
        amount = 20
        
        if money >= amount:
            # Simulate donating money (for demonstration purposes)
            receiver_username = "recipient_username"
            update_money(user_id, -amount)
            await message.reply(f"{username}, you donated {amount} money to {receiver_username}!")
            
            # Notify support chat about the donation
            await client.send_message(SUPPORT_CHAT, f"User {username} donated {amount} money to {receiver_username}.")
        else:
            await message.reply("You don't have enough money to donate.")
    else:
        await message.reply("You are not registered in the game.")
