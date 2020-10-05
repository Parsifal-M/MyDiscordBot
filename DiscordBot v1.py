# Work with Python 3.6
import requests
import urllib.request
import time
import requests
import discord
import datetime
from discord.ext import commands
from discord.ext.commands import Bot


token = ''  # Your token here
botPrefix = ('~')
client = Bot(command_prefix=botPrefix)




#EGS Free Game

@client.command()
async def egs(ctx):
    url = 'https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=NL&allowCountries=NL'

    r = requests.get(url)

    data = r.json()

    title1 = data['data']['Catalog']['searchStore']['elements'][0]['title']
    title2 = data['data']['Catalog']['searchStore']['elements'][1]['title']
    title3 = data['data']['Catalog']['searchStore']['elements'][2]['title']

    offerDate1 = data['data']['Catalog']['searchStore']['elements'][0]['effectiveDate']
    offerDate2 = data['data']['Catalog']['searchStore']['elements'][1]['effectiveDate']
    offerDate3 = data['data']['Catalog']['searchStore']['elements'][2]['effectiveDate']

    offerDate1Formatted = datetime.datetime.strptime(offerDate1, '%Y-%m-%dT%H:%M:%S.%f%z').date()
    offerDate2Formatted = datetime.datetime.strptime(offerDate2, '%Y-%m-%dT%H:%M:%S.%f%z').date()
    offerDate3Formatted = datetime.datetime.strptime(offerDate3, '%Y-%m-%dT%H:%M:%S.%f%z').date()

    await ctx.send("Free Game on EGS: " "\n" + title1 + " " + "-" + " " + str(offerDate1Formatted) + "\n" + title2 + " " + "-" + " " + str(offerDate2Formatted) + "\n" + title3 + " " + "-" + " " + str(offerDate3Formatted))


# Bot Commands


@client.command()
async def coms(ctx):
    await ctx.send("""
    ~slap <name>
    ~wstat(raider.io) <realm> <name>
    ~f
    ~lst(op.gg) <name>
    ~hog
    ~egs
    ~lgame""")

# Get slapped
# Sample from Discord.py


@client.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='for being a lil scrub'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got slapped for {}'.format(slapped, reason))

# Returns Raider.IO profile


@client.command()
async def wstat(ctx, wow_realm: str, wow_name: str):
    url = 'https://raider.io/characters/eu/%s/%s' % (wow_realm, wow_name)
    await ctx.send(url)

# Press F to Pay Respects


@client.command()
async def f(ctx):
    await ctx.send(ctx.message.author.mention + " paid respects, rip in pepperoni")

# Returns player data from OP.gg (euw)


@client.command()
async def lst(ctx, lname: str):
    url2 = 'http://euw.op.gg/summoner/userName=%s' % lname
    await ctx.send(url2)

# Squeeze the Hog


@client.command()
async def hog(ctx):
    await ctx.send(ctx.message.author.mention + " is squeezing his hog real good, he ain't stopping")


client.run(token)
