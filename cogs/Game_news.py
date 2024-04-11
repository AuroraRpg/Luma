import discord
from discord.ext import commands
import requests
import os

gamespot = os.environ['GAMESPOT_TOKEN']

class GameNews(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  @commands.command()
  async def fetch(self, ctx):
    url = f"http://www.gamespot.com/api/articles/?api_key={gamespot}"
    data = requests.get(url)
    parsed = data.json()
    print(data)
    






async def setup(bot):
  await bot.add_cog(GameNews(bot))