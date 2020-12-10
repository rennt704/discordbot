# bot.py
import os
import discord
from dotenv import load_dotenv
from googlesearch import search

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("!quizlet"):
        query = message.content[8:] + " quizlet"
        print(query)
        for j in search(query, tld="co.in", num=10, stop=100, pause=2): 
            print(j)
            if j.startswith("https://quizlet.com"):
                result = j
                break
        await message.channel.send(result)
    else:
        await message.channel.send("Please start your query with !quizlet")

client.run(TOKEN)