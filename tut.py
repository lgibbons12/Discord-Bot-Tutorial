import discord
from discord.ext import commands


from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents, description="I am a cool bot")


class SimpleView(discord.ui.View):

    foo  : bool = None


    async def disable_all_items(self):
        for item in self.children:
            item.disabled = True
        
        await self.message.edit(view=self)
    async def on_timeout(self) -> None:
        await self.message.channel.send("Timeout")
        await self.disable_all_items()
    
    @discord.ui.button(label="Hello", style=discord.ButtonStyle.success)
    async def hello(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("World")
        self.foo = True
        self.stop()
    
    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.red)
    async def cancel(self, interaction: discord.Interaction, button: discord.Button):
        await interaction.response.send_message("Cancelling")
        self.foo = False
        self.stop()

def add(a, b):
    return a + b

@bot.command()
async def test(ctx, arg1, arg2):
    await ctx.send(add(int(arg1), int(arg2)))

import random as r

class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = r.choice(ctx.guild.members)
        return f"{ctx.author} slapped {to_slap} because *{argument}*"

@bot.command()
async def slap(ctx, *, reason: Slapper):
    await ctx.send(reason)

@bot.command()
async def button(ctx):
    view = SimpleView(timeout=50)
    #button = discord.ui.Button(label="Click me")
    #view.add_item(button)

    message = await ctx.send(view=view)
    view.message = message
    await view.wait()
    await view.disable_all_items()

    if view.foo is None:
        print("Timeout")
    elif view.foo == True:
        print("Ok")
    else:
        print("cancel")



bot.run(TOKEN)