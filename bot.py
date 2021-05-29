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
import sys
import os
import dotenv
dotenv.load_dotenv(override=True)

# date and time outside of current country
import dateutil.parser

# Bot prefix
client = commands.Bot(command_prefix = '.',help_command=None)

# Token

my_discord_token = os.getenv("MY_DISCORD_API_KEY")

# For the bot's status
cycleMessages = os.getenv("BOT_CYCLE_MESSAGES")
longCycle = cycleMessages.split(",")
for i in range(0,len(longCycle)):
    longCycle[i] = longCycle[i] + os.getenv("BOT_CYCLE_SUFFIX")

status = cycle(longCycle)
@client.event
async def on_ready():
    try:
        change_status.start()
        # await client.change_presence(status=discord.Status.online, activity=discord.Game('Always Be Your Girl (너의 소녀가 되어줄게)'))
        print('Bot is ready.')
        print('We have logged in as {0.user}'.format(client))
    except Exception as e:
        print(str(e))


@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


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
    final_role = None
    member = ctx.message.author
    for main_role in member.guild.roles:
        if main_role.id != 689772319362646127 and main_role.id != 689775233325989918 and main_role.id != 745263173518491690 and main_role.id != 691190515043008564 and main_role.id != 700910886612893807:
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
    final_role = None
    member = ctx.message.author
    for main_role in member.guild.roles:
        if main_role.id != 689772319362646127 and main_role.id != 689775233325989918 and main_role.id != 745263173518491690 and main_role.id != 691190515043008564 and main_role.id != 700910886612893807:

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
        '```css\nGeneral Commands:\n\n.8ball {your_question} - Ask the bot a question\n\n.cheerup - Try this one if you are feeling down\n\n.conway - A Conway Game of Life Simulator\n\n.dice {number}- Rolls {number} sided die\n\n.format {twitter link with embed} - Retrieves images/gif of twitter embed and returns the date it was posted on\n\n.hug {@person} - Try this one on someone. This will only work if you ping the user you want to hug\n\n.isonline - Check whether the bot is online\n\n.match {person1 and person2} - Ship yourself with your crush (For example, type .match Me and Sojin)\n\n.randomgroup - get a music video from a random K-Pop group\n\n.piglatin {your message} - Convert your message to Pig Latin\n\n.ping - Checks latency\n\n.stanloona {your message} - Convert your message to let others know you really stan LOOΠΔ\n\n.timer {time in minutes} {role to ping} - Set a timer for yourself (in minutes). You can optionally provide an extra argument if you want to ping a role after the timer ends\n\n.weather {city or country} - Get the current weather in the location you have specified\n\n.uptime - Retrieves the uptime of the bot\n\nGame Commands:\n\n.idolguess commands - Displays the Guess the Idol Game commands\n\n.avalon commands - Displays the Avalon commands```')


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
    currentIdolGroup = idolGroups[0]
    for namesIndex in range(0,len(image_list)):

        if currentIdolGroup != idolGroups[namesIndex] or namesIndex == len(idolNames) - 1:
            embed = discord.Embed(colour=0xc8dc6c).add_field(name=currentIdolGroup, value=finalIdolNames)
            currentIdolGroup = idolGroups[namesIndex]
            embedsList.append(embed)
            finalIdolNames = idolNames[namesIndex] + "\n"

        else:
            finalIdolNames = finalIdolNames + idolNames[namesIndex] + "\n"


    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
    paginator.add_reaction('⏮️', "first")
    paginator.add_reaction('⏪', "back")
    paginator.add_reaction('🔐', "lock")
    paginator.add_reaction('⏩', "next")
    paginator.add_reaction('⏭️', "last")
    await paginator.run(embedsList)

@client.command(help="posts a video from a random K-Pop group", aliases=['rg'])
async def randomgroup(ctx):
    randomVideos = []
    theirTitle = []
    theGroup = []
    with open("videos.txt", "r") as f:
        for item in f:
            itemArray = item.split()
            randomVideos.append(itemArray[0])
            itemArray.pop(0)
            finalText = ''
            for word in itemArray:
                finalText = finalText + word + " "
            finalTextArray = finalText.split(",")
            theGroup.append(finalTextArray[0].strip())
            theirTitle.append(finalTextArray[1].strip())

    finalIndex = randint(0,len(randomVideos)-1)

    embed = discord.Embed(colour=0xc8dc6c)
    title = theirTitle[finalIndex]
    text = f'Artist: {theGroup[finalIndex]}'
    embed.add_field(name=title, value=text)
    await ctx.send(embed=embed)
    await ctx.send(randomVideos[finalIndex])


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

# Avalon
rounds_array = [ [2,3,2,3,3] , [2,3,4,3,4], [2,3,3,4,4] , [3,4,4,5,5], [3,4,4,5,5],[3,4,4,5,5]]
hammer_number = []
hammer_number.append(int(os.getenv("HAMMER_NUMBER")))
avalon_roles5 = ['Loyal', 'Percival', 'Merlin','Morgana', 'Assassin']
avalon_roles6 = ['Loyal', 'Loyal', 'Percival', 'Merlin', 'Morgana', 'Assassin']
avalon_roles7 = ['Loyal', 'Loyal', 'Percival', 'Merlin', 'Morgana', 'Assassin', 'Mordred']
avalon_roles8 = ['Loyal', 'Loyal', 'Loyal', 'Percival', 'Merlin', 'Morgana', 'Assassin', 'Mordred']
avalon_roles9 = ['Loyal', 'Loyal', 'Loyal', 'Loyal','Percival', 'Merlin', 'Morgana', 'Assassin', 'Mordred']
avalon_roles10 = ['Loyal', 'Loyal', 'Loyal', 'Loyal', 'Percival', 'Merlin', 'Morgana', 'Assassin','Mordred','Lackey']


game_phase = []
avalon_players_mention = []
avalon_players = []
good_people = []
bad_people = []
fail_votes = []
final_merlin = []
mission_participants = []
yes_no_already_voted = []
has_voted = []
pass_votes = []
score_array = []
yes_votes = []
no_votes = []

current_chooser_index = []
current_chooser = []
hammer_owner_index = []
hammer_owner = []
lady_owner_index = []
lady_owner = []
lady_use = []
turns_done = []
hammer_time = []

@client.command(help="Type '.avalon commands' for more information about how to play Avalon", aliases=['av'])
async def avalon(ctx, *, command):
    global long_message
    if command.lower() == 'commands':
        await ctx.send(f">>> {ctx.author.mention} Please check your DMs for the list of all the Avalon commands :relaxed:")
        await ctx.author.send(
            '```css\n\n.avalon join - join game\n\n.avalon leave - leave game\n\n.avalon start - start game\n\n.avalon reset - resets game\n\n.avalon mission {@person1 @person2 @person3....} - send the mission team to do their mission\n\n.avalon yes - accepts the current mission proposal\n\n.avalon no - declines the current mission proposal\n\n.avalon vote pass - passes the mission if you are doing the mission\n\n.avalon vote fail - fails the mission if you are doing the mission\n\n.avalon lady {@person} - checks the role of the person\n\n.avalon merlin {@person} - guess who the merlin is when the good people have passed three missions\n\n\n\n```')
    elif command.lower() == "join":
        if len(game_phase) <= 0:
            for name in avalon_players_mention:
                if name == ctx.author.mention:
                    await ctx.send(f'>>> {ctx.author.mention}, you have already joined matchmaking... ')
                    return

            if len(avalon_players_mention) == 10:
                await ctx.send(f">>> Sorry. Ten people is the maximum number of players for Avalon")
                return

            avalon_players_mention.append(ctx.author.mention)
            avalon_players.append(ctx.author)
            current_players = len(avalon_players_mention)

            await ctx.send(
                f'>>> You have joined the game {ctx.author.mention}\n\nCurrent number of players: {current_players} ')

        elif len(game_phase) > 0:
            await ctx.send(f">>> Game has already started. Wait for the next game")
            return

    elif command.lower() == 'leave':
        if len(game_phase) <= 0:
            for name in avalon_players_mention:
                if name == ctx.author.mention:
                    avalon_players_mention.remove(name)
                    await ctx.send(f'>>> You have left Avalon matchmaking {ctx.author.mention} ')
                    return
            await ctx.send(f'>>> You have not joined Avalon matchmaking yet {ctx.author.mention}')

        elif len(game_phase) > 0:
            await ctx.send(">>> You can not leave the game once it has started")

    elif command.lower() == 'start':
        if len(game_phase) == 0:

            if len(avalon_players_mention) < 5:
                await ctx.send(f">>> Sorry {ctx.author.mention}, Avalon needs at least five players :cry:")
                return
            elif len(avalon_players_mention) >= 5:

                current_chooser_index.append(randint(0, (len(avalon_players_mention) - 1) ) )
                current_chooser.append(avalon_players_mention[current_chooser_index[0]])

                lady_owner_index.append(randint(0, (len(avalon_players_mention) - 1)))
                lady_owner.append(avalon_players_mention[lady_owner_index[0]])

                hammer_owner_index.append( (current_chooser_index[0] + 5 ) % len(avalon_players_mention) )
                hammer_owner.append(avalon_players_mention[hammer_owner_index[0]])

                game_phase.append(0)
                await ctx.send(f">>> The game of Avalon has begun")

                count_for_index_printing = 0
                main_board = ""
                for person in avalon_players_mention:
                    main_board = main_board + f"{count_for_index_printing}: {person}\n"
                    count_for_index_printing = count_for_index_printing + 1

                await ctx.send(f">>> Round: {len(score_array) + 1}\n\nCurrent Players:\n\n{main_board}\n\nIt is now {current_chooser[0]}'s turn.\n\nPlease nominate {rounds_array[len(avalon_players_mention) - 5 ][len(score_array)]} people to participate in the mission. You can nominate yourself.\n\nThe Hammer lands on {hammer_owner[0]}. There is { (hammer_number[0] - len(turns_done) )  } turns left before they have full control of the proposal of the mission\n\n{lady_owner[0]} has the lady of the lake. You can use this at the start of the third round\n\nUnsure about the commands? Type  **.avalon commands** to find out")


                if len(avalon_players_mention) == 5:

                    random.shuffle(avalon_roles5)
                    random.shuffle(avalon_roles5)
                    random.shuffle(avalon_roles5)
                    random.shuffle(avalon_roles5)
                    random.shuffle(avalon_roles5)

                    the_merlin_index = avalon_roles5.index("Merlin")

                    the_merlin = avalon_players_mention[the_merlin_index]

                    the_morgana_index = avalon_roles5.index("Morgana")

                    the_morgana = avalon_players_mention[the_morgana_index]

                    the_assassin_index = avalon_roles5.index("Assassin")

                    the_assassin = avalon_players_mention[the_assassin_index]

                    merlinmorganaArray = [the_merlin, the_morgana]
                    final_merlin.append(the_merlin)

                    the_index_zero = avalon_players_mention.index(merlinmorganaArray[0])

                    the_index_one = avalon_players_mention.index(merlinmorganaArray[1])

                    random.shuffle(merlinmorganaArray)
                    random.shuffle(merlinmorganaArray)
                    random.shuffle(merlinmorganaArray)
                    random.shuffle(merlinmorganaArray)
                    random.shuffle(merlinmorganaArray)

                    for avalon_player in avalon_players:
                        their_index = avalon_players_mention.index(avalon_player.mention)
                        their_role = avalon_roles5[their_index]

                        await avalon_player.send(
                            f'>>> The roles are\n\nGood:\nLoyal\nPercival\nMerlin\n\nBad:\nMorgana\nAssassin')

                        if their_role == 'Loyal':
                            good_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**Nothing else**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Percival':
                            good_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**One of {merlinmorganaArray[0]} (Index Number: {the_index_zero}) and {merlinmorganaArray[1]} (Index Number: {the_index_one}) is the Merlin, the other is the Morgana**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Merlin':
                            good_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**The bad people are:\n{the_morgana} (Index Number: {the_morgana_index})\n{the_assassin} (Index Number: {the_assassin_index})**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Morgana':
                            bad_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad person is:\n{the_assassin} (Index Number: {the_assassin_index}) who is the Assassin**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Assassin':
                            bad_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad person is:\n{the_morgana} (Index Number: {the_morgana_index}) who is the Morgana**\n\nPlease also note your index number which is **{their_index}**'
                        await avalon_player.send(f'>>> {long_message}')

                elif len(avalon_players_mention) == 6:

                    random.shuffle(avalon_roles6)
                    random.shuffle(avalon_roles6)
                    random.shuffle(avalon_roles6)
                    random.shuffle(avalon_roles6)
                    random.shuffle(avalon_roles6)

                    the_merlin_index = avalon_roles6.index("Merlin")

                    the_merlin = avalon_players_mention[the_merlin_index]

                    the_morgana_index = avalon_roles6.index("Morgana")

                    the_morgana = avalon_players_mention[the_morgana_index]

                    the_assassin_index = avalon_roles6.index("Assassin")

                    the_assassin = avalon_players_mention[the_assassin_index]

                    merlinmorganaArray = [the_merlin, the_morgana]
                    final_merlin.append(the_merlin)

                    the_index_zero = avalon_players_mention.index(merlinmorganaArray[0])

                    the_index_one = avalon_players_mention.index(merlinmorganaArray[1])

                    random.shuffle(merlinmorganaArray)
                    random.shuffle(merlinmorganaArray)
                    random.shuffle(merlinmorganaArray)
                    random.shuffle(merlinmorganaArray)
                    random.shuffle(merlinmorganaArray)

                    for avalon_player in avalon_players:
                        their_index = avalon_players_mention.index(avalon_player.mention)
                        their_role = avalon_roles6[their_index]

                        await avalon_player.send(
                            f'>>> The roles are\n\nGood:\nLoyal\nLoyal\nPercival\nMerlin\n\nBad:\nMorgana\nAssassin')

                        if their_role == 'Loyal':
                            good_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**Nothing else**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Percival':
                            good_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**One of {merlinmorganaArray[0]} (Index Number: {the_index_zero}) and {merlinmorganaArray[1]} (Index Number: {the_index_one}) is the Merlin, the other is the Morgana**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Merlin':
                            good_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**The bad people are:\n{the_morgana} (Index Number: {the_morgana_index})\n{the_assassin} (Index Number: {the_assassin_index})**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Morgana':
                            bad_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad person is:\n{the_assassin} (Index Number: {the_assassin_index}) who is the Assassin**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Assassin':
                            bad_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad person is:\n{the_morgana} (Index Number: {the_morgana_index}) who is the Morgana**\n\nPlease also note your index number which is **{their_index}**'

                        await avalon_player.send(f'>>> {long_message}')

                elif len(avalon_players_mention) == 7:

                    avalon_roles = ['Loyal', 'Loyal', 'Percival', 'Merlin', 'Morgana', 'Assassin', 'Mordred']

                    random.shuffle(avalon_roles7)
                    random.shuffle(avalon_roles7)
                    random.shuffle(avalon_roles7)
                    random.shuffle(avalon_roles7)
                    random.shuffle(avalon_roles7)

                    the_merlin_index = avalon_roles7.index("Merlin")

                    the_merlin = avalon_players_mention[the_merlin_index]

                    the_morgana_index = avalon_roles7.index("Morgana")

                    the_morgana = avalon_players_mention[the_morgana_index]

                    the_assassin_index = avalon_roles7.index("Assassin")

                    the_assassin = avalon_players_mention[the_assassin_index]

                    the_mordred_index = avalon_roles7.index("Mordred")

                    the_mordred = avalon_players_mention[the_mordred_index]

                    merlinmorganaArray = [the_merlin, the_morgana]
                    final_merlin.append(the_merlin)

                    the_index_zero = avalon_players_mention.index(merlinmorganaArray[0])

                    the_index_one = avalon_players_mention.index(merlinmorganaArray[1])

                    random.shuffle(merlinmorganaArray)
                    random.shuffle(merlinmorganaArray)
                    random.shuffle(merlinmorganaArray)
                    random.shuffle(merlinmorganaArray)
                    random.shuffle(merlinmorganaArray)

                    for avalon_player in avalon_players:
                        their_index = avalon_players_mention.index(avalon_player.mention)
                        their_role = avalon_roles7[their_index]

                        await avalon_player.send(
                        f'>>> The roles are\n\nGood:\nLoyal\nLoyal\nPercival\nMerlin\n\nBad:\nMorgana\nAssassin\nMordred')

                        if their_role == 'Loyal':
                            good_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**Nothing else**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Percival':
                            good_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**One of {merlinmorganaArray[0]} (Index Number: {the_index_zero}) and {merlinmorganaArray[1]} (Index Number: {the_index_one}) is the Merlin, the other is the Morgana**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Merlin':
                            good_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**Some of the bad people are:\n{the_morgana} (Index Number: {the_morgana_index})\n{the_assassin} (Index Number: {the_assassin_index})\nThere is another bad person called the Mordred but you do not know who they are**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Morgana':
                            bad_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_assassin} (Index Number: {the_assassin_index}) who is the Assassin\n{the_mordred} (Index Number: {the_mordred_index}) who is the Mordred**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Assassin':
                            bad_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_morgana} (Index Number: {the_morgana_index}) who is the Morgana\n{the_mordred} (Index Number: {the_mordred_index}) who is the Mordred**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Mordred':
                            bad_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_morgana} (Index Number: {the_morgana_index}) who is the Morgana\n{the_assassin} (Index Number: {the_assassin_index}) who is the Assassin**\n\nPlease also note your index number which is **{their_index}**'
                        await avalon_player.send(f'>>> {long_message}')

                elif len(avalon_players_mention) == 8:

                    avalon_roles = ['Loyal', 'Loyal', 'Loyal', 'Percival', 'Merlin', 'Morgana', 'Assassin', 'Mordred']

                    random.shuffle(avalon_roles8)
                    random.shuffle(avalon_roles8)
                    random.shuffle(avalon_roles8)
                    random.shuffle(avalon_roles8)
                    random.shuffle(avalon_roles8)

                    the_merlin_index = avalon_roles8.index("Merlin")

                    the_merlin = avalon_players_mention[the_merlin_index]

                    the_morgana_index = avalon_roles8.index("Morgana")

                    the_morgana = avalon_players_mention[the_morgana_index]

                    the_assassin_index = avalon_roles8.index("Assassin")

                    the_assassin = avalon_players_mention[the_assassin_index]

                    the_mordred_index = avalon_roles8.index("Mordred")

                    the_mordred = avalon_players_mention[the_mordred_index]

                    merlinmorganaArray = [the_merlin, the_morgana]
                    final_merlin.append(the_merlin)

                    the_index_zero = avalon_players_mention.index(merlinmorganaArray[0])

                    the_index_one = avalon_players_mention.index(merlinmorganaArray[1])

                    random.shuffle(merlinmorganaArray)
                    random.shuffle(merlinmorganaArray)
                    random.shuffle(merlinmorganaArray)
                    random.shuffle(merlinmorganaArray)
                    random.shuffle(merlinmorganaArray)

                    for avalon_player in avalon_players:
                        their_index = avalon_players_mention.index(avalon_player.mention)
                        their_role = avalon_roles8[their_index]

                        await avalon_player.send(
                            f'>>> The roles are\n\nGood:\nLoyal\nLoyal\nLoyal\nPercival\nMerlin\n\nBad:\nMorgana\nAssassin\nMordred')

                        if their_role == 'Loyal':
                            good_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**Nothing else**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Percival':
                            good_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**One of {merlinmorganaArray[0]} (Index Number: {the_index_zero}) and {merlinmorganaArray[1]} (Index Number: {the_index_one}) is the Merlin, the other is the Morgana**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Merlin':
                            good_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**Some of the bad people are:\n{the_morgana} (Index Number: {the_morgana_index})\n{the_assassin} (Index Number: {the_assassin_index})\nThere is another bad person called the Mordred but you do not know who they are**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Morgana':
                            bad_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_assassin} (Index Number: {the_assassin_index}) who is the Assassin\n{the_mordred} (Index Number: {the_mordred_index}) who is the Mordred**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Assassin':
                            bad_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_morgana} (Index Number: {the_morgana_index}) who is the Morgana\n{the_mordred} (Index Number: {the_mordred_index}) who is the Mordred**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Mordred':
                            bad_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_morgana} (Index Number: {the_morgana_index}) who is the Morgana\n{the_assassin} (Index Number: {the_assassin_index}) who is the Assassin**\n\nPlease also note your index number which is **{their_index}**'
                        await avalon_player.send(f'>>> {long_message}')

                elif len(avalon_players_mention) == 9:

                    avalon_roles = ['Loyal', 'Loyal', 'Loyal', 'Loyal', 'Percival', 'Merlin', 'Morgana', 'Assassin',
                                    'Mordred']

                    random.shuffle(avalon_roles9)
                    random.shuffle(avalon_roles9)
                    random.shuffle(avalon_roles9)
                    random.shuffle(avalon_roles9)
                    random.shuffle(avalon_roles9)



                    the_merlin_index = avalon_roles9.index("Merlin")

                    the_merlin = avalon_players_mention[the_merlin_index]

                    the_morgana_index = avalon_roles9.index("Morgana")

                    the_morgana = avalon_players_mention[the_morgana_index]

                    the_assassin_index = avalon_roles9.index("Assassin")

                    the_assassin = avalon_players_mention[the_assassin_index]

                    the_mordred_index = avalon_roles9.index("Mordred")

                    the_mordred = avalon_players_mention[the_mordred_index]

                    merlinmorganaArray = [the_merlin, the_morgana]
                    final_merlin.append(the_merlin)

                    the_index_zero = avalon_players_mention.index(merlinmorganaArray[0])

                    the_index_one = avalon_players_mention.index(merlinmorganaArray[1])

                    random.shuffle(merlinmorganaArray)
                    random.shuffle(merlinmorganaArray)
                    random.shuffle(merlinmorganaArray)
                    random.shuffle(merlinmorganaArray)
                    random.shuffle(merlinmorganaArray)

                    for avalon_player in avalon_players:
                        their_index = avalon_players_mention.index(avalon_player.mention)
                        their_role = avalon_roles9[their_index]

                        await avalon_player.send(
                            f'>>> The roles are\n\nGood:\nLoyal\nLoyal\nLoyal\nLoyal\nPercival\nMerlin\n\nBad:\nMorgana\nAssassin\nMordred')

                        if their_role == 'Loyal':
                            good_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**Nothing else**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Percival':
                            good_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**One of {merlinmorganaArray[0]} (Index Number: {the_index_zero}) and {merlinmorganaArray[1]} (Index Number: {the_index_one}) is the Merlin, the other is the Morgana**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Merlin':
                            good_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**Some of the bad people are:\n{the_morgana} (Index Number: {the_morgana_index})\n{the_assassin} (Index Number: {the_assassin_index})\nThere is another bad person called the Mordred but you do not know who they are**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Morgana':
                            bad_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_assassin} (Index Number: {the_assassin_index}) who is the Assassin\n{the_mordred} (Index Number: {the_mordred_index}) who is the Mordred**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Assassin':
                            bad_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_morgana} (Index Number: {the_morgana_index}) who is the Morgana\n{the_mordred} (Index Number: {the_mordred_index}) who is the Mordred**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Mordred':
                            bad_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_morgana} (Index Number: {the_morgana_index}) who is the Morgana\n{the_assassin} (Index Number: {the_assassin_index}) who is the Assassin**\n\nPlease also note your index number which is **{their_index}**'
                        await avalon_player.send(f'>>> {long_message}')

                elif len(avalon_players_mention) == 10:

                    avalon_roles = ['Loyal', 'Loyal', 'Loyal', 'Loyal', 'Percival', 'Merlin', 'Morgana', 'Assassin',
                                    'Mordred', 'Lackey']


                    random.shuffle(avalon_roles10)
                    random.shuffle(avalon_roles10)
                    random.shuffle(avalon_roles10)
                    random.shuffle(avalon_roles10)
                    random.shuffle(avalon_roles10)

                    the_merlin_index = avalon_roles10.index("Merlin")

                    the_merlin = avalon_players_mention[the_merlin_index]

                    the_morgana_index = avalon_roles10.index("Morgana")

                    the_morgana = avalon_players_mention[the_morgana_index]

                    the_assassin_index = avalon_roles10.index("Assassin")

                    the_assassin = avalon_players_mention[the_assassin_index]

                    the_mordred_index = avalon_roles10.index("Mordred")

                    the_mordred = avalon_players_mention[the_mordred_index]

                    the_lackey_index = avalon_roles10.index("Lackey")

                    the_lackey = avalon_players_mention[the_lackey_index]

                    merlinmorganaArray = [the_merlin, the_morgana]
                    final_merlin.append(the_merlin)

                    the_index_zero = avalon_players_mention.index(merlinmorganaArray[0])

                    the_index_one = avalon_players_mention.index(merlinmorganaArray[1])

                    random.shuffle(merlinmorganaArray)
                    random.shuffle(merlinmorganaArray)
                    random.shuffle(merlinmorganaArray)
                    random.shuffle(merlinmorganaArray)
                    random.shuffle(merlinmorganaArray)

                    for avalon_player in avalon_players:
                        their_index = avalon_players_mention.index(avalon_player.mention)
                        their_role = avalon_roles10[their_index]

                        await avalon_player.send(
                            f'>>> The roles are\n\nGood:\nLoyal\nLoyal\nLoyal\nLoyal\nPercival\nMerlin\n\nBad:\nMorgana\nAssassin\nMordred\nLackey')

                        if their_role == 'Loyal':
                            good_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**Nothing else**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Percival':
                            good_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**One of {merlinmorganaArray[0]} (Index Number: {the_index_zero}) and {merlinmorganaArray[1]} (Index Number: {the_index_one}) is the Merlin, the other is the Morgana**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Merlin':
                            good_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**Some of the bad people are:\n{the_morgana} (Index Number: {the_morgana_index})\n{the_assassin} (Index Number: {the_assassin_index})\n{the_lackey} (Index Number: {the_lackey_index})\nThere is another bad person called the Mordred but you do not know who they are**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Morgana':
                            bad_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_assassin} (Index Number: {the_assassin_index}) who is the Assassin\n{the_mordred} (Index Number: {the_mordred_index}) who is the Mordred\n{the_lackey} (Index Number: {the_lackey_index}) who is the Lackey**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Assassin':
                            bad_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_morgana} (Index Number: {the_morgana_index}) who is the Morgana\n{the_mordred} (Index Number: {the_mordred_index}) who is the Mordred\n{the_lackey} (Index Number: {the_lackey_index}) who is the Lackey**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Mordred':
                            bad_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_morgana} (Index Number: {the_morgana_index}) who is the Morgana\n{the_assassin} (Index Number: {the_assassin_index}) who is the Assassin\n{the_lackey} (Index Number: {the_lackey_index}) who is the Lackey**\n\nPlease also note your index number which is **{their_index}**'
                        elif their_role == 'Lackey':
                            bad_people.append(avalon_player.mention)
                            long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_morgana} (Index Number: {the_morgana_index}) who is the Morgana\n{the_assassin} (Index Number: {the_assassin_index}) who is the Assassin\n{the_mordred} (Index Number: {the_mordred_index}) who is the Mordred**\n\nPlease also note your index number which is **{their_index}**'
                        await avalon_player.send(f'>>> {long_message}')




        elif len(game_phase) > 0:
            await ctx.send(f">>> The game of Avalon has already started...")


    elif command.lower() == 'reset':
        await ctx.send("The game has been reset")

        game_phase.clear()
        avalon_players_mention.clear()
        avalon_players.clear()
        good_people.clear()
        bad_people.clear()
        fail_votes.clear()
        final_merlin.clear()
        mission_participants.clear()
        yes_no_already_voted.clear()
        has_voted.clear()
        pass_votes.clear()
        score_array.clear()
        yes_votes.clear()
        no_votes.clear()

        current_chooser_index.clear()
        current_chooser.clear()
        hammer_owner_index.clear()
        hammer_owner.clear()
        lady_owner_index.clear()
        lady_owner.clear()
        lady_use.clear()
        turns_done.clear()
        hammer_time.clear()

    elif command.lower() == 'yes' and len(game_phase) == 2:
        if ctx.author.mention in yes_no_already_voted:
            await ctx.author.send("you have already voted....")
            return

        yes_votes.append(0)
        yes_no_already_voted.append(ctx.author.mention)
        await ctx.send(f">>> {ctx.author.mention} has voted yes")
        if ( math.floor( (len(avalon_players_mention) + 2 ) / 2 ) == len(yes_votes) ):
            await ctx.send("Your mission will go underway")
            turns_done.clear()
            no_votes.clear()
            yes_votes.clear()
            yes_no_already_voted.clear()
            for person in mission_participants:
                person_index = avalon_players_mention.index(person)
                normal_name = avalon_players[person_index]
                await normal_name.send("You are now in a mission. Please type\n **.avalon vote pass** \n to pass the mission \n\n or \n\n **.avalon vote fail**\n to fail the mission")
            game_phase.append(0)
    elif command.lower() == 'no' and len(game_phase) == 2:
        if ctx.author.mention in yes_no_already_voted:
            await ctx.author.send("you have already voted....")
            return

        no_votes.append(0)
        yes_no_already_voted.append(ctx.author.mention)
        await ctx.send(f">>> {ctx.author.mention} has voted no")
        if ( math.floor( (len(avalon_players_mention) + 1 ) / 2 ) == len(no_votes) ):
            await ctx.send("Please let the next person vote...")
            game_phase.pop(0)
            no_votes.clear()
            yes_votes.clear()
            yes_no_already_voted.clear()
            mission_participants.clear()

            tempIndex = (current_chooser_index[0] + 1) % len(avalon_players_mention)
            current_chooser_index.clear()
            current_chooser_index.append(tempIndex)
            current_chooser.clear()
            current_chooser.append(avalon_players_mention[current_chooser_index[0]])
            turns_done.append(0)


            count_for_index_printing = 0
            main_board = ""
            for person in avalon_players_mention:
                main_board = f"{count_for_index_printing}: + {person}\n"
                count_for_index_printing = count_for_index_printing + 1

            if hammer_owner[0] == current_chooser[0]:
                await ctx.send(f">>> Its Hammer time\n\n{hammer_owner[0]}'s mission proposals will go through")
                hammer_owner.clear()
                hammer_time.append(0)

                turns_done.clear()
                return

            await ctx.send(
                f">>>Round: {len(score_array) + 1}\n\nCurrent Players:\n\n{main_board}\n\nIt is now {current_chooser[0]}'s turn.\n\nPlease nominate {rounds_array[len(avalon_players_mention) - 5][len(score_array)]} people to particpate in the mission. You can nominate yourself.\n\nThe Hammer lands on {hammer_owner[0]}. There is {(hammer_number[0] - len(turns_done))} turns left before they have full control of the proposal of the mission\n\n{lady_owner[0]} has the lady of the lake. You can use this at the start of the third round\n\nUnsure about the commands? Type\n**.avalon commands** to find out")


    else:

        split_command = command.lower().split()

        if len(game_phase) > 0:
            if split_command[0].lower() == "mission" and len(game_phase) == 1:

                split_command.pop(0)

                if rounds_array[len(avalon_players_mention) - 5][len(score_array)] != len(split_command):

                    await ctx.send(f">>> You have nominated {len(split_command)} people. However you must nominate {rounds_array[len(avalon_players_mention) - 5][len(score_array)]} people... ")
                    return

                potential_candidates = ""

                for person in split_command:
                    potential_candidates = potential_candidates + person + "\n"
                    editedPerson = "<@" + person[3:len(person)]
                    mission_participants.append(editedPerson)


                    if editedPerson not in avalon_players_mention:
                        await ctx.send("Some of the people you specified are not in the current game. Please try again :flushed:")
                        return

                    if editedPerson in mission_participants:
                        await ctx.send(f"{person} has already been selected in the mission. Please try again :flushed:")
                        return

                    mission_participants.append(editedPerson)
                    ####something important
                    #person_index = avalon_players_mention.index(person)
                    #normal_name = avalon_players[person_index]
                    #await normal_name.send("You are now in a mission. Please type\n **.avalon vote pass** \n to pass the mission \n\n or \n\n **.avalon vote fail**\n to fail the mission")


                game_phase.append(0)

                if len(hammer_time) > 0:
                    game_phase.append(0)
                    await ctx.send(f">>> {potential_candidates} have been selected to enter the mission")
                    hammer_time.clear()
                    for person in mission_participants:
                        person_index = avalon_players_mention.index(person)
                        normal_name = avalon_players[person_index]
                        await normal_name.send(
                            "You are now in a mission. Please type\n **.avalon vote pass** \n to pass the mission \n\n or \n\n **.avalon vote fail**\n to fail the mission")
                else:
                    await ctx.send(f">>> {potential_candidates} have been selected to enter the mission\n\nType\n**.avalon yes**\nto advance this mission\n\nOR\n\n**.avalon no**\nto cancel this mission")


            elif split_command[0].lower() == "vote" and len(game_phase) == 3:
                split_command.pop(0)

                if ctx.author.mention in has_voted:
                    await ctx.author.send("you have already voted....")
                    return

                if split_command[0].lower() == "pass":

                    has_voted.append(ctx.author.mention)
                    pass_votes.append(0)
                    await ctx.author.send("You have successfully voted")


                elif split_command[0].lower() == "fail":
                    has_voted.append(ctx.author.mention)
                    fail_votes.append(0)
                    await ctx.author.send("You have successfully voted")
                else:
                    await ctx.author.send("Invalid command...")

                if len(mission_participants) == len(has_voted):

                    avalon_channel = client.get_channel(int(os.getenv("AVALON_CHANNEL")))
                    await avalon_channel.send(f">>> Mission has been completed\nPass votes: {len(pass_votes)}\n\nFail votes: {len(fail_votes)}")

                    if len(fail_votes) < 2 and len(avalon_players_mention) > 6 and len(score_array) == 3:

                        await avalon_channel.send("The mission has passed")
                        score_array.append(1)

                    elif len(mission_participants) == len(pass_votes):
                        await avalon_channel.send("The mission has passed")
                        score_array.append(1)

                    else:
                        await avalon_channel.send("The mission has failed")
                        score_array.append(0)

                    game_phase.pop(0)
                    game_phase.pop(0)
                    mission_participants.clear()
                    has_voted.clear()
                    fail_votes.clear()
                    pass_votes.clear()

                    lady_use.clear()

                    if score_array.count(1) == 3:
                        game_phase.append(0)
                        game_phase.append(0)
                        game_phase.append(0)
                        await avalon_channel.send("It is time for the bad people to guess who the Merlin is")
                        return


                    elif score_array.count(0) == 3:
                        await avalon_channel.send("The bad team wins")
                        game_phase.clear()
                        avalon_players_mention.clear()
                        avalon_players.clear()
                        good_people.clear()
                        bad_people.clear()
                        fail_votes.clear()
                        final_merlin.clear()
                        mission_participants.clear()
                        yes_no_already_voted.clear()
                        has_voted.clear()
                        pass_votes.clear()
                        score_array.clear()
                        yes_votes.clear()
                        no_votes.clear()

                        current_chooser_index.clear()
                        current_chooser.clear()
                        hammer_owner_index.clear()
                        hammer_owner.clear()
                        lady_owner_index.clear()
                        lady_owner.clear()
                        lady_use.clear()
                        turns_done.clear()
                        hammer_time.clear()
                        return

                    tempIndex = (current_chooser_index[0] + 1) % len(avalon_players_mention)
                    current_chooser_index.clear()
                    current_chooser_index.append(tempIndex)
                    current_chooser.clear()
                    current_chooser.append(avalon_players_mention[current_chooser_index[0]])
                    turns_done.append(0)

                    hammer_owner_index.clear()
                    hammer_owner_index.append( (current_chooser_index[0] + 5) % len(avalon_players_mention) )
                    hammer_owner.clear()
                    hammer_owner.append(avalon_players_mention[ hammer_owner_index[0] ] )

                    lady_use.clear()

                    count_for_index_printing = 0
                    main_board = ""
                    for person in avalon_players_mention:
                        main_board = main_board + f"{count_for_index_printing}: {person}\n"
                        count_for_index_printing = count_for_index_printing + 1
                    await avalon_channel.send(
                        f">>> Round: {len(score_array) + 1}\n\nCurrent Players:\n\n{main_board}\n\nIt is now {current_chooser[0]}'s turn.\n\nPlease nominate {rounds_array[len(avalon_players_mention) - 5][len(score_array)]} people to participate in the mission. You can nominate yourself.\n\nThe Hammer lands on {hammer_owner[0]}. There is {(hammer_number[0] - len(turns_done))} turns left before they have full control of the proposal of the mission\n\n{lady_owner[0]} has the lady of the lake. You can use this at the start of the third round\n\nUnsure about the commands? Type\n**.avalon commands** to find out")


            elif split_command[0].lower() == "merlin" and len(game_phase) == 4:
                if len(game_phase) == 4:
                    person = split_command[1]
                    editedPerson = "<@" + person[3:len(person)]
                    if editedPerson == final_merlin[0]:
                        await ctx.send(f">>> Correct! {final_merlin[0]} is the Merlin\n\nThe Bad team wins")

                    else:
                        await ctx.send(f">>> Sorry, the actual Merlin was {final_merlin[0]} is the Merlin\n\nThe Good team wins")

                    game_phase.clear()
                    avalon_players_mention.clear()
                    avalon_players.clear()
                    good_people.clear()
                    bad_people.clear()
                    fail_votes.clear()
                    final_merlin.clear()
                    mission_participants.clear()
                    yes_no_already_voted.clear()
                    has_voted.clear()
                    pass_votes.clear()
                    score_array.clear()
                    yes_votes.clear()
                    no_votes.clear()

                    current_chooser_index.clear()
                    current_chooser.clear()
                    hammer_owner_index.clear()
                    hammer_owner.clear()
                    lady_owner_index.clear()
                    lady_owner.clear()
                    lady_use.clear()
                    turns_done.clear()
                    hammer_time.clear()
                    return
                else:
                    await ctx.send(f">>> Invalid Command for now...")
            elif split_command[0].lower() == "lady":
                person = split_command[1]
                editedPerson = "<@" + person[3:len(person)]
                if ctx.author.mention != lady_owner[0]:
                    await ctx.send("You do not own the lady of the lake")
                elif len(lady_use) > 0:
                    await ctx.send("The lady of the lake has already been used for this round")

                elif editedPerson not in avalon_players_mention:
                    await ctx.send("Could not find the person you want to inspect")
                elif len(score_array) < 2:
                    await ctx.send("You can not use the lady of the lake before the start of round 3")

                else:
                    if editedPerson in good_people:

                        await ctx.author.send(f"{editedPerson} is Good")

                    else:

                        await ctx.author.send(f"{editedPerson} is Bad")

                    lady_owner_index.clear()
                    lady_owner.clear()
                    lady_use.append(0)

                    lady_owner.append(editedPerson)
                    lady_owner_index.append(avalon_players_mention.index(editedPerson))
                    avalon_channel = client.get_channel(int(os.getenv("AVALON_CHANNEL")))
                    await avalon_channel.send(f">>> {editedPerson} now owns the lady of the lake")
        else:
            await ctx.send(f">>> Invalid Command...")

# reddit
already_posted = []

@client.event
async def reddit_updates():

    #new
    global post
    reset_limit = 205
    await client.wait_until_ready()
    channel = client.get_channel(int(os.getenv("kpop_news_channel_id")))
    reddit = apraw.Reddit(client_id=os.getenv("reddit_client_id"), client_secret=os.getenv("reddit_client_secret"),
                          username=os.getenv("reddit_username"), password=os.getenv("reddit_password"),
                          user_agent=os.getenv("reddit_user_agent"))

    subreddit = await reddit.subreddit('kpop')
    #new_kpop = subreddit.new(limit=5)

    while not client.is_closed():
        try:
            #  #async for post in subreddit.stream.submissions():
            async for post in subreddit.hot(limit=10):
                await asyncio.sleep(int(os.getenv("reddit_wait_time")))

                # for post in new_kpop:
                if post.url not in already_posted:
                    embed = discord.Embed(title="New Update",colour=0xc8dc6c)
                    title = f'{post.title}'
                    embed.add_field(name=title,value="See post below")
                    await channel.send(embed=embed)
                    await channel.send(f'>>> {post.url}')

                    already_posted.append(post.url)
                    if len(already_posted) >= reset_limit:
                        already_posted.pop(0)
        except Exception as e:
            embed = discord.Embed(colour=0xc8dc6c)
            title = f'An Error Occured'
            text = str(e)
            embed.add_field(name=title, value=text)
            channel = client.get_channel(int(os.getenv("error_stream_channel_id")))
            await channel.send(embed=embed)

@client.event
async def weather_updates():
    await client.wait_until_ready()
    channel = client.get_channel(int(os.getenv("weather_news_channel_id")))

    while not client.is_closed():
        try:
            owm = pyowm.OWM(os.getenv("OWM_API_KEY"))
            mgr = owm.weather_manager()
            try:
                obs = mgr.weather_at_place(os.getenv("MY_COUNTRY_LONG"))
            except Exception as e:
                embed2 = discord.Embed(colour=0xc8dc6c)
                title2 = f"Error"
                text2 = f"{str(e)}"
                embed2.add_field(name=title2, value=text2)
                await channel.send(embed=embed2)
                return
            w = obs.weather
            detailed_desc = w.detailed_status
            temperature = w.temperature('celsius')
            cloud_coverage = w.clouds
            wind = w.wind()
            humidity = w.humidity

            wind_direction = ""
            if wind["deg"] >= 345 or wind["deg"] <= 15:
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


            bigtitle = "Weather Forecast in " + os.getenv("MY_COUNTRY_LONG")
            embed = discord.Embed(title=bigtitle, colour=0xc8dc6c)
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
            await channel.send(embed=embed)
        except Exception as e:
            embed2 = discord.Embed(colour=0xc8dc6c)
            title2 = f"Error"
            text2 = f"{str(e)}"
            embed2.add_field(name=title2, value=text2)
            await channel.send(embed=embed2)
        await asyncio.sleep(int(os.getenv("weather_wait_time")))

@client.event
async def idolpost_updates():
    await client.wait_until_ready()
    channel = client.get_channel(int(os.getenv("idolpost_channel_id")))

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

        embed = discord.Embed(title="Idol of the Hour", description=f'{finalGroup} {finalName}', colour=0xc8dc6c)
        file = discord.File(("photos/" + str(finalFromData)), filename="image.jpg")
        embed.set_image(url="attachment://image.jpg")
        await channel.send(file=file, embed=embed)
        await asyncio.sleep(int(os.getenv("idolpost_wait_time")))

@client.event
async def botstatus_updates():
    await client.wait_until_ready()
    channel = client.get_channel(int(os.getenv("botstatus_channel_id")))

    while not client.is_closed():
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(timedelta(seconds=difference))
        embed = discord.Embed(colour=0xc8dc6c)
        embed.add_field(name="Uptime", value=text)
        embed.set_footer(text="Juicy Peach Apricot")
        try:
            await channel.send(embed=embed)
        except discord.HTTPException:
            await channel.send("Current uptime: " + text)
        await asyncio.sleep(int(os.getenv("botstatus_wait_time")))


@client.event
async def birthday_updates():
    await client.wait_until_ready()
    channel = client.get_channel(int(os.getenv("birthday_channel_id")))

    while not client.is_closed():

        country_time_zone = pytz.timezone(os.getenv("MY_COUNTRY_SHORT"))
        country_time = datetime.now(country_time_zone)
        final_date = country_time.strftime("%m-%d")
        final_display_date = country_time.strftime("%B %#d")

        messages = await channel.history(limit=20).flatten()

        not_detected = True;
        for thing in messages:
            for embed in thing.embeds:
                for field in embed.fields:
                    if str(field.name).strip() == f"Birthdays for {final_display_date.strip()}":
                        not_detected = False

        if not_detected:

            text = ''
            with open(f"birthdays/{final_date.strip()}.txt", "r") as f:
                for item in f:
                    text = text + item

            embed = discord.Embed(colour=0xc8dc6c)
            title = f"Birthdays for {final_display_date}"
            embed.add_field(name=title, value=text)
            await channel.send(embed=embed)

        await asyncio.sleep(int(os.getenv("birthday_wait_time")))

client.loop.create_task(reddit_updates())
client.loop.create_task(weather_updates())
client.loop.create_task(idolpost_updates())
client.loop.create_task(botstatus_updates())
client.loop.create_task(birthday_updates())
client.run(my_discord_token)

