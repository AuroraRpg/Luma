import discord
from discord.ext import commands

class Press(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  @commands.command()
  async def fps(self, ctx):
    await ctx.reply("First Person Shooter")


  @commands.command()
  async def new_issue(self, ctx):
    msg = ctx.reply("How many topics are there?")

    def check(m):
      return int(m.content)

    topic_count = await self.bot.wait_for('message', check=check)

    await ctx.reply(f"{topic_count} Topics. Okay")
    topic_num = 1
    for i in range(topic_count):
      msg = await ctx.reply(f'What is the title for Topic {topic_num}')
      topic_num += 1
      #we getting there
      
  
    
  



async def setup(bot):
  await bot.add_cog(Press(bot))