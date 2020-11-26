import discord
from discord.ext import commands

bot = commands.Bot(commands_prefix='[')

@bot.event
async def on_ready():
    print("bot inside")

@bot.event
async def on_member_join(member):
    print(f'{member} join!')

@bot.event
async def on_member_remove(member):
    print(f'{member} join!')


bot.run('NzgxMzkzNDA2NjY3Nzg0MjEz.X78_UQ.nKY6kgCzkL9WjV2Nhl2Wc-G-oTU')