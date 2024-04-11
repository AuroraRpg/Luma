import os
import discord
import requests
from discord.ext import commands
from discord.ext.commands import Bot, has_permissions, MissingPermissions
import asyncio
import resources.gn_resources as gn


intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!?", intents=intents)

@bot.event
async def on_ready():
  print("I'm online!")

@bot.command(pass_context=True)
async def ping(ctx):
  embed = discord.Embed(description="Pong 🏓", colour=discord.Color.blurple())
  await ctx.reply(embed=embed)

async def load_cogs():
  initial_extensions = []
  
  for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])
  
  if __name__ == '__main__':
      for extension in initial_extensions:
        await bot.load_extension(extension)
        print(f"Loaded {extension}")
      print("Loaded all cogs")



async def main():
  token = os.environ['LUMA_TOKEN']
  await gn.fetch()
  await load_cogs()
  await bot.start(token)


asyncio.run(main())