import discord
from discord.ext import commands
from logic import create_graph

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def harita(ctx, city: str = None):
    path = create_graph(city)
    
    if path:
        with open(path, 'rb') as f:
            await ctx.send(file=discord.File(f))
    else:
        await ctx.send("Hata!")

bot.run('TOKEN_BURAYA')
