#IMPORT LIRARY



# import PyNacl
# import randfacts
import base64
from translate import Translator
from keep_alive import keep_alive
import discord
from discord.ext import commands
import wikipedia
import aiohttp
from discord import Game, Intents
from os import environ, listdir
from random import *
import random
from discord.utils import get
import os
import random
import json
from datetime import datetime
from mcstatus import MinecraftServer
import os
import asyncio
from discord import Intents
from discord import FFmpegPCMAudio
import urllib.parse, urllib.request, re
import random
import string
import sys
from replit import db
import smtplib
import ffmpeg
import itertools
import traceback
from async_timeout import timeout
from functools import partial
from youtube_dl import YoutubeDL
import lyricsgenius
#from googlesearch import search 

os.system("pip install PyNacl")
intents = discord.Intents.default()
intents.members = True
intents = Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)
client.remove_command("help")
OWNERID = 616680119079272551

with open("badw.txt") as file:
    bad_words = [bad_word.strip().lower() for bad_word in file.readlines()]
   
 
@client.command()
@commands.has_permissions(administrator=True)
async def addrole(ctx, member: discord.Member, *,role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f"{role} is added to {member}.")


@client.command()
@commands.has_permissions(administrator=True)
async def removerole(ctx, member: discord.Member, *,role: discord.Role):
    await member.remove_roles(role)
    await ctx.send(f"{role} is removed from {member}.")


@client.event
async def on_message(message):
		message.content = message.content.lower()
		if any(bad_word in message.content for bad_word in bad_words):
				await message.channel.send("{}, No bad words please!".format(message.author.mention))
		await client.process_commands(message)
		if message.author == client.user:
				return
		print(f"{message.guild.name}: {message.author.name} sent: {message.content}")


@client.command()
async def bmi(ctx, weight, height):
    try:
        x = float(height) * float(height)
        y = float(weight)
        z = float(y) / float(x)
        n = z * 10000
        BMI = n
        if BMI <= (18.5):
            embed = discord.Embed(
                title="Underweight !",
                description=f"You Have {BMI} So You Are Underweight !"
                '')
        if BMI >= (19) and BMI <= (24.9):
            embed = discord.Embed(
                title="Normal .",
                description=f"You Have {BMI} So You Are Normal ."
                '')
        if BMI >= (25):
            embed = discord.Embed(
                title="Overweight !",
                description=f"You Have {BMI} So You Are Overweight !"
                '')
        else:
            embed = discord.Embed(
                title="ERROR !",
                description=f"Example : '!bmi weight height'"
                '')
        await ctx.send(embed=embed)
    except:
        embed = discord.Embed(
            title="ERROR !", description=f"Example : '!bmi weight height'"
            '')
        await ctx.send(embed=embed)



@client.command()
async def hi(ctx):
    await ctx.send("{}, hello".format(ctx.author.mention))


# @client.command()
# async def join(ctx):
#     if not ctx.message.author.voice:
#         await ctx.send("You are not connected to a voice channel!")
#         return
#     else:
#         channel = ctx.message.author.voice.channel
#         user = ctx.message.author.mention
#         await ctx.send(f'{user}, Connected to {channel} (if i am bot connected this is because there is an error using this command)')
#         await ctx.message.add_reaction('✅')
#     await channel.connect()

# @client.command()
# async def leave(ctx):
#     voice_client = ctx.message.guild.voice_client
#     user = ctx.message.author.mention
#     channel = ctx.message.author.voice.channel
#     if not voice_client:
#         await ctx.send(f"{user} I am not connected to a voice channel")
#     else:
#         await voice_client.disconnect()
#         await ctx.send(f'{user}, Disconnected from {channel}')
#         await ctx.message.add_reaction('✅')


@client.command(aliases=["m", "M", "Mute"])
@commands.has_permissions(administrator=True)
async def mute(ctx, *, member: discord.Member):
    command_name = "mute"
    author = ctx.author
    await member.edit(mute=True)
    await ctx.send(f"{member.mention} is muted")
    await ctx.message.add_reaction('✅')


@client.command(aliases=["unm", "UNM", "Unmute"])
@commands.has_permissions(administrator=True)
async def unmute(ctx, *, member: discord.Member):
    command_name = "unmute"
    author = ctx.author
    await member.edit(mute=False)
    await ctx.send(f"{member.mention} is unmuted")
    await ctx.message.add_reaction('✅')


@client.command()
@commands.has_permissions(administrator=True)
async def vcmute(ctx):
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=True)
        await ctx.send("everybody was muted")
        await ctx.message.add_reaction('✅')
        break


@client.command()
@commands.has_permissions(administrator=True)  #new one to karim
async def deafen(ctx, *, member: discord.Member):
    command_name = "deafen"
    author = ctx.author
    await member.edit(deafen=True)
    await ctx.send(f"{member.mention} is deafened")


@client.command()
@commands.has_permissions(administrator=True)  #new one to karim
async def undeafen(ctx, *, member: discord.Member):
    command_name = "undeafen"
    author = ctx.author
    await member.edit(deafen=False)
    await ctx.send(f"{member.mention} is undeafened")


@client.command()  #new one to karim
@commands.has_permissions(administrator=True)
async def vcdeafen(ctx):
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(deafen=True)
        await ctx.send("everybody was deafened")
        await ctx.message.add_reaction('✅')
        break


@client.command()  #new one to karim
@commands.has_permissions(administrator=True)
async def vcundeafen(ctx):
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(deafen=False)
        await ctx.send("everybody was undeafened")
        await ctx.message.add_reaction('✅')
        break


@client.command()
@commands.has_permissions(administrator=True)
async def vcunmute(ctx):
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=False)
        await ctx.send("everybody was unmuted")
        await ctx.message.add_reaction('✅')
        break


@client.command()  #new one to karim
async def mincraftserver(ctx):
    server = MinecraftServer.lookup("mc.hypixel.net")
    status = server.status()
    await ctx.send("The server has {0} players and replied in {1} ms".format(
        status.players.online, status.latency))


@client.event  #ready
async def on_ready():
    print('{0.user} bot is ready'.format(client))
    current_guilds = len(client.guilds)
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Game(f'!help | Serving {current_guilds} servers'))
    '''for guild in client.guilds:
        for member in guild.members:
            print(member)'''
    members = []

    for guild in client.guilds:
        members.extend(guild.members)

    members_set = set(members)
    members_served = len(members_set)
    print(members_served)

    print('Servers connected to:')
    for guild in client.guilds:
        print(guild.name)
    await asyncio.sleep(3)


@client.command()  #memes
async def meme(ctx):
    embed = discord.Embed(title="", description="")
    try:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(
                    'https://www.reddit.com/r/dankmemes/new.json?sort=hot'
            ) as r:
                res = await r.json()
                embed.set_image(
                    url=res['data']['children'][randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)
    except:
        await ctx.send(
            "Couldn't get meme, please try again. (contact @NOT kar1m yt#0001 the creator of The Kid Laroi bot for more info)."
        )


@client.command()  #definitions
async def definition(ctx, word):
    if (word == None):
        await ctx.send("Please enter a word")
    try:
        await ctx.send(wikipedia.summary(word))
    except:
        await ctx.send("No definition found")


@client.command()
async def calc(ctx, *, lst):
    try:
        x = eval(str(lst.replace(':', '/').replace('x', '*').lower()))
        embed = discord.Embed(title=f"Your Answer Is {x}")
        await ctx.send(embed=embed)
    except:
        await ctx.send("Wrong, Example: !calc 1 + 1 - 1 x 1")


@client.command()  #ultimate_infos
async def help(ctx, member: discord.User = None):
    embed = discord.Embed(
        title='Need Help Using Me ?',
        color=0xFFA07A,
        url='https://marawan-pablo-help.notkar1myt.repl.co',
        description='this site is for all commands')
    embed.set_thumbnail(url=client.user.avatar_url)
    await ctx.send(embed=embed)
    await ctx.message.add_reaction('✅')


# ❌
@client.command(aliases=["cm", "CM", "Cmute"])
@commands.has_permissions(administrator=True)
async def cmute(ctx, *, member: discord.Member):
    command_name = "mute"
    author = ctx.author
    await member.edit(send_messages=False)
    await ctx.send(f"{member.mention} is muted")
    await ctx.message.add_reaction('✅')


@client.command(aliases=["cunm", "CUNM", "Cunmute"])
@commands.has_permissions(administrator=True)
async def cunmute(ctx, *, member: discord.Member):
    command_name = "unmute"
    author = ctx.author
    await member.edit(send_messages=True)
    await ctx.send(f"{member.mention} is unmuted")
    await ctx.message.add_reaction('✅')


@client.command()
async def lol(ctx):
    await ctx.send("😂")


@client.command()
async def studing(ctx):
    await ctx.send("study good for full marks 🙂")


@client.command()
async def thx(ctx):
    await ctx.send("your welcome 😉")


@client.command()
async def bye(ctx):
    await ctx.send("bye, {} 🙂".format(ctx.author.mention))


@client.command()
async def goodnite(ctx):
    await ctx.send("{} goodnite and sweat dreams ♥️  ".format(
        ctx.author.mention))


@client.command()  #ping
async def ping(ctx):
    embed = discord.Embed(
        title=f'My Ping is {round(client.latency * 1000)}ms', color=0x0061ff)
    await ctx.send(embed=embed)

# @client.command(aliases=["fact"])
# async def funfact(ctx):
# 	fact = randfacts.getFact()
# 	embed = discord.Embed(title="Fun Fact",
# 	description=f"{fact}")
# 	await ctx.send(embed=embed)

@client.command(
    description="bans a user with specific reason (only admins)")  #ban
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.User = None, *, reason=None):
    try:
        if (reason == None):
            await ctx.channel.send("You  have to specify a reason!")
            return
        if (member == ctx.message.author or member == None):
            await ctx.send("""You cannot ban yourself!""")
        else:
            message = f"You have been banned from {ctx.guild.name} for {reason}"
            await member.send(message)
            await ctx.guild.ban(member, reason=reason)
            print(member)
            print(reason)
            await ctx.channel.send(f"{member} is banned!")
    except:
        await ctx.send(f"Error banning user {member} (cannot ban owner or bot)"
                       )


@client.command(
    description="kicks a user with specific reason (only admins)")  #kick
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.User = None, *, reason=None):
    try:
        if (reason == None):
            await ctx.channel.send("You  have to specify a reason!")
            return
        if (member == ctx.message.author or member == None):
            await ctx.send("""You cannot kick yourself!""")

        else:
            message = f"You have been kicked from {ctx.guild.name} for {reason}"
            await member.send(message)
            await ctx.guild.kick(member, reason=reason)
            print(member)
            print(reason)
            await ctx.channel.send(f"{member} is kicked!")
    except:
        await ctx.send(
            f"Error kicking user {member} (cannot kick owner or bot)")


@client.event
async def on_guild_join(guild):  #bot joins
    embed = discord.Embed(
        title='Need Help Using Me ?',
        color=0x0061ff,
        url='http://karimhany.karimkhalifa.com/mbot/',
        description=
        'this site is for all commands\nthis domain is provided by kimo#3163')
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            print(f"joined *{guild.name}*")
            await channel.send(embed=embed)
        break


@client.command(
    description="Gives random number between the 2 numbers : Ex `$random 1 5`"
)  #random
async def random(ctx, num1, num2=None):
    try:
        if (num2 == None or num1 == None):
            await ctx.send(
                "Please provide 2 numbers to choose from. Ex: `$random 1 5` this will give you a random number between 1 and 5."
            )
            return
        else:
            num1 = int(num1)
            num2 = int(num2)

    except:
        await ctx.send(
            "Please provide 2 numbers and not words Ex: `!random 1 5` this will give you a random number between 1 and 5."
        )
        return
    try:

        await ctx.send(f"Random number: {randint(num1, num2)}")
    except:
        await ctx.send(
            "Error: couldn't choose random number \n How to use command: Ex: `!random 1 3` this will return you a random number between 1 and 3."
        )


@client.command(pass_context=True)  #warn
@commands.has_permissions(administrator=True)
#@commands.is_owner()
async def warn(ctx, member: discord.User = None, *, reason=None):
    if member.name == "NOT kar1m yt":
        await ctx.send("You cannot warn an owner")
    else:
        message = f"You have been warned from {ctx.guild.name} for {reason}"
        await member.send(message)
        await ctx.channel.send(f"✅ **@{member}** has been warned for {reason}")


@client.command(pass_context=True)  #change nickname
@commands.has_permissions(administrator=True)
async def chnick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f"Nickname was changed for {member.mention}")


@client.command()  #lock
#@commands.is_owner()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('Channel locked.')


@client.command()  #lock
#@commands.is_owner()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.send('Channel unlocked.')


@client.command(pass_context=True)  #reset nickname
@commands.has_permissions(administrator=True)
async def renick(ctx, member: discord.Member):
    await member.edit(nick=None)
    await ctx.send(f"Nickname was reseted for {member.mention}")


@client.command()
async def game(ctx):
    await ctx.send("entered game mode")

    @client.command()
    async def attack(ctx, member: discord.User = None):
        guild = ctx.guild
        await guild.create_role(name="Attacker")
        if (member == None):
            await ctx.send("please mention someone to attack !")
        else:
            role = discord.utils.get(ctx.guild.roles, name="Attacker")
            user = ctx.message.author
            await user.add_roles(role)
            await ctx.channel.send(
                f"{member} is attacked, will he defend back ????")
            await asyncio.sleep(15)
            role = discord.utils.get(ctx.guild.roles, name="Attacker")
            user = ctx.message.author
            await user.remove_roles(role)

        @client.command()
        async def defend(ctx):
            guild = ctx.guild
            await guild.create_role(name="Defender")
            role = discord.utils.get(ctx.guild.roles, name="Defender")
            user = ctx.message.author
            await user.add_roles(role)
            await ctx.send("{} defended himself".format(ctx.author.mention))
            await asyncio.sleep(5)
            role = discord.utils.get(ctx.guild.roles, name="Defender")
            user = ctx.message.author
            await user.remove_roles(role)


@client.command()
async def yt(ctx, channel=None):
    if channel == None:
        await ctx.send("please specify a channel")
    elif channel == "kodiks":
        await ctx.send("http://youtube.com/channel/UCg5IIWjA0JS34tTd_b8lbLQ")
    elif channel == "kodiksvfx":
        await ctx.send("http://youtube.com/channel/UCg5IIWjA0JS34tTd_b8lbLQ")
    elif channel == "kar1m":
        await ctx.send(
            "https://www.youtube.com/channel/UCerf1Gxg4WhXUTui8c9lWlw")
    elif channel == "snow":
        await ctx.send(
            "https://www.youtube.com/channel/UCQDvIKeI0aL3SqKXYY9kJiw")
    elif channel == '2k_dayninja':
        await ctx.send(
            "https://www.youtube.com/channel/UCOYu-6etnbY2jHwXR_u5HgA")
    elif channel == "kaccha":
        await ctx.send("https://youtube.com/channel/UCMvB99ahsLjswO6nDBEUDA")
    else:
        await ctx.send("invalid format , example '!yt kodiks'")


@client.command()
async def time(ctx):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")


@client.command()
async def servers(ctx):
    activeservers = client.guilds
    for guild in activeservers:
        await ctx.send(guild.name)

# def flaskservers():
# 	activeservers = client.guilds
# 	servers = ""
#     for guild in activeservers:
#         #await ctx.send(guild.name)
# 		servers += f"{guild.name}\n"
# 	return servers

@client.event
async def on_member_join(member):
    if member.guild.name == 'kar1mHub':
        embed = discord.Embed(
            title=
            f'welcome {member.name} !\nwelcome to {member.guild.name} go see #✨how-roles-work and #✨rules ',
            color=0x0061ff,
            font_size=200)
        embed.set_thumbnail(url=member.avatar_url)
        await client.get_channel(755836023069474947).send(
            f"{member.mention}", embed=embed)
        role = discord.utils.get(member.guild.roles, name="Community")
        await member.add_roles(role)
    elif member.guild.name == 'SacRed Gaming':
        embed = discord.Embed(
            title=
            f'welcome {member.name} !\nwelcome to {member.guild.name} You Are The {member.count}th member',
            color=0x0061ff,
            font_size=200)
        embed.set_thumbnail(url=member.avatar_url)
        await client.get_channel(771067666235916348).send(
            f"{member.mention}", embed=embed)
    elif member.guild.name == 'Promise':
        embed = discord.Embed(
            title=
            f'welcome {member.name}!\n1 - Read our rules : #rules\n2 - Go & chat : #chat؛\n-3 - Have a wonderfull day ^^.',
            color=0x0061ff,
            font_size=200)
        await client.get_channel(787846332437626900).send(
            f"{member.mention}", embed=embed)
        role = discord.utils.get(member.guild.roles, name="Member's")
        await member.add_roles(role)
    else:
        return


@client.event
async def on_member_remove(member):
    if member.guild.name == 'kar1mHub':
        embed = discord.Embed(
            title=
            f'Bye {member.name} !\nYou will be missed by {member.guild.name}',
            color=0x0061ff)
        await client.get_channel(789858919949664296).send(embed=embed)
    if member.guild.name == "Kodik's Editing Server":
        embed = discord.Embed(
            title=
            f'Bye {member.name} !\nYou will be missed by {member.guild.name}',
            color=0x0061ff)
        await client.get_channel(782213231900491796).send(embed=embed)
    else:
        return


#@commands.is_owner()


@client.command(alias=["remindme", "reminder"])
async def remind(ctx, time, *, mode):
    if mode == 's':
        embed = discord.Embed(
            title=f"{ctx.author.name}",
            description=f"{ctx.author.name} {time} {mode} Has Passed",
            color=0x0061ff)
        await ctx.send(f"```py\nI Will Remind You In {time} {mode}```")
        await asyncio.sleep(int(time))
        await ctx.send(embed=embed)
    elif mode == 'm':
        embed = discord.Embed(
            title=f"{ctx.author.name}",
            description=f"{ctx.author.name} {time} {mode} Has Passed",
            color=0x0061ff)
        await ctx.send(f"```I Will Remind You In {time} {mode} ```")
        await asyncio.sleep(int(time * 60))
        await ctx.send(embed=embed)
    elif mode == 'h':
        embed = discord.Embed(
            title=f"{ctx.author.name}",
            description=f"{ctx.author.name} {time} {mode} Has Passed",
            color=0x0061ff)
        await ctx.send(f"```I Will Remind You In {time} {mode}```")
        await asyncio.sleep(int(time * 3600))
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(
            title="Wrong, Example : '!remind 2 s'", color=0x0061ff)
        await ctx.send(embed=embed)


#########################CHRISTMAS EVENT#########################################################################################################################################################################################################################
@client.command()
@commands.is_owner()
async def christmas(ctx):
    for guild in client.guilds:
        for channel in guild.channels:
            if guild.name == "kar1mHub":
                karim = '<@616680119079272551>'
                kimo = '<@518386469421842443>'
                ateya = '<@756638375032914060>'
                await client.get_channel(756047602197463170).send(
                    f"Happy New Year @everyone and of course my boss and creator {karim} and of course i didn't forget my two friends {kimo} and his bot {ateya} ! 2010"
                )
            if guild.name == "Kodik's Editing Server":
                kodiks = '<@767285497344294912>'
                partofmycomp = '<@768696688143368213>'
                await client.get_channel(782209236222214148).send(
                    f"Happy New Year @everyone and of course my two supporters and friends {kodiks} and {partofmycomp}! 2010"
                )
            if guild.name == "the ninja's group":
                ninja = '<@423935646550458410>'
                await client.get_channel(722488124386705537).send(
                    f"Happy New Year @everyone and of course my man who gave me a my nickname (Juice WRLD) {ninja}! 2010"
                )
            break


##########################################################################################################################################################################################
# @client.event
# async def on_command_error(ctx,error):
#     embed = discord.Embed(title='Need Help Using Me ?',
#                     color=0xFFA07A,
#                     url='https://marawan-pablo-help.notkar1myt.repl.co',
#                     description='this command was not found')
#     embed.set_thumbnail(url=client.user.avatar_url)
#     await ctx.send(embed=embed)
#     await ctx.message.add_reaction('❌')


# Load command to manage our "Cogs" or extensions
@client.command()
async def load(ctx, extension):
    # Check if the user running the command is actually the owner of the bot
    if ctx.author.id == OWNERID:
        client.load_extension(f'Cogs.{extension}')
        await ctx.send(f"Enabled the Cog!")
    else:
        await ctx.send(f"You are not cool enough to use this command")


# Unload command to manage our "Cogs" or extensions
@client.command()
async def unload(ctx, extension):
    # Check if the user running the command is actually the owner of the bot
    if ctx.author.id == OWNERID:
        client.unload_extension(f'Cogs.{extension}')
        await ctx.send(f"Disabled the Cog!")
    else:
        await ctx.send(f"You are not cool enough to use this command")


# @client.command(aliases=['trans'])
# async def translate(ctx, fromm, to, *, text):
#     try:
#         translator= Translator(from_lang=fromm,to_lang=to)
#         translation = translator.translate(text)
#         embed = discord.Embed(title="Translation",
#             description=f'Translation: {translation}\n\nMy Creator also created a translator : https://translator.notkar1myt.repl.co/')
#         await ctx.send(embed=embed)
#     except:
#         await ctx.send("Make Sure The Two Languages Are Spelled Correctly (example : !translate english french my text here)\nMy Creator also created a translator : https://translator.notkar1myt.repl.co/")
  
@client.command()
async def ly(ctx, song:str, artist:str):
    genius = lyricsgenius.Genius("K2MVdGHG5avZZA5Ax7gtZxlGLKl1Y21Pnx8RGItkfER9zVwaSisYipJ_fKOMgrgd")
    artistt = genius.search_artist(artist, max_songs=0, sort="title")
    song = genius.search_song(f"{song}", artistt.name)
    # query = f"{song} by {artistt} lyrics"
    # for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
    embed = discord.Embed(title=f'{song} By {artistt}',
            description=f"{song.lyrics[0:1800]}")
    await ctx.send(embed=embed)

# Reload command to manage our "Cogs" or extensions
@client.command(name="reload")
async def reload_(ctx, extension):
    # Check if the user running the command is actually the owner of the bot
    if ctx.author.id == OWNERID:
        client.reload_extension(f'Cogs.{extension}')
        await ctx.send(f"Reloaded the Cog!")
    else:
        await ctx.send(f"You are not cool enough to use this command")


# Automatically load all the .py files in the Cogs folder
for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        # try:
        client.load_extension(f'Cogs.{filename[:-3]}')
        # except Exception:
        #     raise Exception

keep_alive()




client.run('NzcwNjY1OTI4NTAwOTY5NTAy.X5g4kw.qrmFuvwlgeCpZV3J1xPE8fJXo0E')
