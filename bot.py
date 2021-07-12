# for discord functionality

import discord
from discord.ext import commands, tasks
import asyncio

# for weather updates
import pyowm

# reddit
import praw
import apraw

import math
import random
from itertools import cycle
from random import randint

#
from datetime import datetime, date, timedelta
import pytz
import time
import sched

# role assignment
from discord.ext.commands import Bot
import discord
from discord.utils import get


# pagination
import DiscordUtils

# Secret stuff
import os
import dotenv
dotenv.load_dotenv(override=True)

# Bias Match Image manipulation
from PIL import Image


# set the random seed to system time
random.seed()

# Bot prefix
client = commands.Bot(command_prefix = '.',help_command=None)

# Token

my_discord_token = os.getenv("MY_DISCORD_API_KEY")

@client.event
async def on_ready():
    try:
        print('Bot is ready.')
        print('We have logged in as {0.user}'.format(client))
    except Exception as e:
        print(str(e))



# Events that get triggered

@client.event
async def on_raw_reaction_add(payload):
    global role
    message_id = payload.message_id
    if message_id == int(os.getenv("SAD_ROLES_MESSAGE_ID")):
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if payload.emoji.name == os.getenv("SAD_EMOTE_1"):
            role = discord.utils.get(guild.roles, name=os.getenv("SAD_ROLE_1"))
        elif payload.emoji.name == os.getenv("SAD_EMOTE_2"):
            role = discord.utils.get(guild.roles, name=os.getenv("SAD_ROLE_2"))

        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

            if member is not None:
                await member.add_roles(role)
            else:
                print("member not found")
        else:
            print("role not found")

# Sadboiclique
@client.event
async def on_raw_reaction_remove(payload):
    global role
    sadboi_message_id = payload.message_id
    if sadboi_message_id == int(os.getenv("SAD_ROLES_MESSAGE_ID")):
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if payload.emoji.name == os.getenv("SAD_EMOTE_1"):
            role = discord.utils.get(guild.roles, name=os.getenv("SAD_ROLE_1"))
        elif payload.emoji.name == os.getenv("SAD_EMOTE_2"):
            role = discord.utils.get(guild.roles, name=os.getenv("SAD_ROLE_2"))


        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)

            if member is not None:
                await member.remove_roles(role)
            else:
                print("member not found")
        else:
            print("role not found")

@client.event
async def on_message(message):

    coolWords5 = ["Pong", "pong", "PONG"]
    coolWords6 = ["dice"]
    coolWords7 = ["8ball"]
    coolWords8 = ["Question:", "Compatibility:"]
    coolWords9 = ["hug", ".cheerup "]
    coolWords10 = [".match"]

    for word in coolWords5:
        if message.content.count(word) > 0:
            emoji = '🏓'
            await message.add_reaction(emoji)


    for word in coolWords8:
        if message.content.count(word) > 0:
            emoji = '✅'
            emoji2 = '❌'
            await message.add_reaction(emoji)
            await message.add_reaction(emoji2)

    if message.channel.id == int(os.getenv("kpop_roles_channel_id")):
        await asyncio.sleep(2)
        await message.channel.purge(limit=1)

    if message.author == client.user:
        return

    if message.content.startswith(".format") or message.content.startswith(".f"):

        try:
            embeds = message.embeds
            await message.channel.purge(limit=1)
            firstIteration = True
            for embed in embeds:
                if firstIteration:
                    UTC = pytz.utc
                    timeZ = pytz.timezone('Asia/Seoul')
                    dt_K = datetime.now(timeZ)
                    utc_K = dt_K.astimezone(UTC)
                    finaldate = utc_K.strftime("%y%m%d")
                    await message.channel.send(f"```css\n{finaldate} Twitter Update - {embed.to_dict()['author']['name']}```")
                    await message.channel.send(embed.to_dict()['description'])
                    firstIteration = False

                if 'image' in embed.to_dict():
                    await message.channel.send(embed.to_dict()['image']['url'])

        except Exception as e:
            await message.channel.send("an error occurred...")

    for word in coolWords6:
        if message.content.count(word) > 0:
            emoji = '🎲'
            await message.add_reaction(emoji)

    for word in coolWords7:
        if message.content.count(word) > 0:
            emoji = '🎱'
            await message.add_reaction(emoji)

    for word in coolWords9:
        if message.content.count(word) > 0:
            emoji = '🤗'
            await message.add_reaction(emoji)

    for word in coolWords10:
        if message.content.count(word) > 0:
            emoji = '😍'
            await message.add_reaction(emoji)

    await client.process_commands(message)

start_time = time.time()
@client.command(pass_context=True,help="gets uptime of bot")
async def uptime(ctx):
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(timedelta(seconds=difference))
        embed = discord.Embed(colour=0xc8dc6c)
        embed.add_field(name="Uptime", value=text)
        embed.set_footer(text="Juicy Peach Apricot")
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send("Current uptime: " + text)


# adding roles in kpop planet discord server
@client.command(pass_context=True,aliases=['+'])
async def addmain(ctx, *, role_name_request):
    restricted_roles = os.getenv("kpop_nonaddable_roles").split(",")
    for index in range(len(restricted_roles)):
        restricted_roles[index] = int(restricted_roles[index].strip())
    final_role = None
    member = ctx.message.author
    for main_role in member.guild.roles:
        if main_role.id not in restricted_roles:
            if role_name_request.lower() == str(main_role).lower():
                final_role = discord.utils.get(member.guild.roles, name=str(main_role))

    if final_role is not None:
        if final_role in member.roles:
            embed = discord.Embed(colour=0xc8dc6c)
            text = f"{ctx.author.mention} you already have the `{str(final_role)}` role..."
            embed.add_field(name="Unsuccessful", value=text)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(colour=0xc8dc6c)
            text = f"{ctx.author.mention} you added the `{str(final_role)}` role"
            embed.add_field(name="Success", value=text)
            await ctx.send(embed=embed)
            await member.add_roles(final_role)
    else:
        embed = discord.Embed(colour=0xc8dc6c)
        text = f"{ctx.author.mention} the role: `{role_name_request}` was not found... "
        embed.add_field(name="Unsuccessful", value=text)
        await ctx.send(embed=embed)

@client.command(pass_context=True,aliases=['-'])
async def removemain(ctx, *, role_name_request):
    restricted_roles = os.getenv("kpop_nonaddable_roles").split(",")
    for index in range(len(restricted_roles)):
        restricted_roles[index] = int(restricted_roles[index].strip())
    final_role = None
    member = ctx.message.author
    for main_role in member.guild.roles:
        if main_role.id not in restricted_roles:

            if role_name_request.lower() == str(main_role).lower():

                final_role = discord.utils.get(member.guild.roles, name=str(main_role))

    if final_role is not None:
        if final_role in member.roles:
            embed = discord.Embed(colour=0xc8dc6c)
            text = f"{ctx.author.mention} you removed the `{str(final_role)}` role"
            embed.add_field(name="Success", value=text)
            await ctx.send(embed=embed)
            await member.remove_roles(final_role)
        else:
            embed = discord.Embed(colour=0xc8dc6c)
            text = f"{ctx.author.mention} the role `{str(final_role)}` is not one of your current roles..."
            embed.add_field(name="Unsuccessful", value=text)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(colour=0xc8dc6c)
        text = f"{ctx.author.mention} the role: `{role_name_request}` was not found... "
        embed.add_field(name="Unsuccessful", value=text)
        await ctx.send(embed=embed)


# Commands
@client.command(help="create welcome page")
async def welcomepage(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send('>>> Hello\n\nType **.commands** for the list of all commands\nFeel free to make suggestions in <#666041759008030761>\nGet your roles in <#721370113189609654>\n\nhttps://thumbs.gfycat.com/PhonySelfishArrowana.webp')


@client.command(help="create roles page")
async def rolespage(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send('>>> React with  <:sujeongconcernyoinked:674901390405140501>  if you want Kpop updates\nReact with  <:suyunpout:708254305202995221>  if you want a surprise\nUn-react the appropriate emoji if you do not want that certain role anymore\n\nOtherwise DM <@487187111045234692> if you want your own custom-made role or the role you want if the bot is offline')


@client.command(help="Displays a list of all commands")
async def commands(ctx):
    await ctx.send(">>> Please check your DMs for the list of all commands :relaxed:")
    await ctx.author.send(
        '```css\nGeneral Commands:\n\n.8ball {your_question} - Ask the bot a question\n\n.cheerup - Try this one if you are feeling down\n\n.conway - A Conway Game of Life Simulator\n\n.dice {number}- Rolls {number} sided die\n\n.format {twitter link with embed} - Retrieves images/gif of twitter embed and returns the date it was posted on\n\n.hug {@person} - Try this one on someone. This will only work if you ping the user you want to hug\n\n.isonline - Check whether the bot is online\n\n.match {person1 and person2} - Ship yourself with your crush (For example, type .match Me and Sojin)\n\n.randomgroup - get a music video from a random K-Pop group\n\n.piglatin {your message} - Convert your message to Pig Latin\n\n.ping - Checks latency\n\n.stanloona {your message} - Convert your message to let others know you really stan LOOΠΔ\n\n.timer {time in minutes} {role to ping} - Set a timer for yourself (in minutes). You can optionally provide an extra argument if you want to ping a role after the timer ends\n\n.weather {city or country} - Get the current weather in the location you have specified\n\n.uptime - Retrieves the uptime of the bot\n\nGame Commands:\n\n.biasmatch - Starts up a new multiplayer game of Bias Match\n\n.idolguess commands - Displays the Guess the Idol Game commands```')


@client.command(help="Checks Latency")
async def ping(ctx):
    embed = discord.Embed(colour=0xc8dc6c)
    text = f"Latency: {round(client.latency * 1000)} ms"
    embed.add_field(name="Pong!", value=text)
    await ctx.send(embed=embed)


@client.command(help="Try this one on someone. This will only work if you ping the user you want to hug")
async def hug(ctx, member: discord.Member):
    embed = discord.Embed(colour=0xc8dc6c)
    title = f"Hugging {member}"
    text = f"OwO (>^.^)> (っ´∀｀)っ (っ⇀⑃↼)っ {member} ⊂(・﹏・⊂) ლ(･ω･*ლ) <(^.^<) OwO"
    embed.add_field(name=title, value=text)
    await ctx.send(embed=embed)


@hug.error
async def hug_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.BadArgument):
        embed = discord.Embed(colour=0xc8dc6c)
        title = "Unsuccessful"
        text = 'User not found **OR** "@" is missing at the start. Please try again...'
        embed.add_field(name=title, value=text)
        await ctx.send(embed=embed)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.BadArgument):
        embed = discord.Embed(colour=0xc8dc6c)
        title = "Unsuccessful"
        text = 'Enter the appropriate arguments. Please try again...'
        embed.add_field(name=title, value=text)
        await ctx.send(embed=embed)


@client.command(help="Ask it a question (Will not work if no arguments are entered)", aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['yes lol.',
                 'ugh maybe.',
                 'definitely not.',
                 'try again later.',
                 'not sure lmao.',
                 'you should ask Ginger',
                 'I should not tell you now',
                 'I do not think you should know',
                 'Definitely',
                 'Outlook good',
                 "Don't count on it",
                 "I'm afraid not",
                 'Try googling that one lol',
                 'Ha HAaaAAAaaaAA',
                 'Are you kidding me? Of course!',
                 'Are you kidding me? Of course not!']
    embed = discord.Embed(colour=0xc8dc6c)
    title = f"{question}?"
    text = f'{random.choice(responses)}'
    embed.add_field(name=title, value=text)
    await ctx.send(embed=embed)


@client.command(
    help="Ship yourself with your crush (For example, type .match Me and Sojin")
async def match(ctx, *, question):
    embed = discord.Embed(colour=0xc8dc6c)
    title = f"Shipping {question}..."
    text = f'Compatibility: {randint(0, 100)}%'
    embed.add_field(name=title, value=text)
    await ctx.send(embed=embed)


@client.command(help="Rolls die")
async def dice(ctx, *, number):
    try:
        realnumber = int(number.strip())
        embed = discord.Embed(colour=0xc8dc6c)
        title = f"Rolls Game Die"
        text = f'{randint(1, realnumber)}'
        embed.add_field(name=title, value=text)
        await ctx.send(embed=embed)
    except Exception as e:
        embed = discord.Embed(colour=0xc8dc6c)
        title = f"Error"
        text = f'You must enter one whole number only greater than 0'
        embed.add_field(name=title, value=text)
        await ctx.send(embed=embed)


@client.command(help="Convert your message to let others know you really stan LOONA", aliases=['sl'])
async def stanloona(ctx, *, arg):
    temp = arg.split()
    big_message = ""
    for thing in temp:
        med_message = " Stan " + thing + " Loona "
        big_message = big_message + med_message
    embed = discord.Embed(colour=0xc8dc6c)
    title = f"STAN LOONA"
    text = f'{big_message}'
    embed.add_field(name=title, value=text)
    await ctx.send(embed=embed)


@client.command(help="Convert your message to Pig Latin", aliases=['pl'])
async def piglatin(ctx, *, arg):
    temp = arg.split()
    big_message = ""
    for thing in temp:
        med_message = thing[-1] + thing[:-1] + "e"
        big_message = big_message + " " + med_message + " "
    embed = discord.Embed(colour=0xc8dc6c)
    title = f"Pig Latin Message"
    text = f'{big_message}'
    embed.add_field(name=title, value=text)
    await ctx.send(embed=embed)

@client.command(help="retrieves all idols in the database", aliases=['aib'])
async def allidolsbackup(ctx):
    image_list = os.listdir("./photos")
    image_list.sort(key=lambda x: x.lower())
    await ctx.send(len(image_list))
    for idols in image_list:
        finalArrayForm = idols.split(',')
        finalGroup = finalArrayForm[0].strip()
        finalArrayForm[len(finalArrayForm) - 1] = finalArrayForm[len(finalArrayForm) - 1][
                                                  0:len(finalArrayForm[len(finalArrayForm) - 1]) - 4].strip()
        finalName = finalArrayForm[1].strip()

        await ctx.send(f"{finalGroup} {finalName}")


@client.command(help="retrieves all idols in the database", aliases=['ai'])
async def allidols(ctx):
    embedsList = []
    idolGroups = []
    idolNames = []


    image_list = os.listdir("./photos")
    image_list.sort(key=lambda x: x.lower())

    for idols in image_list:
        finalArrayForm = idols.split(',')
        finalGroup = finalArrayForm[0].strip()
        finalArrayForm[len(finalArrayForm) - 1] = finalArrayForm[len(finalArrayForm) - 1][
                                                  0:len(finalArrayForm[len(finalArrayForm) - 1]) - 4].strip()
        finalName = finalArrayForm[1].strip()

        idolNames.append(finalName)
        idolGroups.append(finalGroup)

    finalIdolNames = ''
    refreshCount = []
    currentIdolGroup = ''

    for namesIndex in range(len(image_list)):

        if namesIndex == len(idolNames) - 1:
            finalIdolNames = finalIdolNames + f", {idolNames[namesIndex]}"
            embed = discord.Embed(title="All Idols",colour=0xc8dc6c).add_field(name=f"Total Idols: {len(image_list)} | Total Groups: {len(set(idolGroups))}", value=f"\n{finalIdolNames}", inline=False)
            embedsList.append(embed)
        elif currentIdolGroup != idolGroups[namesIndex]:

            if len(refreshCount) == 10:

                embed = discord.Embed(title="All Idols", colour=0xc8dc6c).add_field(
                    name=f"Total Idols: {len(image_list)} | Total Groups: {len(set(idolGroups))}", value=f"\n{finalIdolNames}", inline=False)
                embedsList.append(embed)
                refreshCount.clear()
                currentIdolGroup = idolGroups[namesIndex]
                finalIdolNames = f"\n\n__**{idolGroups[namesIndex]}**__\n{idolNames[namesIndex]}"

            else:

                currentIdolGroup = idolGroups[namesIndex]
                finalIdolNames = finalIdolNames + f"\n\n__**{idolGroups[namesIndex]}**__\n{idolNames[namesIndex]}"

            refreshCount.append(0)

        else:
            finalIdolNames = finalIdolNames + f", {idolNames[namesIndex]}"




    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)

    paginator.add_reaction('⏮️', "first")
    paginator.add_reaction('⏪', "back")
    paginator.add_reaction('🔐', "lock")
    paginator.add_reaction('⏩', "next")
    paginator.add_reaction('⏭️', "last")

    await paginator.run(embedsList)


rgCounter = 0
videoStopIndex = 0
rgPointer = []
indexArray = []
Items = []
with open("videos.txt", "r") as f:
    for item in f:
        indexArray.append(rgCounter)
        rgCounter = rgCounter + 1

        itemArray = item.split(",")
        Items.append(itemArray)

    random.shuffle(Items)
    videoStopIndex = rgCounter

@client.command(help="posts a video from a random K-Pop group", aliases=['rg'])
async def randomgroup(ctx):

    embed = discord.Embed(colour=0xc8dc6c)
    title = Items[len(rgPointer)][2]
    text = f'Artist: {Items[len(rgPointer)][1]}'
    embed.add_field(name=title, value=text)
    await ctx.send(embed=embed)
    await ctx.send(Items[len(rgPointer)][0])

    rgPointer.append(0)

    if len(rgPointer) == videoStopIndex:

        rgPointer.clear()
        random.shuffle(Items)



online_counter = [0]


@client.command(help="Find out whether the bot is online or not", aliases=['io'])
async def isonline(ctx):
    await client.wait_until_ready()

    interval = 3
    embed = discord.Embed(title="Is the Bot Online", description=f'If the emoji is changing approximately every 3 to 6 seconds, the bot is online',
                          colour=0xc8dc6c)

    m0 = await ctx.send(embed=embed)

    await asyncio.sleep(interval)
    while not client.is_closed():
        country_time_zone = pytz.timezone('NZ')
        country_time = datetime.now(country_time_zone)
        final_message_date = country_time.strftime("%B %#d %Y at %H:%M:%S")
        await asyncio.sleep(interval)
        emojis = [":rabbit:",":cat:",":dove:",":frog:",":deer:",":owl:",":fish:",":bat:",":swan:",":penguin:",":butterfly:",":wolf:"]
        final_choice = random.choice(emojis)
        final_choice2 = random.choice(emojis)
        final_choice3 = random.choice(emojis)
        final_choice4 = random.choice(emojis)
        final_choice5 = random.choice(emojis)
        embednew = discord.Embed(title="Is the Bot Online",
                              description=f'Look at these animals :relaxed:\n\n{final_choice} {final_choice2} {final_choice3} {final_choice4} {final_choice5}',
                              colour=0xc8dc6c)
        await m0.edit(embed=embednew)
        online_counter.append(0)
        if len(online_counter) == 5:
            await asyncio.sleep(interval)
            embedlast = discord.Embed(title="Is the Bot Online",description=f"Bot is online :relaxed:. Last updated on {final_message_date} NZT",colour=0xc8dc6c)
            await m0.edit(embed=embedlast)
            online_counter.clear()
            return


timer_players = []
@client.command(help="Set a timer for yourself (in minutes) and ping a role if you want to after the time has elapsed", aliases=['t'])
async def timer(ctx, *, minutes):

    try:
        temp = minutes.split()
        finalminutes = temp[0]
        if len(temp) > 2:
            embedtemp = discord.Embed(colour=0xc8dc6c)
            titletemp = "Error"
            texttemp = f"You may only pass 1 or 2 arguments for this command"
            embedtemp.add_field(name=titletemp, value=texttemp)
            await ctx.send(embed=embedtemp)
            return

        for people in timer_players:
            if people == ctx.author.mention:
                embedtemp = discord.Embed(colour=0xc8dc6c)
                titletemp = "Error"
                texttemp = f"You already have a timer elapsing"
                embedtemp.add_field(name=titletemp, value=texttemp)
                await ctx.send(embed=embedtemp)
                return

        if float(finalminutes) <= 0:
            embednew = discord.Embed(title="Error",
                                     description=f'Negative numbers and zero are not allowed',
                                     colour=0xc8dc6c)
            await ctx.send(embed=embednew)
            return
        timer_players.append(ctx.author.mention)
        if float(finalminutes).is_integer() and int(finalminutes) == 1 :
            description = f'You will be notified in {finalminutes} minute'
        else:
            description = f'You will be notified in {finalminutes} minutes'
        embednew = discord.Embed(title=f"{ctx.author}: Your timer has started",
                                 description=description,
                                 colour=0xc8dc6c)
        await ctx.send(embed=embednew)
        await asyncio.sleep(int(60 * float(finalminutes)))
        for people in timer_players:
            if people == ctx.author.mention:
                timer_players.remove(people)
        embedlast = discord.Embed(title=f"{ctx.author}: Your timer has ended",
                                 description=f'You may start a new timer',
                                 colour=0xc8dc6c)
        if len(temp) == 2:
            await ctx.send(temp[1])
        await ctx.author.send(embed=embedlast)
    except ValueError:
        embednew = discord.Embed(title="Error",
                                 description=f'You must enter a number or your number cannot end with a 0',
                                 colour=0xc8dc6c)
        await ctx.send(embed=embednew)
        for people in timer_players:
            if people == ctx.author.mention:
                timer_players.remove(people)

cheerup_players = []
slides = [0]

@client.command(help="Try this one if you are feeling down")
async def cheerup(ctx):
    for people in cheerup_players:
        if people == ctx.author.mention:
            embedtemp = discord.Embed(colour=0xc8dc6c)
            titletemp = "Slideshow in Progress"
            texttemp = f"Please wait until your current slideshow has finished"
            embedtemp.add_field(name=titletemp, value=texttemp)
            await ctx.send(embed=embedtemp)
            return
    cheerup_players.append(ctx.author.mention)
    image_list = os.listdir("./photos")
    counterNumber = len(image_list)
    theIndex = randint(0, counterNumber - 1)
    finalFromData = str(image_list[theIndex])
    finalArrayForm = finalFromData.split(',')
    finalGroup = finalArrayForm[0].strip()
    finalArrayForm[len(finalArrayForm) - 1] = finalArrayForm[len(finalArrayForm) - 1][
                                              0:len(finalArrayForm[len(finalArrayForm) - 1]) - 4].strip()
    finalName = finalArrayForm[1].strip()

    cheers = [f'{finalGroup} {finalName} hopes you are having a nice day today! :relaxed:',
              f'Best wishes :smiling_face_with_3_hearts:\nfrom {finalGroup} {finalName}',
              f'{finalGroup} {finalName} believes in you! :grinning:',
              f'{finalGroup} {finalName} says to not give up even though you feel like giving up! :smiley:',
              f'The only thing {finalGroup} {finalName} hopes for you is that you are happy and having fun! :smile:',
              f'{finalGroup} {finalName} is proud of your achievements! :grin:',
              f'{finalGroup} {finalName} says "Stay positive!" :blush:',
              f'{finalGroup} {finalName} says "keep working on your goals!" :innocent:',
              f'{finalGroup} {finalName} is rooting for you! :slight_smile:',
              f'{finalGroup} {finalName} is counting on you! :relieved:',
              f'{finalGroup} {finalName} knows you can make it through the hard times :heart_eyes:',
              f'{finalGroup} {finalName} says they will be here to talk if need be! :kissing_heart:',
              f'{finalGroup} {finalName} tells you to work hard now so you will have no regrets in the future :kissing:',
              f'{finalGroup} {finalName} wants you to smile! :kissing_smiling_eyes:',
              f'{finalGroup} {finalName} wants you to relax after a very stressful day! :kissing_closed_eyes:',
              f'{finalGroup} {finalName} wants you to relax because you deserve it from working hard all day! :heart_eyes_cat:',
              f'{finalGroup} {finalName} will never give up on you! :clap:',
              f'{finalGroup} {finalName} will always be your best friend! :handshake:',
              f'{finalGroup} {finalName} will never stop believing in you :grinning:',
              f'{finalGroup} {finalName} always has your back :punch:',
              f'{finalGroup} {finalName} is here to remind you that you tried your best :star_struck:',
              f'{finalGroup} {finalName} is here to make you laugh :stuck_out_tongue:',
              f'{finalGroup} {finalName} wants you to work hard so you can be happier in the future! :partying_face:',
              f'{finalGroup} {finalName} believes you can achieve anything you put your effort in :grinning:',
              f'{finalGroup} {finalName} wants you to eat well! :ramen:',
              f'{finalGroup} {finalName} wants you to sleep well! :sleeping_accommodation:',
              f'{finalGroup} {finalName} wants you to stay warm from the cold weather! :fire:',
              f'{finalGroup} {finalName} wants to see you soon! :airplane:',
              f'{finalGroup} {finalName} is here to remind you of the good times! :fireworks:',
              f'{finalGroup} {finalName} knows good times are coming for a good person like you! :chart_with_upwards_trend:']

    embed = discord.Embed(title="Cheer Up!",description=f'{random.choice(cheers)}',colour=0xc8dc6c)
    file = discord.File(("photos/"+ str(finalFromData)),filename="image.jpg")
    embed.set_image(url="attachment://image.jpg")
    await ctx.send(file=file,embed=embed)

    interval = 5
    await asyncio.sleep(interval)
    while not client.is_closed():

        image_list = os.listdir("./photos")
        counterNumber = len(image_list)
        theIndex = randint(0, counterNumber - 1)
        finalFromData = str(image_list[theIndex])
        finalArrayForm = finalFromData.split(',')
        finalGroup = finalArrayForm[0].strip()
        finalArrayForm[len(finalArrayForm) - 1] = finalArrayForm[len(finalArrayForm) - 1][
                                                  0:len(finalArrayForm[len(finalArrayForm) - 1]) - 4].strip()
        finalName = finalArrayForm[1].strip()

        cheers = [f'{finalGroup} {finalName} hopes you are having a nice day today! :relaxed:',
                  f'Best wishes :smiling_face_with_3_hearts:\nfrom {finalGroup} {finalName}',
                  f'{finalGroup} {finalName} believes in you! :grinning:',
                  f'{finalGroup} {finalName} says to not give up even though you feel like giving up! :smiley:',
                  f'The only thing {finalGroup} {finalName} hopes for you is that you are happy and having fun! :smile:',
                  f'{finalGroup} {finalName} is proud of your achievements! :grin:',
                  f'{finalGroup} {finalName} says "Stay positive!" :blush:',
                  f'{finalGroup} {finalName} says "keep working on your goals!" :innocent:',
                  f'{finalGroup} {finalName} is rooting for you! :slight_smile:',
                  f'{finalGroup} {finalName} is counting on you! :relieved:',
                  f'{finalGroup} {finalName} knows you can make it through the hard times :heart_eyes:',
                  f'{finalGroup} {finalName} says they will be here to talk if need be! :kissing_heart:',
                  f'{finalGroup} {finalName} tells you to work hard now so you will have no regrets in the future :kissing:',
                  f'{finalGroup} {finalName} wants you to smile! :kissing_smiling_eyes:',
                  f'{finalGroup} {finalName} wants you to relax after a very stressful day! :kissing_closed_eyes:',
                  f'{finalGroup} {finalName} wants you to relax because you deserve it from working hard all day! :heart_eyes_cat:',
                  f'{finalGroup} {finalName} will never give up on you! :clap:',
                  f'{finalGroup} {finalName} will always be your best friend! :handshake:',
                  f'{finalGroup} {finalName} will never stop believing in you :grinning:',
                  f'{finalGroup} {finalName} always has your back :punch:',
                  f'{finalGroup} {finalName} is here to remind you that you tried your best :star_struck:',
                  f'{finalGroup} {finalName} is here to make you laugh :stuck_out_tongue:',
                  f'{finalGroup} {finalName} wants you to work hard so you can be happier in the future! :partying_face:',
                  f'{finalGroup} {finalName} believes you can achieve anything you put your effort in :grinning:',
                  f'{finalGroup} {finalName} wants you to eat well! :ramen:',
                  f'{finalGroup} {finalName} wants you to sleep well! :sleeping_accommodation:',
                  f'{finalGroup} {finalName} wants you to stay warm from the cold weather! :fire:',
                  f'{finalGroup} {finalName} wants to see you soon! :airplane:',
                  f'{finalGroup} {finalName} is here to remind you of the good times! :fireworks:',
                  f'{finalGroup} {finalName} knows good times are coming for a good person like you! :chart_with_upwards_trend:']

        embed = discord.Embed(title="Cheer Up!", description=f'{random.choice(cheers)}', colour=0xc8dc6c)
        file = discord.File(("photos/" + str(finalFromData)), filename="image.jpg")
        embed.set_image(url="attachment://image.jpg")
        await ctx.send(file=file, embed=embed)
        await asyncio.sleep(interval)
        slides.append(0)
        if len(slides) == 10:
            embed = discord.Embed(colour=0xc8dc6c)
            title = "Slideshow Finished"
            text = f" You may start a new slideshow {ctx.author.mention}"
            embed.add_field(name=title, value=text)
            await ctx.send(embed=embed)
            slides.clear()
            for people in cheerup_players:
                if people == ctx.author.mention:
                    cheerup_players.remove(people)

            return

conway_players = []

@client.command(help="A Conway Game of Life Simulator")
async def conway(ctx):
    for people in conway_players:
        if people == ctx.author.mention:
            embedtemp = discord.Embed(colour=0xc8dc6c)
            titletemp = "Error"
            texttemp = f"You already have a simulation going on"
            embedtemp.add_field(name=titletemp, value=texttemp)
            await ctx.send(embed=embedtemp)
            return
    conway_players.append(ctx.author.mention)
    s = ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', '\n', 'w',
         'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', '\n', 'w', 'w',
         'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', '\n', 'w', 'w', 'w',
         'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', '\n', 'w', 'w', 'w', 'w',
         'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', '\n', 'w', 'w', 'w', 'w', 'w',
         'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', '\n', 'w', 'w', 'w', 'w', 'w', 'w',
         'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', '\n', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
         'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', '\n', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
         'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', '\n', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w',
         'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', '\n', ]

    some_count = []
    for item in s:

        if item == '\n':

            some_count.append(0)

        elif randint(0, 1) == 1:

            s[len(some_count)] = "░"
            some_count.append(0)


        else:

            s[len(some_count)] = "▓"
            some_count.append(0)

    some_count.clear()

    final_display = "".join(s)



    generation = [0]


    embed = discord.Embed(title="Game of Life",colour=0xc8dc6c)
    title = f'Generation: {len(generation)}'
    text = f"{final_display}"
    embed.add_field(name=title, value=text)
    m0 = await ctx.send(embed=embed)
    await asyncio.sleep(2)

    IsOver = [0]
    while len(IsOver) == 1:
        t = list(final_display)
        final_next = list(final_display)
        some_count = []
        blank_count = []
        for item in t:

            if item == '\n':

                some_count.append(0)

            elif item == "░":
                temp_count = []

                if len(some_count) - 1 >= 0 and t[len(some_count) - 1] == "░" and t[len(some_count) - 1] != '\n':
                    temp_count.append(0)
                if len(some_count) - 21 >= 0 and t[len(some_count) - 21] == "░" and t[len(some_count) - 21] != '\n':
                    temp_count.append(0)
                if len(some_count) - 22 >= 0 and t[len(some_count) - 22] == "░" and t[len(some_count) - 22] != '\n':
                    temp_count.append(0)
                if len(some_count) - 20 >= 0 and t[len(some_count) - 20] == "░" and t[len(some_count) - 20] != '\n':
                    temp_count.append(0)
                if len(some_count) + 1 <= 209 and t[len(some_count) + 1] == "░" and t[len(some_count) + 1] != '\n':
                    temp_count.append(0)
                if len(some_count) + 21 <= 209 and t[len(some_count) + 21] == "░" and t[len(some_count) + 21] != '\n':
                    temp_count.append(0)
                if len(some_count) + 22 <= 209 and t[len(some_count) + 22] == "░" and t[len(some_count) + 22] != '\n':
                    temp_count.append(0)
                if len(some_count) + 20 <= 209 and t[len(some_count) + 20] == "░" and t[len(some_count) + 20] != '\n':
                    temp_count.append(0)

                if len(temp_count) == 2:
                    final_next[len(some_count)] = "░"
                    temp_count.clear()
                    some_count.append(0)
                elif len(temp_count) == 3:
                    final_next[len(some_count)] = "░"
                    temp_count.clear()
                    some_count.append(0)
                else:
                    final_next[len(some_count)] = "▓"
                    temp_count.clear()
                    blank_count.append(0)
                    some_count.append(0)



            elif item == "▓":
                temp_count = []

                if len(some_count) - 1 >= 0 and t[len(some_count) - 1] == "░" and t[len(some_count) - 1] != '\n':
                    temp_count.append(0)
                if len(some_count) - 21 >= 0 and t[len(some_count) - 21] == "░" and t[len(some_count) - 21] != '\n':
                    temp_count.append(0)
                if len(some_count) - 22 >= 0 and t[len(some_count) - 22] == "░" and t[len(some_count) - 22] != '\n':
                    temp_count.append(0)
                if len(some_count) - 20 >= 0 and t[len(some_count) - 20] == "░" and t[len(some_count) - 20] != '\n':
                    temp_count.append(0)
                if len(some_count) + 1 <= 209 and t[len(some_count) + 1] == "░" and t[len(some_count) + 1] != '\n':
                    temp_count.append(0)
                if len(some_count) + 21 <= 209 and t[len(some_count) + 21] == "░" and t[len(some_count) + 21] != '\n':
                    temp_count.append(0)
                if len(some_count) + 22 <= 209 and t[len(some_count) + 22] == "░" and t[len(some_count) + 22] != '\n':
                    temp_count.append(0)
                if len(some_count) + 20 <= 209 and t[len(some_count) + 20] == "░" and t[len(some_count) + 20] != '\n':
                    temp_count.append(0)

                if len(temp_count) == 3:
                    final_next[len(some_count)] = "░"
                    temp_count.clear()
                    some_count.append(0)

                else:
                    final_next[len(some_count)] = "▓"
                    temp_count.clear()
                    blank_count.append(0)
                    some_count.append(0)

        final_next_display = "".join(final_next)

        generation.append(0)

        embed = discord.Embed(title="Game of Life", colour=0xc8dc6c)
        title = f'Generation: {len(generation)}'
        text = f"{final_display}"
        embed.add_field(name=title, value=text)
        await m0.edit(embed=embed)
        await asyncio.sleep(2)

        if len(generation) == 100:
            generation.clear()
            IsOver.pop(0)
            embed = discord.Embed( colour=0xc8dc6c)
            title = f'Stopping at Generation 100'
            text = f"You may start a new simulation {ctx.author.mention}"
            embed.add_field(name=title, value=text)
            await ctx.send(embed=embed)
            some_count.clear()
            blank_count.clear()
            for people in conway_players:
                if people == ctx.author.mention:
                    conway_players.remove(people)

            return

        if len(blank_count) == 200:
            generation.clear()
            IsOver.pop(0)
            embed = discord.Embed(colour=0xc8dc6c)
            title = f'No More Cells Remaining'
            text = f"You may start a new simulation {ctx.author.mention}"
            embed.add_field(name=title, value=text)
            await ctx.send(embed=embed)
            some_count.clear()
            blank_count.clear()
            for people in conway_players:
                if people == ctx.author.mention:
                    conway_players.remove(people)

            return

        some_count.clear()
        blank_count.clear()

        final_display = final_next_display

        await asyncio.sleep(2)


@client.command(help="Get a current update of the weather of the city specified",aliases=['w'])
async def weather(ctx,*,city: str):

    try:
        owm = pyowm.OWM(os.getenv("OWM_API_KEY"))
        mgr = owm.weather_manager()
        try:
            obs = mgr.weather_at_place(city)
        except Exception as e:
            embed2 = discord.Embed(colour=0xc8dc6c)
            title2 = f"Error"
            text2 = f"{str(e)}"
            embed2.add_field(name=title2, value=text2)
            await ctx.send(embed=embed2)
            return
        w = obs.weather
        detailed_desc = w.detailed_status
        temperature = w.temperature('celsius')
        cloud_coverage = w.clouds
        wind = w.wind()
        humidity = w.humidity

        wind_direction = ""
        if wind["deg"] >=345 or wind["deg"] <= 15:
            wind_direction = 'East'
        elif wind["deg"] > 15 and wind["deg"] < 75:
            wind_direction = 'North-East'
        elif wind["deg"] >= 75 and wind["deg"] <= 105:
            wind_direction = 'North'
        elif wind["deg"] > 105 and wind["deg"] < 165:
            wind_direction = 'North-West'
        elif wind["deg"] >= 165 and wind["deg"] <= 195:
            wind_direction = 'West'
        elif wind["deg"] > 195 and wind["deg"] < 255:
            wind_direction = 'South-West'
        elif wind["deg"] >= 255 and wind["deg"] <= 285:
            wind_direction = 'South'
        elif wind["deg"] > 285 and wind["deg"] < 345:
            wind_direction = 'South-East'

        bigtitle = f"Weather Forecast in {city.capitalize()}"
        embed = discord.Embed(title=bigtitle,colour=0xc8dc6c)
        title = f"Observation"
        text = f"{detailed_desc.capitalize()}"
        title2 = "Wind Speed"
        text2 = f'{round(wind["speed"] * 1.6)} kilometres/hour {wind_direction} (@ {wind["deg"]}°)'
        title3 = "Current Temperature"
        text3 = f'{round(temperature["temp"])}°C, Maximum: {round(temperature["temp_max"])}°C, Minimum: {round(temperature["temp_min"])}°C'
        title4 = f"Humidity"
        text4 = f"{humidity}% humid with {cloud_coverage}% cloud coverage"
        embed.add_field(name=title, value=text)
        embed.add_field(name=title2, value=text2)
        embed.add_field(name=title3, value=text3)
        embed.add_field(name=title4, value=text4)
        await ctx.send(embed=embed)
    except Exception as e:
        embed2 = discord.Embed(colour=0xc8dc6c)
        title2 = f"Error"
        text2 = f"{str(e)}"
        embed2.add_field(name=title2, value=text2)
        await ctx.send(embed=embed2)

# Bias Match


server_players = []
@client.command(help="Play a multiplayer game of Bias Match", aliases=['bm'])
async def biasmatch(ctx):
    idol_players = os.listdir("./photos")
    random.shuffle(idol_players)
    game_selection = []
    for index in range(32):
        game_selection.append(idol_players[index])
    pre_selection = []
    current_pointer = []


    if ctx.guild.id not in server_players:
        server_players.append(ctx.guild.id)

        while ctx.guild.id in server_players:

            finalFromData = str(game_selection[len(current_pointer)])
            finalArrayForm = finalFromData.split(',')
            finalGroup = finalArrayForm[0].strip()
            finalName = finalArrayForm[1].strip()
            if finalName.lower().endswith(".jpg"):
                finalName = finalName[0:len(finalName) - 4]

            finalFromData2 = str(game_selection[len(current_pointer) + 1])
            finalArrayForm2 = finalFromData2.split(',')
            finalGroup2 = finalArrayForm2[0].strip()
            finalName2 = finalArrayForm2[1].strip()
            if finalName2.lower().endswith(".jpg"):
                finalName2 = finalName2[0:len(finalName2) - 4]

            image1 = Image.open("photos/" + str(finalFromData))


            image2 = Image.open("photos/" + str(finalFromData2))


            image1 = image1.resize((500, 600))
            image2 = image2.resize((525, 600))

            image1_size = image1.size
            image2_size = image2.size

            new_image = Image.new('RGB', ( image1_size[0] + image2_size[0] , image1_size[1]), (250, 250, 250))


            new_image.paste(image1, (0, 0))

            new_image.paste(image2, (image1_size[0], 0))

            new_image.save("merged_image.jpg", "JPEG")

            final_title = "Choose the idol to move on to the next round"

            if len(game_selection) == 2:
                final_title = "Choose the winner of the final round"

            embed = discord.Embed(title=final_title, description=f'{finalGroup} {finalName} vs {finalGroup2} {finalName2}', colour=0xc8dc6c)

            file = discord.File(("merged_image.jpg"), filename="image.jpg")
            embed.set_image(url="attachment://image.jpg")
            msg = await ctx.send(file=file, embed=embed)


            await msg.add_reaction("⬅")
            await msg.add_reaction("➡")


            await asyncio.sleep(8)


            nmsg = await ctx.channel.fetch_message(msg.id)

            #count reactions
            reaction = discord.utils.get(nmsg.reactions, emoji="⬅")
            reaction2 = discord.utils.get(nmsg.reactions, emoji="➡")

            if reaction.count > reaction2.count:

                pre_selection.append(game_selection[len(current_pointer)])
                await nmsg.add_reaction('⏪')

            elif reaction2.count > reaction.count:

                pre_selection.append(game_selection[len(current_pointer) + 1])
                await nmsg.add_reaction('⏩')

            elif reaction.count == reaction2.count:
                finalNo = randint(1, 2)

                if finalNo == 1:
                    await nmsg.add_reaction('⏪')

                    pre_selection.append(game_selection[len(current_pointer)])


                else:
                    await nmsg.add_reaction('⏩')
                    pre_selection.append(game_selection[len(current_pointer) + 1] )


            if len(game_selection) - 1 == len(current_pointer) + 1:

                game_selection.clear()
                for entry in pre_selection:
                    game_selection.append(entry)

                pre_selection.clear()
                current_pointer.clear()

            else:

                current_pointer.append(0)
                current_pointer.append(0)

            await asyncio.sleep(2)
            await nmsg.delete()



            if len(game_selection) == 1:
                finalFromData = str(game_selection[0])
                finalArrayForm = finalFromData.split(',')
                finalGroup = finalArrayForm[0].strip()
                finalName = finalArrayForm[1].strip()
                if finalName.lower().endswith(".jpg"):
                    finalName = finalName[0:len(finalName) - 4]

                embed = discord.Embed(title="The winner is...",
                                      description=f'__**{finalGroup} {finalName}**__',
                                      colour=0xc8dc6c)
                file = discord.File(("photos/" + str(finalFromData)), filename="image.jpg")
                embed.set_image(url="attachment://image.jpg")
                await ctx.send(file=file, embed=embed)

                server_players.remove(ctx.guild.id)
    else:
        embedsecond = discord.Embed(colour=0xc8dc6c)
        titlesecond = f"Sorry"
        textsecond = f"There is a Bias Match session currently running in this server"
        embedsecond.add_field(name=titlesecond, value=textsecond)
        await ctx.send(embed=embedsecond)

# Idol Guess

# Initialising Variables for Idol Guess

theFinalGroup = []
theFinalNames = []
theFinalPhoto = []
hasStarted = []
longScore = []

@client.command(help="Type '.idolguess commands' for more information about how to play Idol Guess", aliases=['ig'])
async def idolguess(ctx, *, guess):
    if guess == 'commands':
        await ctx.send(
            "```css\n\n.idolguess start - Starts the game\n\n.idolguess {the name of the person} - Make your guess (For example, type .idolguess sojin)\n\n.idolguess skip - Skips the current idol you have to guess at the cost of one life\n\n.idolguess quit - Quits the whole game overall\n\n.allidols - Retrieve all the idols in the database```")
    elif guess == 'start' and len(hasStarted) == 0:
        hasStarted.append(0)

        image_list = os.listdir("./photos")
        counterNumber = len(image_list)
        theIndex = randint(0, counterNumber - 1)
        finalFromData = str(image_list[theIndex])
        finalArrayForm = finalFromData.split(',')
        finalArrayForm[len(finalArrayForm) - 1] = finalArrayForm[len(finalArrayForm) - 1][0:len(finalArrayForm[len(finalArrayForm) - 1]) - 4].strip()
        theFinalGroup.append(finalArrayForm[0].strip())

        finalArrayForm.pop(0)
        for item in finalArrayForm:
            theFinalNames.append(item)


        embed = discord.Embed(title="Who is this?", description=f'Lives remaining: {4 - len(hasStarted)}', colour=0xc8dc6c)
        file = discord.File(("photos/" + str(finalFromData)), filename="image.jpg")
        embed.set_image(url="attachment://image.jpg")
        await ctx.send(file=file, embed=embed)
        await asyncio.sleep(30)

    elif guess.lower() in (name.lower().strip() for name in theFinalNames) and len(hasStarted) != 0:

        theFinalNames.clear()
        theFinalGroup.clear()
        theFinalPhoto.clear()
        longScore.append(0)

        image_list = os.listdir("./photos")
        counterNumber = len(image_list)
        theIndex = randint(0, counterNumber - 1)
        finalFromData = str(image_list[theIndex])
        finalArrayForm = finalFromData.split(',')
        finalArrayForm[len(finalArrayForm) - 1] = finalArrayForm[len(finalArrayForm) - 1][0:len(finalArrayForm[len(finalArrayForm) - 1]) - 4].strip()
        theFinalGroup.append(finalArrayForm[0].strip())

        finalArrayForm.pop(0)
        for item in finalArrayForm:
            theFinalNames.append(item)

        embedfirst = discord.Embed(colour=0xc8dc6c)
        titlefirst = f"You are Correct!"
        textfirst = f"Well done!"
        embedfirst.add_field(name=titlefirst, value=textfirst)
        await ctx.send(embed=embedfirst)

        embed = discord.Embed(title="Who is this?", description=f'Lives remaining: {4 - len(hasStarted)}',
                              colour=0xc8dc6c)
        file = discord.File(("photos/" + str(finalFromData)), filename="image.jpg")
        embed.set_image(url="attachment://image.jpg")
        await ctx.send(file=file, embed=embed)

    elif ((guess.lower() not in (name.lower().strip() for name in theFinalNames) ) or (guess.lower() == 'skip')) and len(
            hasStarted) != 0 and guess.lower() != 'quit' and guess.lower() != 'start':
        hasStarted.append(0)

        embedsecond = discord.Embed(colour=0xc8dc6c)
        titlesecond = f"Sorry"
        textsecond = f"The answer was {theFinalNames[0]} from {theFinalGroup[0]}"
        embedsecond.add_field(name=titlesecond, value=textsecond)
        await ctx.send(embed=embedsecond)

        if len(hasStarted) == 4:


            embedthird = discord.Embed(title="You Have Lost",colour=0xc8dc6c)
            titlethird = f"Final Score"
            textthird = f"{len(longScore)}"
            embedthird.add_field(name=titlethird, value=textthird)
            await ctx.send(embed=embedthird)
            theFinalNames.clear()
            theFinalGroup.clear()
            theFinalPhoto.clear()
            hasStarted.clear()
            longScore.clear()
            return

        theFinalNames.clear()
        theFinalGroup.clear()
        theFinalPhoto.clear()

        image_list = os.listdir("./photos")
        counterNumber = len(image_list)
        theIndex = randint(0, counterNumber - 1)
        finalFromData = str(image_list[theIndex])
        finalArrayForm = finalFromData.split(',')
        finalArrayForm[len(finalArrayForm) - 1] = finalArrayForm[len(finalArrayForm) - 1][
                                                  0:len(finalArrayForm[len(finalArrayForm) - 1]) - 4].strip()
        theFinalGroup.append(finalArrayForm[0].strip())

        finalArrayForm.pop(0)
        for item in finalArrayForm:
            theFinalNames.append(item)

        embed = discord.Embed(title="Who is this?", description=f'Lives remaining: {4 - len(hasStarted)}',
                              colour=0xc8dc6c)
        file = discord.File(("photos/" + str(finalFromData)), filename="image.jpg")
        embed.set_image(url="attachment://image.jpg")
        await ctx.send(file=file, embed=embed)

    elif guess.lower() == 'quit':

        embedsecond = discord.Embed(colour=0xc8dc6c)
        titlesecond = f"Sorry"
        textsecond = f"The answer was {theFinalNames[0]} from {theFinalGroup[0]}"
        embedsecond.add_field(name=titlesecond, value=textsecond)
        await ctx.send(embed=embedsecond)

        embedthird = discord.Embed(title="You Have Lost", colour=0xc8dc6c)
        titlethird = f"Final Score"
        textthird = f"{len(longScore)}"
        embedthird.add_field(name=titlethird, value=textthird)
        await ctx.send(embed=embedthird)

        theFinalNames.clear()
        theFinalGroup.clear()
        theFinalPhoto.clear()
        hasStarted.clear()
        longScore.clear()

    else:
        embedzero = discord.Embed(colour=0xc8dc6c)
        titlezero = f"Sorry"
        textzero = f"That command is invalid for now"
        embedzero.add_field(name=titlezero, value=textzero)
        await ctx.send(embed=embedzero)

@tasks.loop(seconds = 21600)
async def reddit_updates():
    await client.wait_until_ready()


    channel = client.get_channel(int(os.getenv("kpop_news_channel_id")))
    reddit = apraw.Reddit(client_id=os.getenv("reddit_client_id"), client_secret=os.getenv("reddit_client_secret"),
                          username=os.getenv("reddit_username"), password=os.getenv("reddit_password"),
                          user_agent=os.getenv("reddit_user_agent"))

    subreddit = await reddit.subreddit('kpop')


    try:

        async for post in subreddit.hot(limit=10):

            embed = discord.Embed(title="New Update", colour=0xc8dc6c)
            title = f'{post.title}'
            embed.add_field(name=title, value="See post below")
            await channel.send(embed=embed)
            await channel.send(f'>>> {post.url}')


    except Exception as e:
        embed = discord.Embed(colour=0xc8dc6c)
        title = f'An Error Occured'
        text = str(e)
        embed.add_field(name=title, value=text)
        channel = client.get_channel(int(os.getenv("error_stream_channel_id")))
        await channel.send(embed=embed)

@tasks.loop(seconds = 86400)
async def idolpost_updates():
    await client.wait_until_ready()
    channel = client.get_channel(int(os.getenv("idolpost_channel_id")))


    image_list = os.listdir("./photos")
    counterNumber = len(image_list)
    theIndex = randint(0, counterNumber - 1)
    finalFromData = str(image_list[theIndex])
    finalArrayForm = finalFromData.split(',')
    finalGroup = finalArrayForm[0].strip()
    finalArrayForm[len(finalArrayForm) - 1] = finalArrayForm[len(finalArrayForm) - 1][
                                                  0:len(finalArrayForm[len(finalArrayForm) - 1]) - 4].strip()
    finalName = finalArrayForm[1].strip()

    embed = discord.Embed(title="Idol of the Day", description=f'{finalGroup} {finalName}', colour=0xc8dc6c)
    file = discord.File(("photos/" + str(finalFromData)), filename="image.jpg")
    embed.set_image(url="attachment://image.jpg")
    await channel.send(file=file, embed=embed)


reddit_updates.start()
idolpost_updates.start()

client.run(my_discord_token)

