import json
import random
import asyncio
from pyrogram import Client, filters
from Naruto.database.database import get_user, update_user
from Naruto.config.config import SUPPORT_CHAT

# Load character data from character.json
with open("character.json", "r") as character_file:
    character_data = json.load(character_file)

# Store the group IDs and their message counts
group_message_counts = {}

# Command to handle spawning characters in the 10th message
@Client.on_message(filters.group & ~filters.edited & ~filters.bot)
async def spawn_character_in_group(client, message):
    group_id = message.chat.id
    if group_id not in group_message_counts:
        group_message_counts[group_id] = 0
    group_message_counts[group_id] += 1

    if group_message_counts[group_id] == 10:
        character = random.choice(character_data)
        character_id = character["id"]
        character_name = character["name"]
        image_link = character["image"]

        await client.send_photo(group_id, image_link, caption=f"Character ID: {character_id}\nAnime: {character['anime']}\nName: {character_name}")

        # Store the spawned character in the group's data (for challenges)
        group_message_counts[group_id] = 0
        if "spawned_characters" not in group_message_counts:
            group_message_counts["spawned_characters"] = {}
        group_message_counts["spawned_characters"][group_id] = character

# Command for challenging characters
@Client.on_message(filters.command("challenge"))
async def challenge_character(client, message):
    user_id = message.from_user.id
    user = get_user(user_id)

    if user:
        group_id = message.chat.id
        if "spawned_characters" in group_message_counts and group_id in group_message_counts["spawned_characters"]:
            current_character = group_message_counts["spawned_characters"][group_id]
            character_name = current_character["name"]
            character_level = current_character.get("level", 1)

            user_level = user.get("level", 10)
            win_probability = min(user_level * 10, 90)

            await message.reply(f"Battle starting in 3 seconds against {character_name} (Level: {character_level})...")

            await asyncio.sleep(3)

            if random.randint(1, 100) <= win_probability:
                await message.reply(f"You won against {character_name}! Congratulations!")
            else:
                await message.reply(f"You lost against {character_name}. Better luck next time!")

            del group_message_counts["spawned_characters"][group_id]
        else:
            await message.reply("No character has been spawned in this group yet.")
    else:
        await message.reply("You need to register in the game to participate in challenges.")

# You can add more features and functionality to this plugin as needed
