# Work with Python 3.6

import discord
from discord.ext import commands
from googleapiclient.discovery import build
import pprint

token = 'NDkzNDM1MzExNzY3MDI3NzIy.Xkrnfg.ubdKLF1Q2F31JlgIVoRzVN3LUhk'  # Your token here

bot = commands.Bot(command_prefix='~')

# Bot Commands


@bot.command()
async def coms(ctx):
    await ctx.send("""
    !slap <name>
    !wstat(raider.io) <realm> <name>
    !f
    !lst(op.gg) <name>
    !hog
    !lgame""")

# Get slapped
# Sample from Discord.py


@bot.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='for being a lil scrub'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got slapped for {}'.format(slapped, reason))

# Returns Raider.IO profile


@bot.command()
async def wstat(ctx, wow_realm: str, wow_name: str):
    url = 'https://raider.io/characters/eu/%s/%s' % (wow_realm, wow_name)
    await ctx.send(url)

# Press F to Pay Respects


@bot.command()
async def f(ctx):
    await ctx.send(ctx.message.author.mention + " paid respects, rip in pepperoni")

# Returns player data from OP.gg (euw)


@bot.command()
async def lst(ctx, lname: str):
    url2 = 'http://euw.op.gg/summoner/userName=%s' % lname
    await ctx.send(url2)

# Squeeze the Hog


@bot.command()
async def hog(ctx):
    await ctx.send(ctx.message.author.mention + " is squeezing his hog real good, he ain't stopping")

bot.run(token)
