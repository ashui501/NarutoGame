import random
from pyrogram import Client, filters
from Naruto.database.database import get_user, update_money
from Naruto.config.config import SUPPORT_CHAT

@Client.on_message(filters.command("mission"))
async def mission_command(client, message):
    user_id = message.from_user.id
    user = get_user(user_id)
    
    if user:
        # Simulate a mission with a random reward (for demonstration purposes)
        success_chance = 0.7  # 70% success chance
        reward_range = (20, 50)  # Reward range (min, max)
        
        if random.random() <= success_chance:
            reward = random.randint(*reward_range)
            update_money(user_id, reward)
            await message.reply(f"Mission successful! You earned {reward} money!")
            
            # Notify support chat about the successful mission
            await client.send_message(SUPPORT_CHAT, f"User {user['username']} completed a mission and earned {reward} money.")
        else:
            await message.reply("Mission failed. Better luck next time!")
    else:
        await message.reply("You are not registered in the game.")

# You can add more mission-related commands or functionality to this plugin as needed
