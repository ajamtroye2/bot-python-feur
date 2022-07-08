import discord
from discord.ext import commands
import typing

bot = commands.Bot(command_prefix = "", description = "Bot de test")
client = discord.Client()

@bot.event
async def on_ready():
  print("Le bot est prêt {0.user}".format(bot))

@bot.command()
async def quoi(msg):
  print("feur")
  await msg.send("feur")

@bot.command()
async def quoii(msg):
  print("feur")
  await msg.send("feur")

@bot.command()
async def quoiii(msg):
  print("feur")
  await msg.send("feur")

@bot.command()
async def quoiiii(msg):
  print("feur")
  await msg.send("nan mais la y'a trop de i")

@bot.command()
async def QUOI(msg):
  print("feur")
  await msg.send("feur") 

@bot.command()
async def QUOUA(msg):
  print("feur")
  await msg.send("feur")

@bot.command()
async def quoa(msg):
  print("feur")
  await msg.send("feur")

@bot.command()
async def rep(ctx, arg):
    await ctx.send(arg)

    
@bot.command()
async def C(ctx, *, arg):
    fin = arg.split() 
    nb = len(fin)
    print(nb)
    if fin[-1] == "quoi" or fin[-1] == "quoi?":
        print("feur")
        await ctx.send("feur")
    elif fin[-1] == "?" and fin[-2] == "quoi":
        print("feur")
        await ctx.send("feur")
    elif fin[-1] == "!" and fin[-2] == "quoi":
        print("feur")
        await ctx.send("feur")
        
@bot.command()
async def c(ctx, *, arg):
    fin = arg.split() 
    nb = len(fin)
    print(nb)
    if fin[-1] == "quoi" or fin[-1] == "quoi?":
        print("feur")
        await ctx.send("feur")
    elif fin[-1] == "?" and fin[-2] == "quoi":
        print("feur")
        await ctx.send("feur")
    elif fin[-1] == "!" and fin[-2] == "quoi":
        print("feur")
        await ctx.send("feur")

async def is_owner(ctx):
    return ctx.author.id == 561824789040332824

@bot.command()
@commands.check(is_owner)
async def ban(ctx, members: commands.Greedy[discord.Member],
                   delete_days: typing.Optional[int] = 0, *,
                   reason: str):
    """Mass bans members with an optional delete_days parameter"""
    for member in members:
        await member.ban(delete_message_days=delete_days, reason=reason)
  


bot.run("ODc5ODM1MDQ5MTc5MTA3NDU4.GmSUC-.PMMA0X_VaXyzvru422IRIz_TcsXZ3Dmc0g4DyE")


