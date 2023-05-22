from discord.ext import commands
import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready!")

@bot.slash_command(name="say_duck", description="says the word duck")
async def say_duck(ctx: commands.Context):
    await ctx.send("Duck")

# Run the bot
bot.run(TOKEN)
