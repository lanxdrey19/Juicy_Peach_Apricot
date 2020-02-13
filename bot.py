# for discord functionality

import discord
from discord.ext import commands, tasks
import asyncio

# for chatterbot functionality

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# for weather updates

import pyowm

# for artwork

from PIL import Image, ImageDraw, ImageFont

# for music quiz

from discord.utils import get
import youtube_dl
import os

# miscellaneous

import math
import random
from itertools import cycle
from random import randint

# might be important later

# import nltk
# nltk.download('popular', quiet=True)
# import warnings
# warnings.filterwarnings("ignore")

# Bot prefix

client = commands.Bot(command_prefix = '.')

# For the bot's status

status = cycle(['Fiesta','Hands Up', 'Nun Nu Nan Na', 'Crossroads', 'Wish', 'So What', 'Dun Dun','Cool',  'Bouncy', 'Say My Name'])


@client.event
async def on_ready():
    change_status.start()
    #await client.change_presence(status=discord.Status.online, activity=discord.Game('Always Be Your Girl (너의 소녀가 되어줄게)'))
    print('Bot is ready.')
    print('We have logged in as {0.user}'.format(client))


@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

# Events that get triggered

@client.event
async def on_message(message):

    coolWords1 = ["clear", "CLEAR", "Clear", "clc", "CLC", "Clc"]
    coolWords2 = ["omg", "OMG", 'Omg']
    coolWords3 = ["hi", "HI", "Hi", "HELLO", "Hello", "hello", "help", "Help", "HELP"]
    coolWords4 = ["^2", "up to", "Up To","Up to", "UP TO"]
    coolWords5 = ["Pong","pong", "PONG"]
    coolWords6 = ["dice"]
    coolWords7 = ["8ball"]
    coolWords8 = ["Question:", "Compatibility:"]
    coolWords9 = ["hug", ".cheerup "]
    coolWords10 = [".match"]
    coolWords11 = ["bye","Bye","BYE","GTG","Gtg","gtg","gotta go","Gotta go"]
    coolWords12 = ["!cd", "!ww","!t"]
    coolWords13 = ["im","Im","IM", "I'm","i'm","I'M","i am","I am", "I Am", "I AM"]



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

    if message.author == client.user:
        return

    for word in coolWords1:
        if message.content.count(word) > 0:
            await message.channel.send('>>> >clear\n**clears existing variables in the workspace**\n>clc\nhttps://www.youtube.com/watch?v=MY4qnUGwWIU')
            emoji = '🤣'
            await message.add_reaction(emoji)

    for word in coolWords2:
        if message.content.count(word) > 0:
            await message.channel.send('>>> https://www.youtube.com/watch?v=QTD_yleCK9Y')
            emoji = '😱'
            await message.add_reaction(emoji)

    for word in coolWords3:
        if message.content.startswith(word):
            await message.channel.send(f'>>> Hello there {message.author.mention}! I am Sad Bot\nType **.commands** or **.help** for the list of all commands\nFeel free to make suggestions in the **#suggestions** channel\n\nhttps://thumbs.gfycat.com/PhonySelfishArrowana.webp')
            emoji = '👋'
            # or '\U0001f44d' or '👍'
            await message.add_reaction(emoji)
            return

    for word in coolWords4:
        if message.content.startswith(word):
            await message.channel.send('>>> https://www.youtube.com/watch?v=nUODTpWSmm0\nHow about you?')
            emoji = '😂'
            await message.add_reaction(emoji)

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

    for word in coolWords11:
        if message.content.count(word) > 0:
            await message.channel.send(f'>>> https://www.youtube.com/watch?v=4gX_p1VkgA4')
            await message.channel.send(f">>> Bye bye {message.author.mention}\n\nhttps://gfycat.com/BetterFondHumpbackwhale")
            emoji = '👋'
            # or '\U0001f44d' or '👍'
            await message.add_reaction(emoji)

    for word in coolWords12:
        if message.content.count(word) > 0:
            if randint(1,20) == 1:
                await message.channel.send(">>> Your free trial of Kokobot has ended. However, Sadbot will always be free. Use Sadbot today!\n\n https://scontent.fakl6-1.fna.fbcdn.net/v/t1.15752-9/82462694_272856383692002_507557532571533312_n.jpg?_nc_cat=105&_nc_ohc=T61ibjd8r44AX_9ZXSp&_nc_ht=scontent.fakl6-1.fna&oh=c8467554b6b0be0dc27bfee1e38cab98&oe=5E9F6FBF")
            else:
                return
    for word in coolWords13:
        if message.content.startswith(word):
            #img = Image.new('RGBA', (1200, 1200), 'white')
            img = Image.open("iam.png")

            font = ImageFont.truetype("arial.ttf", 60)
            str1 = message.content
            str2 = f"From: {message.author}"
            draw = ImageDraw.Draw(img)
            draw.text((1, 75), str1, font=font, fill='cyan')
            draw.text((1,800),str2 , font=font, fill='cyan')

            img.save("iam2.png")

            await message.channel.send(file=discord.File("iam2.png"))


            img.close()
            img2 = Image.open("iam.png")
            img2.save("iam2.png")
            img2.close()

    await client.process_commands(message)


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

# Commands

@client.command(help="Displays a list of all commands")
async def commands(ctx):
    await ctx.send('```css\nGeneral Commands:\n\n.8ball {your_question} - Ask it a question\n\n.about - Details of Sadbot\n\n.artwork {colour} - Creates your artwork with the colour you have specified (You must specify a colour for this command to work. For example, type .artwork blue)\n\n.cheerup - Try this one if you are feeling down\n\n.conway - A Conway Game of Life Simulator\n\n.dice - Rolls die\n\n.examszn - Get some words of wisdom from the bot if you are feeling stressed for your upcoming exams\n\n.hug {@person} - Try this one on someone. This will only work if you ping the user you want to hug\n\n.match {person1 and person2} - Ship yourself with your crush (For example, type .match Thomas and Nayeon)\n\n.piglatin {your message} - Convert your message to Pig Latin\n\n.ping - Checks latency\n\n.sadbot {your message} - Talk to sadbot about kpop\n\n.stanloona {your message} - Convert your message to let others know you really stan LOONA\n\nGame Commands:\n\n.idolguess commands - For Guess the Idol Game commands\n\n.idolquest commands - For Idol Quest Game commands\n\n.avalon commands - For Avalon Game commands\n\n.musicquiz commands - For Music Quiz commands```')

@client.command(help="Displays details of Sadbot")
async def about(ctx):
    await ctx.send(">>> Version: 0.4.0\nLatest Additions: Music Quiz\nFuture Additions: To be announced...\nMaintainer: chuuchu#2206\nGithub: https://github.com/oliviacolombia/sadbot\n\nSadbot has been made with lots of love!\n\nhttps://gfycat.com/AchingLeanFalcon")


@client.command(help="Checks Latency")
async def ping(ctx):
    await ctx.send(f'>>> Pong!\nLatency: {round(client.latency * 1000)} ms')


@client.command(help="Try this one on someone. This will only work if you ping the user you want to hug")
async def hug(ctx, member: discord.Member):
    await ctx.send(f'>>> OwO (>^.^)> (っ´∀｀)っ (っ⇀⑃↼)っ {member.mention} ⊂(・﹏・⊂) ლ(･ω･*ლ) <(^.^<) OwO')


@hug.error
async def hug_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.BadArgument):
        await ctx.send('>>> Error: User not found **OR** "@" is missing at the start.\nPlease try again...')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.BadArgument):
        await ctx.send('>>> Error: Enter appropriate arguments.\nPlease try again...')


@client.command(help="Ask it a question (Will not work if no arguments are entered)",aliases=['8ball'])
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
    await ctx.send(f'>>> Question: {question}?\nAnswer: {random.choice(responses)}')


@client.command(help="Ship yourself with your crush (For example, type .match Thomas and Nayeon)Displays details of Sadbot")
async def match(ctx, *, question):
    await ctx.send(f'>>> Shipping {question}...\nCompatibility: {randint(0,100)}%')


@client.command(help="Rolls die")
async def dice(ctx):
    await ctx.send(f'>>> :game_die: **Rolls game die** :game_die:\n{randint(1,6)}')


@client.command(help="Get some words of wisdom from the bot if you are feeling stressed for your upcoming exams")
async def examszn(ctx):
    await ctx.send('>>> https://scontent.fakl6-1.fna.fbcdn.net/v/t1.15752-9/82276376_604105316813162_5652167650046902272_n.jpg?_nc_cat=110&_nc_ohc=sJgWVpNAbHAAX-17ANX&_nc_ht=scontent.fakl6-1.fna&oh=0da1366686ae449cf1c6f4a1e6f68d20&oe=5EBE1A66')


@client.command(help="Convert your message to let others know you really stan LOONA",aliases=['sl'])
async def stanloona(ctx,*,arg):
    temp = arg.split()
    big_message = ""
    for thing in temp:
        med_message = " Stan " + thing + " Loona "
        big_message = big_message + med_message
    await ctx.send(f">>> {big_message}")


@client.command(help="Convert your message to Pig Latin",aliases=['pl'])
async def piglatin(ctx,*,arg):
    temp = arg.split()
    big_message = ""
    for thing in temp:
        med_message = thing[-1]  + thing[:-1] + "e"
        big_message = big_message + " " + med_message + " "
    await ctx.send(f">>> {big_message}")

@client.command(help="Creates your artwork with the colour you have specified (You must specify a colour for this command to work. For example, type .artwork blue)")
async def artwork(ctx, colour):

    img = Image.new('RGBA', (1200, 1200), 'silver')

    font = ImageFont.truetype("arial.ttf", 5)
    str1 = '*'
    draw = ImageDraw.Draw(img)

    the_count = 0
    randpointx = randint(0, 1199)
    randpointy = randint(0, 1199)
    prevplotx = randpointx
    prevploty = randpointy

    draw.text((randpointx, randpointy), str1, font=font, fill=colour)
    while the_count < 100000:


        xcoords = [600,1,1199]
        ycoords = [1,1199,1199]
        rand_index = randint(0,2)

        final_pointx = xcoords[rand_index]
        final_pointy = ycoords[rand_index]

        prevplotx = int(( final_pointx + prevplotx ) / 2)
        prevploty = int(( final_pointy + prevploty ) / 2)


        draw.text((prevplotx,prevploty),str1,font=font,fill=colour)

        the_count = the_count + 1


    img.save("artwork.png")

    await ctx.send(file=discord.File("artwork.png"))

conway_players = []

@client.command(help="Try this one if you are feeling down")
async def cheerup(ctx):

    f = open("kpop.txt", "r")
    theirGroup = []
    theirName = []
    theirPhoto = []


    for x in f:
        temp = x.split()
        theirGroup.append(temp[0])
        theirName.append(temp[1])
        theirPhoto.append(temp[2])

    f.close()
    # 163 kpop idols in txt file jan 15 2020
    theIndex = randint(0,162)
    finalGroup = theirGroup[theIndex]
    finalName = theirName[theIndex]

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

    await ctx.send(f">>> :blush: Here's another photo to cheer you up! :blush:\n\n")
    await ctx.send(f'>>> {random.choice(cheers)}')
    await ctx.send(f'{theirPhoto[theIndex]}')

@client.command(help="A Conway Game of Life Simulator")
async def conway(ctx):
    for people in conway_players:
        if people == ctx.author.mention:
            await ctx.send('You already have a simulation going on...')
            return
    conway_players.append(ctx.author.mention)
    s = ['w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','\n','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','\n','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','\n','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','\n','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','\n','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','\n','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','\n','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','\n','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','\n','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','\n',]

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

    m0 = await ctx.send(f'>>> {final_display}')

    generation = [0]
    m1 = await ctx.send(f'>>> Generation: {len(generation)}')
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

        await m0.edit(content=f'>>> {final_next_display}')
        await m1.edit(content=f'>>> Generation: {len(generation)}')

        if len(generation) == 100:
            generation.clear()
            IsOver.pop(0)
            await ctx.send(f">>> Stopping at Generation 100, you may start a new simulation {ctx.author.mention}")
            some_count.clear()
            blank_count.clear()
            for people in conway_players:
                if people == ctx.author.mention:
                    conway_players.remove(people)

            return


        if len(blank_count) == 200:
            generation.clear()
            IsOver.pop(0)
            await ctx.send(f">>> No more Cells Remaining, you may start a new simulation {ctx.author.mention}")
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

##### Games #####

# Avalon

# Initialising mission requirements and roles
rounds_array = [ [2,2,2,3,3,3] , [3,3,3,4,4,4], [2,4,3,4,4,4] , [3,3,4,5,5,5], [3,4,4,5,5,5]]
avalon_roles5 = ['Loyal', 'Percival', 'Merlin','Morgana', 'Assassin']
avalon_roles6 = ['Loyal', 'Loyal', 'Percival', 'Merlin', 'Morgana', 'Assassin']
avalon_roles7 = ['Loyal', 'Loyal', 'Percival', 'Merlin', 'Morgana', 'Assassin', 'Mordred']
avalon_roles8 = ['Loyal', 'Loyal', 'Loyal', 'Percival', 'Merlin', 'Morgana', 'Assassin', 'Mordred']
avalon_roles9 = ['Loyal', 'Loyal', 'Loyal', 'Loyal','Percival', 'Merlin', 'Morgana', 'Assassin', 'Mordred']
avalon_roles10 = ['Loyal', 'Loyal', 'Loyal', 'Loyal', 'Percival', 'Merlin', 'Morgana', 'Assassin','Mordred','Lackey']

# Who's in which team
avalon_players = []
bad_team = []
good_team = []

# Score, phase and round trackers
round_phase = []
game_phase = []
good_score = []
bad_score = []

# Pre-Mission Privileges
current_person = []
current_person_index = []
hammer_person = []
lady_person = []
lady_use = []

# Pre-mission votes
yes_count = []
no_count = []

# Mission Privileges
mission_participants = []
mission_has_voted = []
fail_votes = []

# Miscellaneous
the_game_merlin = []
reaction_message = []

@client.command(help="Type .avalon commands for more information about this command",aliases=['a'])
async def avalon(ctx, response):
    if response == 'commands':
        await ctx.send("```css\n\n.avalon join - Join Avalon Matchmaking\n\n.avalon start - Commences an Avalon game\n\n.avalon myrole - Your Avalon role will be sent to you via a direct message from Sadbot\n\n.choose {participants} - Nominate who you want to go undertake the current mission. Remember to tag them when using this command\n\navalon pass - Pass the mission\n\n.avalon fail - Fail the mission\n\n.lady {person you want to find the alliance of} - Checks the role of the person using the Lady of the Lake. Remember to tag them when using this command\n\n.merlin {person who you think is Merlin} - The bad people to win the game if they guess who the Merlin is correctly. Remember to tag them when using this command```")
    elif response == 'join':
        if len(round_phase) != 0:
            await ctx.send(f"Please wait for the next game {ctx.author.mention}")
            return

        if len(avalon_players) == 10:
            await ctx.send(f"Avalon can only have ten players at maximum {ctx.author.mention}")
            return

        for name in avalon_players:
            if name == ctx.author.mention:
                await ctx.send(f"You are already in Avalon matchmaking {ctx.author.mention}")
                return

        avalon_players.append(ctx.author.mention)

        await ctx.send(f"You have successfully joined Avalon matchmaking {ctx.author.mention}\n\n Number of players in matchmaking: {len(avalon_players)}")

    elif response == 'leave':

        if len(round_phase) != 0:
            await ctx.send(f"You can not leave the current Avalon game once it has started {ctx.author.mention}")
            return

        for name in avalon_players:
            if name == ctx.author.mention:
                avalon_players.remove(name)
                await ctx.send(f"You have successfully left Avalon matchmaking {ctx.author.mention}")
                return

        await ctx.send(f"You were not in Avalon matchmaking yet {ctx.author.mention}")

    elif response == 'start':


        if len(avalon_players) < 5:
            await ctx.send(f"Avalon needs at least five players {ctx.author.mention}")
            return
        else:

            game_phase.append(0)
            round_phase.append(0)

            random_person = random.choice(avalon_players)
            current_person.append(random_person)

            current_person_index.append(avalon_players.index(random_person))

            if current_person_index[0] + 1 == len(avalon_players):
                lady_person.append(avalon_players[0])
            else:
                lady_person.append(avalon_players[current_person_index[0] + 1])

            if current_person_index[0] - 4 < 0:
                leftovers = current_person_index[0] - 4
                final_hammer_index = len(avalon_players) + leftovers
                hammer_person.append(final_hammer_index)
            else:
                final_hammer_index = current_person_index[0] - 4
                hammer_person.append(final_hammer_index)


            await ctx.send(f"Round {len(round_phase)}\n\nList of players:\n\n:arrow_left: {avalon_players} :arrow_right: \n\nIt is currently {current_person[0]}'s turn. Please choose {rounds_array[ len(avalon_players) - 5 ][ len(round_phase) - 1 ]} people to go on the mission. Type **.choose @person(1) @person(2)... @person(n-2) @person(n-1) @person(n)** to nominate who will go into the mission\n\nHammer falls on {hammer_person[0]}\n\nLady of the lake falls on {lady_person[0]}. After the end of round two, you can use this card. Type **.lady @person** to see their alliance")
    elif response == 'pass':


        if len(game_phase) != 2:
            await ctx.send(f"Voting is invalid for now... {ctx.author.mention}")
        for people in mission_has_voted:
            if ctx.author.mention == people:
                await ctx.send(f"You have already voted {ctx.author.mention}")
                return
        for people in mission_participants:
            if ctx.author.mention == people:
                mission_has_voted.append(0)
                await ctx.send("You have successfully voted")


        if (len(mission_participants) == mission_has_voted and len(game_phase) != 4 and len(fail_votes) < 1) or (len(mission_participants) == mission_has_voted and len(game_phase) == 4 and len(fail_votes < 2) and len(avalon_players) > 6):
            channel = client.get_channel(your_channel_id_goes_here)
            await channel.send(f"The mission has passed. Number of fails: {len(fail_votes)} ")

            good_score.append(0)
            round_phase.append(0)
            mission_has_voted.clear()
            mission_participants.clear()
            lady_use.clear()

            if len(good_score) == 3:

                game_phase.append(0)

                await channel.send(f"The bad people {bad_team} have one more chance to win if they guess who the Merlin is. Type **.merlin @person** to guess who the Merlin is")
                return

            elif len(good_score) != 3:
                round_phase.append(0)
                game_phase.remove(0)

                if current_person_index[0] - 4 < 0:
                    leftovers = current_person_index[0] - 4
                    final_hammer_index = len(avalon_players) + leftovers
                    hammer_person.append(final_hammer_index)
                else:
                    final_hammer_index = current_person_index[0] - 4
                    hammer_person.append(final_hammer_index)

                await channel.send(f"Round {len(round_phase)}\n\nList of players:\n\n:arrow_left: {avalon_players} :arrow_right: \n\nIt is currently {current_person[0]}'s turn. Please choose {rounds_array[len(avalon_players) - 5][len(round_phase) - 1]} people to go on the mission. Type **.choose @person(1) @person(2)... @person(n-2) @person(n-1) @person(n)** to nominate who will go into the mission\n\nHammer falls on {hammer_person[0]}\n\nLady of the lake falls on {lady_person[0]}. After the end of round two, you can use this card. Type **.lady @person** to see their alliance")




    elif response == 'fail':

        if len(game_phase) != 2:
            await ctx.send(f"Voting is invalid for now... {ctx.author.mention}")
        for people in mission_has_voted:
            if ctx.author.mention == people:
                await ctx.send(f"You have already voted {ctx.author.mention}")
                return
        for people in mission_participants:
            if ctx.author.mention == people:
                mission_has_voted.append(0)
                fail_votes.append(0)
                await ctx.send("You have successfully voted")

        if ( len(fail_votes) >= 1 and round_phase != 4 ) or ( len(fail_votes) >= 2 and avalon_players >= 7  and round_phase == 4 ):
            channel = client.get_channel(your_channel_id_goes_here)

            await channel.send(f"The mission has failed. Number of fails: {len(fail_votes)}")

            bad_score.append(0)
            round_phase.append(0)
            mission_has_voted.clear()
            mission_participants.clear()
            lady_use.clear()

            if len(bad_score) == 3:

                await channel.send(f"The bad people win! Congrats {bad_team}")

                avalon_players.clear()
                bad_team.clear()
                good_team.clear()

                round_phase.clear()
                game_phase.clear()
                good_score.clear()
                bad_score.clear()

                current_person.clear()
                current_person_index.clear()
                hammer_person.clear()
                lady_person.clear()
                lady_use.clear()

                yes_count.clear()
                no_count.clear()

                mission_participants.clear()
                mission_has_voted.clear()
                fail_votes.clear()

                the_game_merlin.clear()
                reaction_message.clear()
                return

            elif len(bad_score) != 3:
                round_phase.append(0)
                game_phase.remove(0)

                if current_person_index[0] - 4 < 0:
                    leftovers = current_person_index[0] - 4
                    final_hammer_index = len(avalon_players) + leftovers
                    hammer_person.append(final_hammer_index)
                else:
                    final_hammer_index = current_person_index[0] - 4
                    hammer_person.append(final_hammer_index)

                await channel.send(f"Round {len(round_phase)}\n\nList of players:\n\n:arrow_left: {avalon_players} :arrow_right: \n\nIt is currently {current_person[0]}'s turn. Please choose {rounds_array[len(avalon_players) - 5][len(round_phase) - 1]} people to go on the mission. Type **.choose @person(1) @person(2)... @person(n-2) @person(n-1) @person(n)** to nominate who will go into the mission\n\nHammer falls on {hammer_person[0]}\n\nLady of the lake falls on {lady_person[0]}. After the end of round two, you can use this card. Type **.lady @person** to see their alliance")

    elif response == 'myrole':
        if len(game_phase) >= 1:

            if len(avalon_players) == 5:

                await ctx.author.send(f'>>> The roles are\n\nGood:\nLoyal\nPercival\nMerlin\n\nBad:\nMorgana\nAssassin')

                random.shuffle(avalon_roles5)
                random.shuffle(avalon_roles5)
                random.shuffle(avalon_roles5)
                random.shuffle(avalon_roles5)
                random.shuffle(avalon_roles5)

                their_index = avalon_players.index(ctx.author.mention)

                their_role = avalon_roles5[their_index]

                the_merlin_index = avalon_roles5.index("Merlin")

                the_merlin = avalon_players[the_merlin_index]

                the_morgana_index = avalon_roles5.index("Morgana")

                the_morgana = avalon_players[the_morgana_index]

                the_assassin_index = avalon_roles5.index("Assassin")

                the_assassin = avalon_players[the_assassin_index]

                merlinmorganaArray = [the_merlin, the_morgana]

                the_index_zero = avalon_players.index(merlinmorganaArray[0])

                the_index_one = avalon_players.index(merlinmorganaArray[1])

                random.shuffle(merlinmorganaArray)
                random.shuffle(merlinmorganaArray)
                random.shuffle(merlinmorganaArray)
                random.shuffle(merlinmorganaArray)
                random.shuffle(merlinmorganaArray)

                if their_role == 'Loyal':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**Nothing else**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Percival':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**One of {merlinmorganaArray[0]} (Index Number: {the_index_zero}) and {merlinmorganaArray[1]} (Index Number: {the_index_one}) is the Merlin, the other is the Morgana**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Merlin':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**The bad people are:\n{the_morgana} (Index Number: {the_morgana_index})\n{the_assassin} (Index Number: {the_assassin_index})**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Morgana':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad person is:\n{the_assassin} (Index Number: {the_assassin_index}) who is the Assassin**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Assassin':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad person is:\n{the_morgana} (Index Number: {the_morgana_index}) who is the Morgana**\n\nPlease also note your index number which is **{their_index}**'
                await ctx.author.send(f'>>> {long_message}')

                for name in avalon_players:
                    temp_index = avalon_players.index(name)
                    if avalon_roles5[temp_index] == "Morgana" or avalon_roles5[temp_index] == "Assassin":
                        bad_team.append(name)
                    else:
                        good_team.append(name)

                merlin_final_index = avalon_roles5.index("Merlin")
                merlin_final = avalon_players[merlin_final_index]
                the_game_merlin.append(merlin_final)

            elif len(avalon_players) == 6:


                await ctx.author.send(f'>>> The roles are\n\nGood:\nLoyal\nLoyal\nPercival\nMerlin\n\nBad:\nMorgana\nAssassin')

                random.shuffle(avalon_roles6)
                random.shuffle(avalon_roles6)
                random.shuffle(avalon_roles6)
                random.shuffle(avalon_roles6)
                random.shuffle(avalon_roles6)

                their_index = avalon_players.index(ctx.author.mention)

                their_role = avalon_roles6[their_index]

                the_merlin_index = avalon_roles6.index("Merlin")

                the_merlin = avalon_players[the_merlin_index]

                the_morgana_index = avalon_roles6.index("Morgana")

                the_morgana = avalon_players[the_morgana_index]

                the_assassin_index = avalon_roles6.index("Assassin")

                the_assassin = avalon_players[the_assassin_index]

                merlinmorganaArray = [the_merlin, the_morgana]

                the_index_zero = avalon_players.index(merlinmorganaArray[0])

                the_index_one = avalon_players.index(merlinmorganaArray[1])

                random.shuffle(merlinmorganaArray)
                random.shuffle(merlinmorganaArray)
                random.shuffle(merlinmorganaArray)
                random.shuffle(merlinmorganaArray)
                random.shuffle(merlinmorganaArray)

                if their_role == 'Loyal':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**Nothing else**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Percival':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**One of {merlinmorganaArray[0]} (Index Number: {the_index_zero}) and {merlinmorganaArray[1]} (Index Number: {the_index_one}) is the Merlin, the other is the Morgana**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Merlin':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**The bad people are:\n{the_morgana} (Index Number: {the_morgana_index})\n{the_assassin} (Index Number: {the_assassin_index})**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Morgana':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad person is:\n{the_assassin} (Index Number: {the_assassin_index}) who is the Assassin**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Assassin':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad person is:\n{the_morgana} (Index Number: {the_morgana_index}) who is the Morgana**\n\nPlease also note your index number which is **{their_index}**'

                await ctx.author.send(f'>>> {long_message}')

                for name in avalon_players:
                    temp_index = avalon_players.index(name)
                    if avalon_roles6[temp_index] == "Morgana" or avalon_roles5[temp_index] == "Assassin":
                        bad_team.append(name)
                    else:
                        good_team.append(name)

                merlin_final_index = avalon_roles6.index("Merlin")
                merlin_final = avalon_players[merlin_final_index]
                the_game_merlin.append(merlin_final)

            elif len(avalon_players) == 7:


                await ctx.author.send(f'>>> The roles are\n\nGood:\nLoyal\nLoyal\nPercival\nMerlin\n\nBad:\nMorgana\nAssassin\nMordred')

                random.shuffle(avalon_roles7)
                random.shuffle(avalon_roles7)
                random.shuffle(avalon_roles7)
                random.shuffle(avalon_roles7)
                random.shuffle(avalon_roles7)

                their_index = avalon_players.index(ctx.author.mention)

                their_role = avalon_roles7[their_index]

                the_merlin_index = avalon_roles7.index("Merlin")

                the_merlin = avalon_players[the_merlin_index]

                the_morgana_index = avalon_roles7.index("Morgana")

                the_morgana = avalon_players[the_morgana_index]

                the_assassin_index = avalon_roles7.index("Assassin")

                the_assassin = avalon_players[the_assassin_index]

                the_mordred_index = avalon_roles7.index("Mordred")

                the_mordred = avalon_players[the_mordred_index]

                merlinmorganaArray = [the_merlin, the_morgana]

                the_index_zero = avalon_players.index(merlinmorganaArray[0])

                the_index_one = avalon_players.index(merlinmorganaArray[1])

                random.shuffle(merlinmorganaArray)
                random.shuffle(merlinmorganaArray)
                random.shuffle(merlinmorganaArray)
                random.shuffle(merlinmorganaArray)
                random.shuffle(merlinmorganaArray)

                if their_role == 'Loyal':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**Nothing else**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Percival':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**One of {merlinmorganaArray[0]} (Index Number: {the_index_zero}) and {merlinmorganaArray[1]} (Index Number: {the_index_one}) is the Merlin, the other is the Morgana**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Merlin':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**Some of the bad people are:\n{the_morgana} (Index Number: {the_morgana_index})\n{the_assassin} (Index Number: {the_assassin_index})\nThere is another bad person called the Mordred but you do not know who they are**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Morgana':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_assassin} (Index Number: {the_assassin_index}) who is the Assassin\n{the_mordred} (Index Number: {the_mordred_index}) who is the Mordred**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Assassin':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_morgana} (Index Number: {the_morgana_index}) who is the Morgana\n{the_mordred} (Index Number: {the_mordred_index}) who is the Mordred**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Mordred':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_morgana} (Index Number: {the_morgana_index}) who is the Morgana\n{the_assassin} (Index Number: {the_assassin_index}) who is the Assassin**\n\nPlease also note your index number which is **{their_index}**'
                await ctx.author.send(f'>>> {long_message}')

                for name in avalon_players:
                    temp_index = avalon_players.index(name)
                    if avalon_roles7[temp_index] == "Morgana" or avalon_roles5[temp_index] == "Assassin" or avalon_roles5[temp_index] == "Mordred":
                        bad_team.append(name)
                    else:
                        good_team.append(name)

                merlin_final_index = avalon_roles7.index("Merlin")
                merlin_final = avalon_players[merlin_final_index]
                the_game_merlin.append(merlin_final)

            elif len(avalon_players) == 8:


                await ctx.author.send(
                    f'>>> The roles are\n\nGood:\nLoyal\nLoyal\nLoyal\nPercival\nMerlin\n\nBad:\nMorgana\nAssassin\nMordred')

                random.shuffle(avalon_roles8)
                random.shuffle(avalon_roles8)
                random.shuffle(avalon_roles8)
                random.shuffle(avalon_roles8)
                random.shuffle(avalon_roles8)

                their_index = avalon_players.index(ctx.author.mention)

                their_role = avalon_roles8[their_index]

                the_merlin_index = avalon_roles8.index("Merlin")

                the_merlin = avalon_players[the_merlin_index]

                the_morgana_index = avalon_roles8.index("Morgana")

                the_morgana = avalon_players[the_morgana_index]

                the_assassin_index = avalon_roles8.index("Assassin")

                the_assassin = avalon_players[the_assassin_index]

                the_mordred_index = avalon_roles8.index("Mordred")

                the_mordred = avalon_players[the_mordred_index]

                merlinmorganaArray = [the_merlin, the_morgana]

                the_index_zero = avalon_players.index(merlinmorganaArray[0])

                the_index_one = avalon_players.index(merlinmorganaArray[1])

                random.shuffle(merlinmorganaArray)
                random.shuffle(merlinmorganaArray)
                random.shuffle(merlinmorganaArray)
                random.shuffle(merlinmorganaArray)
                random.shuffle(merlinmorganaArray)

                if their_role == 'Loyal':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**Nothing else**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Percival':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**One of {merlinmorganaArray[0]} (Index Number: {the_index_zero}) and {merlinmorganaArray[1]} (Index Number: {the_index_one}) is the Merlin, the other is the Morgana**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Merlin':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**Some of the bad people are:\n{the_morgana} (Index Number: {the_morgana_index})\n{the_assassin} (Index Number: {the_assassin_index})\nThere is another bad person called the Mordred but you do not know who they are**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Morgana':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_assassin} (Index Number: {the_assassin_index}) who is the Assassin\n{the_mordred} (Index Number: {the_mordred_index}) who is the Mordred**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Assassin':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_morgana} (Index Number: {the_morgana_index}) who is the Morgana\n{the_mordred} (Index Number: {the_mordred_index}) who is the Mordred**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Mordred':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_morgana} (Index Number: {the_morgana_index}) who is the Morgana\n{the_assassin} (Index Number: {the_assassin_index}) who is the Assassin**\n\nPlease also note your index number which is **{their_index}**'
                await ctx.author.send(f'>>> {long_message}')

                for name in avalon_players:
                    temp_index = avalon_players.index(name)
                    if avalon_roles8[temp_index] == "Morgana" or avalon_roles5[temp_index] == "Assassin" or avalon_roles5[temp_index] == "Mordred":
                        bad_team.append(name)
                    else:
                        good_team.append(name)

                merlin_final_index = avalon_roles8.index("Merlin")
                merlin_final = avalon_players[merlin_final_index]
                the_game_merlin.append(merlin_final)

            elif len(avalon_players) == 9:


                await ctx.author.send(
                    f'>>> The roles are\n\nGood:\nLoyal\nLoyal\nLoyal\nLoyal\nPercival\nMerlin\n\nBad:\nMorgana\nAssassin\nMordred')

                random.shuffle(avalon_roles9)
                random.shuffle(avalon_roles9)
                random.shuffle(avalon_roles9)
                random.shuffle(avalon_roles9)
                random.shuffle(avalon_roles9)

                their_index = avalon_players.index(ctx.author.mention)

                their_role = avalon_roles9[their_index]

                the_merlin_index = avalon_roles9.index("Merlin")

                the_merlin = avalon_players[the_merlin_index]

                the_morgana_index = avalon_roles9.index("Morgana")

                the_morgana = avalon_players[the_morgana_index]

                the_assassin_index = avalon_roles9.index("Assassin")

                the_assassin = avalon_players[the_assassin_index]

                the_mordred_index = avalon_roles9.index("Mordred")

                the_mordred = avalon_players[the_mordred_index]

                merlinmorganaArray = [the_merlin, the_morgana]

                the_index_zero = avalon_players.index(merlinmorganaArray[0])

                the_index_one = avalon_players.index(merlinmorganaArray[1])

                random.shuffle(merlinmorganaArray)
                random.shuffle(merlinmorganaArray)
                random.shuffle(merlinmorganaArray)
                random.shuffle(merlinmorganaArray)
                random.shuffle(merlinmorganaArray)

                if their_role == 'Loyal':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**Nothing else**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Percival':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**One of {merlinmorganaArray[0]} (Index Number: {the_index_zero}) and {merlinmorganaArray[1]} (Index Number: {the_index_one}) is the Merlin, the other is the Morgana**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Merlin':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**Some of the bad people are:\n{the_morgana} (Index Number: {the_morgana_index})\n{the_assassin} (Index Number: {the_assassin_index})\nThere is another bad person called the Mordred but you do not know who they are**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Morgana':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_assassin} (Index Number: {the_assassin_index}) who is the Assassin\n{the_mordred} (Index Number: {the_mordred_index}) who is the Mordred**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Assassin':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_morgana} (Index Number: {the_morgana_index}) who is the Morgana\n{the_mordred} (Index Number: {the_mordred_index}) who is the Mordred**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Mordred':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_morgana} (Index Number: {the_morgana_index}) who is the Morgana\n{the_assassin} (Index Number: {the_assassin_index}) who is the Assassin**\n\nPlease also note your index number which is **{their_index}**'
                await ctx.author.send(f'>>> {long_message}')

                for name in avalon_players:
                    temp_index = avalon_players.index(name)
                    if avalon_roles9[temp_index] == "Morgana" or avalon_roles5[temp_index] == "Assassin" or avalon_roles5[temp_index] == "Mordred":
                        bad_team.append(name)
                    else:
                        good_team.append(name)

                merlin_final_index = avalon_roles9.index("Merlin")
                merlin_final = avalon_players[merlin_final_index]
                the_game_merlin.append(merlin_final)


            elif len(avalon_players) == 10:


                await ctx.author.send(
                    f'>>> The roles are\n\nGood:\nLoyal\nLoyal\nLoyal\nLoyal\nPercival\nMerlin\n\nBad:\nMorgana\nAssassin\nMordred\nLackey')

                random.shuffle(avalon_roles10)
                random.shuffle(avalon_roles10)
                random.shuffle(avalon_roles10)
                random.shuffle(avalon_roles10)
                random.shuffle(avalon_roles10)

                their_index = avalon_players.index(ctx.author.mention)

                their_role = avalon_roles10[their_index]

                the_merlin_index = avalon_roles10.index("Merlin")

                the_merlin = avalon_players[the_merlin_index]

                the_morgana_index = avalon_roles10.index("Morgana")

                the_morgana = avalon_players[the_morgana_index]

                the_assassin_index = avalon_roles10.index("Assassin")

                the_assassin = avalon_players[the_assassin_index]

                the_mordred_index = avalon_roles10.index("Mordred")

                the_mordred = avalon_players[the_mordred_index]

                the_lackey_index = avalon_roles10.index("Lackey")

                the_lackey = avalon_players[the_lackey_index]

                merlinmorganaArray = [the_merlin, the_morgana]

                the_index_zero = avalon_players.index(merlinmorganaArray[0])

                the_index_one = avalon_players.index(merlinmorganaArray[1])

                random.shuffle(merlinmorganaArray)
                random.shuffle(merlinmorganaArray)
                random.shuffle(merlinmorganaArray)
                random.shuffle(merlinmorganaArray)
                random.shuffle(merlinmorganaArray)

                if their_role == 'Loyal':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**Nothing else**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Percival':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**One of {merlinmorganaArray[0]} (Index Number: {the_index_zero}) and {merlinmorganaArray[1]} (Index Number: {the_index_one}) is the Merlin, the other is the Morgana**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Merlin':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Good**\n\nAdditionally you know:\n\n**Some of the bad people are:\n{the_morgana} (Index Number: {the_morgana_index})\n{the_assassin} (Index Number: {the_assassin_index})\n{the_lackey} (Index Number: {the_lackey_index})\nThere is another bad person called the Mordred but you do not know who they are**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Morgana':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_assassin} (Index Number: {the_assassin_index}) who is the Assassin\n{the_mordred} (Index Number: {the_mordred_index}) who is the Mordred\n{the_lackey} (Index Number: {the_lackey_index}) who is the Lackey**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Assassin':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_morgana} (Index Number: {the_morgana_index}) who is the Morgana\n{the_mordred} (Index Number: {the_mordred_index}) who is the Mordred\n{the_lackey} (Index Number: {the_lackey_index}) who is the Lackey**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Mordred':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_morgana} (Index Number: {the_morgana_index}) who is the Morgana\n{the_assassin} (Index Number: {the_assassin_index}) who is the Assassin\n{the_lackey} (Index Number: {the_lackey_index}) who is the Lackey**\n\nPlease also note your index number which is **{their_index}**'
                elif their_role == 'Lackey':
                    long_message = f'Your role:\n\n**{their_role}**\n\nYour alliance:\n\n**Bad**\n\nAdditionally you know:\n\n**Including yourself, the other bad people are:\n{the_morgana} (Index Number: {the_morgana_index}) who is the Morgana\n{the_assassin} (Index Number: {the_assassin_index}) who is the Assassin\n{the_mordred} (Index Number: {the_mordred_index}) who is the Mordred**\n\nPlease also note your index number which is **{their_index}**'
                await ctx.author.send(f'>>> {long_message}')

                for name in avalon_players:
                    temp_index = avalon_players.index(name)
                    if avalon_roles10[temp_index] == "Morgana" or avalon_roles5[temp_index] == "Assassin" or avalon_roles5[temp_index] == "Mordred" or avalon_roles5[temp_index] == "Lackey":
                        bad_team.append(name)
                    else:
                        good_team.append(name)

                merlin_final_index = avalon_roles10.index("Merlin")
                merlin_final = avalon_players[merlin_final_index]
                the_game_merlin.append(merlin_final)

        elif len(game_phase) < 1:
            await ctx.send(f'>>> {ctx.author.mention} Avalon matchmaking is not finished yet...')


@client.command(help="Type .avalon commands for more information about this command",aliases=['c'])
async def choose(ctx, *, response):

    if len(game_phase) != 1:
        await ctx.send(f"This command is invalid for now {ctx.author.mention}")
        return

    if current_person[0] != ctx.author.mention:
        await ctx.send(f"It is currently not your turn {ctx.author.mention}")
        return

    temp = response.split()

    y_axis = len(avalon_players) - 5
    x_axis = len(round_phase)


    some_message = ""

    for things in temp:

        mission_participants.append(things)
        some_message = some_message + f"{things}\n"

    people_needed = rounds_array[y_axis][x_axis]

    if (len(temp) == people_needed) and hammer_person[0] == current_person[0]:
        game_phase.append(0)
        await ctx.send(f">>> {some_message}\nhave been chosen for this mission. Direct-message the bot whether you want to pass or fail the mission by typing **.avalon pass** or **.avalon fail**")
        return

    elif (len(temp) == people_needed):
        await ctx.send(f">>> {some_message}\nhave been chosen for this mission. Click on the green tick to allow the mission to go through or click the red cross to stop this mission from going through")
    else:
        await ctx.send(f"Sorry... You entered the wrong number of people {ctx.author.mention}...")
        mission_participants.clear()
        return

    big_message = f">>> {some_message}\nhave been chosen for this mission. Click on the green tick to allow the mission to go through or click the red cross to stop this mission from going through"
    reaction_message.append(big_message)

    message = reaction_message[0]
    emoji1 = '✅'
    emoji2 = '❌'

    await message.add_reaction(emoji1)
    await message.add_reaction(emoji2)

@client.command(help="Type .avalon commands for more information about this command",aliases=['l'])
async def lady(ctx, response):
    if len(lady_use) < 1:
        if ctx.author.mention == lady_person:
            if len(game_phase) >= 2:
                for people in good_team:
                    if people == response:
                        await ctx.author.send(f">>> {response} is good")
                        lady_person.remove(0)
                        lady_person.append(response)
                        lady_use.append(0)
                        await ctx.send(f"{response} now has the lady of the lake")
                        return

                for people in good_team:
                    if people == response:
                        await ctx.author.send(f">>> {response} is bad")
                        lady_person.remove(0)
                        lady_person.append(response)
                        lady_use.append(0)
                        await ctx.send(f"{response} now has the lady of the lake")
                        return

                await ctx.author.send(f">>> An error has occurred ")
                return

            else:
                await ctx.send("You can only use the lady of the lake after the end of round two...")
                return

        else:
            await ctx.send("You do not have the lady of the lake")
    else:
        await ctx.send("The lady of the lake has already been used this round")


@client.command(help="Type .avalon commands for more information about this command",aliases=['m'])
async def merlin(ctx, response):


    if response == the_game_merlin[0]:
        await ctx.send(f"The bad people win. Congrats {bad_team}")

        avalon_players.clear()
        bad_team.clear()
        good_team.clear()
        round_phase.clear()
        game_phase.clear()
        good_score.clear()
        bad_score.clear()
        current_person.clear()
        current_person_index.clear()
        hammer_person.clear()
        lady_person.clear()
        lady_use.clear()
        yes_count.clear()
        no_count.clear()
        mission_participants.clear()
        mission_has_voted.clear()
        fail_votes.clear()
        the_game_merlin.clear()
        reaction_message.clear()



    else:
        await ctx.send(f"The good people win. Congrats {good_team}. The merlin was{the_game_merlin[0]}")

        avalon_players.clear()
        bad_team.clear()
        good_team.clear()
        round_phase.clear()
        game_phase.clear()
        good_score.clear()
        bad_score.clear()
        current_person.clear()
        current_person_index.clear()
        hammer_person.clear()
        lady_person.clear()
        lady_use.clear()
        yes_count.clear()
        no_count.clear()
        mission_participants.clear()
        mission_has_voted.clear()
        fail_votes.clear()
        the_game_merlin.clear()
        reaction_message.clear()





@client.event
async def on_reaction_add(reaction,user):
    emoji1 = '✅'
    emoji2 = '❌'
    channel = reaction.message.channel

    if len(game_phase) == 0:
        return

    if reaction.message.content == reaction_message[0]:
        the_message = reaction.message.content

        await the_message.add_reaction(emoji1)
        await the_message.add_reaction(emoji2)


    if user == client.user:
        return


    if len(game_phase) != 1:
        await channel.send("Voting is not currently available right now")
        return


    if reaction.message.content != reaction_message[0]:
        return

    if reaction.emoji == emoji1:
        await channel.send(f'{user.name} has added {reaction.emoji} to the message "{reaction.message.content}"')
        yes_count.append(0)


    elif reaction.emoji == emoji2:
        await channel.send(f'{user.name} has added {reaction.emoji} to the message "{reaction.message.content}"')
        no_count.append(0)

    if len(no_count) >= math.ceil(float(len(avalon_players)) / float(2.0)):
        await channel.send(">>> Please let the next person decide who goes on a mission")
        mission_participants.clear()
        yes_count.clear()
        no_count.clear()
        reaction_message.clear()

        if current_person_index[0] - 1 < 0:
            leftovers = current_person_index[0] - 1
            current_person_index.clear()
            current_person.clear()
            current_person_index.append(len(avalon_players) + leftovers)
            current_person.append(avalon_players[len(avalon_players) + leftovers])
        elif current_person_index[0] - 1 >= 0:
            index_temp = current_person_index[0] - 1
            current_person_index.clear()
            current_person.clear()
            current_person_index.append(index_temp)
            current_person.append(avalon_players[index_temp])






        if current_person[0] == hammer_person[0]:

            await channel.send(f"{hammer_person} gets to decide who goes on the mission. Choose the people you want to go on the mission. Type **.choose @person(1) @person(2) ... @person(n-1) @person(n)**")
            reaction_message.clear()

            if current_person_index[0] - 1 < 0:
                leftovers = current_person_index[0] - 1
                current_person_index.clear()
                current_person.clear()
                current_person_index.append(len(avalon_players) + leftovers)
                current_person.append(avalon_players[len(avalon_players) + leftovers])

            elif current_person_index[0] - 1 >= 0:
                index_temp = current_person_index[0] - 1
                current_person_index.clear()
                current_person.clear()
                current_person_index.append(index_temp)
                current_person.append(avalon_players[index_temp])

            hammer_person.clear()
            if current_person_index[0] - 4 < 0:
                leftovers = current_person_index[0] - 4
                final_hammer_index = len(avalon_players) + leftovers
                hammer_person.append(final_hammer_index)
            else:
                final_hammer_index = current_person_index[0] - 4
                hammer_person.append(final_hammer_index)

        return

    elif len(yes_count) >= math.ceil( float(float(len(avalon_players) ) + float(1.0) ) / float(2.0)):
        await channel.send(f">>> This mission will go through\n\n{mission_participants}, direct-message the bot your vote, type **avalon pass** to pass te mission or **avalon fail** to fail the mission")
        yes_count.clear()
        no_count.clear()
        game_phase.append(0)
        reaction_message.clear()

        if current_person_index[0] - 1 < 0:
            leftovers = current_person_index[0] - 1
            current_person_index.clear()
            current_person.clear()
            current_person_index.append(len(avalon_players) + leftovers)
            current_person.append(avalon_players[len(avalon_players) + leftovers])

        elif current_person_index[0] - 1 >= 0:
            index_temp = current_person_index[0] - 1
            current_person_index.clear()
            current_person.clear()
            current_person_index.append(index_temp)
            current_person.append(avalon_players[index_temp])

        hammer_person.clear()
        if current_person_index[0] - 4 < 0:
            leftovers = current_person_index[0] - 4
            final_hammer_index = len(avalon_players) + leftovers
            hammer_person.append(final_hammer_index)
        else:
            final_hammer_index = current_person_index[0] - 4
            hammer_person.append(final_hammer_index)

        return


@client.event
async def on_reaction_remove(reaction,user):
    emoji1 = '✅'
    emoji2 = '❌'
    channel = reaction.message.channel

    if reaction.message.content == reaction_message[0]:

        the_message = reaction.message.content

        await the_message.add_reaction(emoji1)
        await the_message.add_reaction(emoji2)

    if user == client.user:
        return

    if len(game_phase) != 1:
        await channel.send("Voting is not currently available right now")
        return

    if reaction.message.content != reaction_message[0]:
        return

    if reaction.emoji == emoji1:
        await channel.send(f'{user.name} has removed {reaction.emoji} from the message "{reaction.message.content}"')
        yes_count.remove(0)

    elif reaction.emoji == emoji2:
        await channel.send(f'{user.name} has removed {reaction.emoji} from the message "{reaction.message.content}"')
        no_count.remove(0)


# Idol Quest

iq_players = []
@client.command(help="Type .idolquest commands for more information about this command",aliases=['iq'])
async def idolquest(ctx, response):
    if response == 'commands':
        await ctx.send("```css\n\n.idolquest begin - Uploads yourself into the Idol Quest Database. Do this first if you want to play Idol Quest\n\n.idolquest compete - Compete against the top kpop idols to gain points\n\n.idolquest improvelist - See whether you have enough points to improve your various talents\n\n.improve {skill} - Use your points to improve your talent (For example, type .improve dancing)```")
        return
    elif response == 'begin':
        f = open('idolquest.txt','r')
        their_username = []
        for entry in f:

            temp = entry.split()
            their_username.append(temp[0])
        f.close()

        for name in their_username:
            if name == ctx.author.mention:
                await ctx.send(">>> You have already started your quest. You can type **.idolquest compete** to showcase your talents")
                return
        f = open('idolquest.txt','a')

        long_message = f'\n{ctx.author.mention} 0 1 1 1 1'
        f.write(long_message)

        f.close()
        await ctx.send(f'>>> Want to become the most talented idol?\n\nYour journey starts here\n\nWelcome {ctx.author.mention} to Idol Quest\n\nType **.idolquest compete** to start your journey')

    elif response == 'improvelist':
        f = open('idolquest.txt', 'r')
        their_username = []
        their_points = []
        their_singing = []
        their_dancing = []
        their_acting = []
        their_variety = []
        for entry in f:
            temp = entry.split()
            their_username.append(temp[0])
            their_points.append(temp[1])
            their_singing.append(temp[2])
            their_dancing.append(temp[3])
            their_acting.append(temp[4])
            their_variety.append(temp[5])
        f.close()
        important_index = 0
        for name in their_username:
            if name == ctx.author.mention:
                await ctx.send(f">>> **Welcome to the SadBot Entertainment Training Facility {ctx.author.mention}**\n\n**Your points: {their_points[important_index]}\n\nImprove singing level with 10000 points\n**Your singing level: {their_singing[important_index]}\n\n**Improve dancing level with 10000 points**\nYour dancing level: {their_dancing[important_index]}\n\n**Improve acting level with 10000 points**\nYour acting level: {their_acting[important_index]}\n\n**Improve variety level with 10000 points**\nYour variety level: {their_variety[important_index]}\n\nType **.improve singing** if you want to improve your singing. Likewise with the other skills. Note the lower case of the first letter of the skill. This command is case sensitive")
            else:
                important_index = important_index + 1

    elif response == 'compete':
        for people in iq_players:
            if people == ctx.author.mention:
                await ctx.send('You are already competing...')
                return
        iq_players.append(ctx.author.mention)

        f = open('idolquest.txt', 'r')
        their_username = []
        their_points = []
        their_singing = []
        their_dancing = []
        their_acting = []
        their_variety = []
        count = 0
        for entry in f:
            temp = entry.split()
            their_username.append(temp[0])
            their_points.append(temp[1])
            their_singing.append(temp[2])
            their_dancing.append(temp[3])
            their_acting.append(temp[4])
            their_variety.append(temp[5])
            count = count + 1
        f.close()
        index = 0

        for name in their_username:
            if name == ctx.author.mention:

                threshold = randint(1, 100)
                if int(their_singing[index]) >= threshold:
                    singingBoost = 1.5
                else:
                    singingBoost = 1

                if int(their_dancing[index]) >= threshold:
                    dancingBoost = 2.5
                else:
                    dancingBoost = 2

                if int(their_acting[index]) >= threshold:
                    actingBoost = 0.5
                else:
                    actingBoost = 1

                if int(their_variety[index]) >= threshold:
                    varietyBoost = 1.5
                else:
                    varietyBoost = 2

                yourScore = randint(10 * singingBoost, 10 * dancingBoost)
                oppScore = randint(10 * actingBoost, 10 * varietyBoost)

                kpopfile = open("kpop.txt", "r")
                theirGroup = []
                theirName = []
                theirPhoto = []

                for x in kpopfile:
                    temp = x.split()
                    theirGroup.append(temp[0])
                    theirName.append(temp[1])
                    theirPhoto.append(temp[2])

                kpopfile.close()
                # 163 kpop idols in txt file jan 24 2020
                theIndex = randint(0, 162)
                group_name = theirGroup[theIndex]
                member_name = theirName[theIndex]

                if yourScore > oppScore:

                    extra_bonus = randint(2, 4)
                    if extra_bonus == 2:
                        extra_message = 'Bonus Points:\nParticipation + 1\nWinning + 1'
                    elif extra_bonus == 3:
                        extra_message = 'Bonus Points:\nParticipation + 1\nWinning + 1\nStanding Ovation + 1'
                    elif extra_bonus == 4:
                        extra_message = f'Bonus Points:\nParticipation + 1\nWinning + 1\nStanding Ovation + 1\nCritical Acclaim + 1'

                    m0 = await ctx.send(f'>>> Competing against {group_name} {member_name}...\n{theirPhoto[theIndex]}\n\n')
                    m1 = await ctx.send(
                        f'>>> Congratulations {ctx.author.mention}, you won against {group_name} {member_name}\n\n{extra_message}\n\nTotal Points: {str(int(their_points[index]) + extra_bonus)}')

                    f = open('idolquest.txt', 'w')
                    big_message = f'{ctx.author.mention} {str(int(their_points[index]) + extra_bonus)} {their_singing[index]} {their_dancing[index]} {their_acting[index]} {their_variety[index]}'
                    f.write(big_message)

                    for values in range(count):
                        if ctx.author.mention != their_username[values]:
                            long_message = f'{their_username[values]} {their_points[values]} {their_singing[values]} {their_dancing[values]} {their_acting[values]} {their_variety[values]}'
                            f.write(f'\n{long_message}')

                    f.close()
                else:

                    participation_bonus = 1
                    m0 = await ctx.send(f'>>> Competing against {group_name} {member_name}...\n{theirPhoto[theIndex]}\n\n')
                    m1 = await ctx.send(
                        f'>>> {group_name} {member_name} has won. Sorry {ctx.author.mention}\n\nBonus Points:\nParticipation + 1\n\nTotal Points: {str(int(their_points[index]) + participation_bonus)}')

                    f = open('idolquest.txt', 'w')
                    big_message = f'{ctx.author.mention} {str(int(their_points[index]) + participation_bonus)} {their_singing[index]} {their_dancing[index]} {their_acting[index]} {their_variety[index]}'
                    f.write(big_message)
                    for values in range(count):
                        if ctx.author.mention != their_username[values]:
                            long_message = f'{their_username[values]} {their_points[values]} {their_singing[values]} {their_dancing[values]} {their_acting[values]} {their_variety[values]}'
                            f.write(f'\n{long_message}')
                    f.close()
            else:
                index = index + 1

        if ctx.author.mention not in their_username:
            await ctx.send("You have not added your details to the database. Add yourself by typing **.idolquest begin**")
            return

        await asyncio.sleep(5)
        while True:
            f = open('idolquest.txt', 'r')
            their_username = []
            their_points = []
            their_singing = []
            their_dancing = []
            their_acting = []
            their_variety = []
            count = 0
            for entry in f:
                temp = entry.split()
                their_username.append(temp[0])
                their_points.append(temp[1])
                their_singing.append(temp[2])
                their_dancing.append(temp[3])
                their_acting.append(temp[4])
                their_variety.append(temp[5])
                count = count + 1
            f.close()
            index = 0

            for name in their_username:
                if name == ctx.author.mention:

                    threshold = randint(1,100)
                    if int(their_singing[index]) >= threshold:
                        singingBoost = 1.5
                    else:
                        singingBoost = 1

                    if int(their_dancing[index]) >= threshold:
                        dancingBoost = 2.5
                    else:
                        dancingBoost = 2

                    if int(their_acting[index]) >= threshold:
                        actingBoost = 0.5
                    else:
                        actingBoost = 1

                    if int(their_variety[index]) >= threshold:
                        varietyBoost = 1.5
                    else:
                        varietyBoost = 2

                    yourScore = randint(10*singingBoost, 10*dancingBoost)
                    oppScore = randint(10*actingBoost, 10*varietyBoost)

                    kpopfile = open("kpop.txt", "r")
                    theirGroup = []
                    theirName = []
                    theirPhoto = []

                    for x in kpopfile:
                        temp = x.split()
                        theirGroup.append(temp[0])
                        theirName.append(temp[1])
                        theirPhoto.append(temp[2])

                    kpopfile.close()
                    # 163 kpop idols in txt file jan 24 2020
                    theIndex = randint(0, 162)
                    group_name = theirGroup[theIndex]
                    member_name = theirName[theIndex]

                    if yourScore > oppScore:

                        extra_bonus = randint(2,4)
                        if extra_bonus == 2:
                            extra_message = 'Bonus Points:\nParticipation + 1\nWinning + 1'
                        elif extra_bonus == 3:
                            extra_message = 'Bonus Points:\nParticipation + 1\nWinning + 1\nStanding Ovation + 1'
                        elif extra_bonus == 4:
                            extra_message = f'Bonus Points:\nParticipation + 1\nWinning + 1\nStanding Ovation + 1\nCritical Acclaim + 1'

                        await m0.edit(content=f'>>> Competing against {group_name} {member_name}...\n{theirPhoto[theIndex]}\n\n')
                        await m1.edit(content=f'>>> Congratulations {ctx.author.mention}, you won against {group_name} {member_name}\n\n{extra_message}\n\nTotal Points: {str(int(their_points[index]) + extra_bonus)}')

                        f = open('idolquest.txt', 'w')
                        big_message = f'{ctx.author.mention} {str(int(their_points[index]) + extra_bonus )} {their_singing[index]} {their_dancing[index]} {their_acting[index]} {their_variety[index]}'
                        f.write(big_message)

                        for values in range(count):
                            if ctx.author.mention != their_username[values]:
                                long_message = f'{their_username[values]} {their_points[values]} {their_singing[values]} {their_dancing[values]} {their_acting[values]} {their_variety[values]}'
                                f.write(f'\n{long_message}')
                        f.close()
                        await asyncio.sleep(5)
                    else:

                        participation_bonus = 1
                        await m0.edit(content=f'>>> Competing against {group_name} {member_name}...\n{theirPhoto[theIndex]}\n\n')
                        await m1.edit(content=f'>>> {group_name} {member_name} has won. Sorry {ctx.author.mention}\n\nBonus Points:\nParticipation + 1\n\nTotal Points: {str(int(their_points[index]) + participation_bonus)}')

                        f = open('idolquest.txt', 'w')
                        big_message = f'{ctx.author.mention} {str(int(their_points[index]) + participation_bonus )} {their_singing[index]} {their_dancing[index]} {their_acting[index]} {their_variety[index]}'
                        f.write(big_message)

                        for values in range(count):

                            if ctx.author.mention != their_username[values]:
                                long_message = f'{their_username[values]} {their_points[values]} {their_singing[values]} {their_dancing[values]} {their_acting[values]} {their_variety[values]}'

                                f.write(f'\n{long_message}')

                        f.close()
                        await asyncio.sleep(5)
                else:
                    index = index + 1


@client.command(help="Type .idolquest commands for more information about this command")
async def improve(ctx, skill):
    f = open('idolquest.txt', 'r')
    their_username = []
    their_points = []
    their_singing = []
    their_dancing = []
    their_acting = []
    their_variety = []
    count = 0
    for entry in f:
        temp = entry.split()
        their_username.append(temp[0])
        their_points.append(temp[1])
        their_singing.append(temp[2])
        their_dancing.append(temp[3])
        their_acting.append(temp[4])
        their_variety.append(temp[5])
        count = count + 1
    f.close()
    index = 0
    for name in their_username:
        if name == ctx.author.mention:

            if skill == 'singing' and int(their_points[index]) >= 10000:
                await ctx.send(f'>>> Congratulations {ctx.author.mention}, you have improved your singing to level {str(int(their_singing[index]) + 1)}')
                f = open('idolquest.txt','w')
                big_message = f'{ctx.author.mention} {str(int(their_points[index]) - 10000)} {str(int(their_singing[index]) + 1)} {their_dancing[index]} {their_acting[index]} {their_variety[index]}'
                f.write(big_message)
                for values in range(count):
                    if ctx.author.mention != their_username[values]:
                        long_message = f'{their_username[values]} {their_points[values]} {their_singing[values]} {their_dancing[values]} {their_acting[values]} {their_variety[values]}'
                        f.write(f'\n{long_message}')
                f.close()

            elif skill == 'dancing' and int(their_points[index]) >= 10000:
                await ctx.send(f'>>> Congratulations {ctx.author.mention}, you have improved your dancing to level {str(int(their_dancing[index]) + 1)}')
                f = open('idolquest.txt', 'w')
                big_message = f'{ctx.author.mention} {str(int(their_points[index]) - 10000)} {their_singing[index]} {str(int(their_dancing[index]) + 1)} {their_acting[index]} {their_variety[index]}'
                f.write(big_message)
                for values in range(count):
                    if ctx.author.mention != their_username[values]:
                        long_message = f'{their_username[values]} {their_points[values]} {their_singing[values]} {their_dancing[values]} {their_acting[values]} {their_variety[values]}'
                        f.write(f'\n{long_message}')
                f.close()
            elif skill == 'acting' and int(their_points[index]) >= 10000:
                await ctx.send(f'>>> Congratulations {ctx.author.mention}, you have improved your acting to level {str(int(their_acting[index]) + 1)}')
                f = open('idolquest.txt', 'w')
                big_message = f'{ctx.author.mention} {str(int(their_points[index]) - 10000)} {their_singing[index]} {their_dancing[index]} {str(int(their_acting[index]) + 1)} {their_variety[index]}'
                f.write(big_message)
                for values in range(count):
                    if ctx.author.mention != their_username[values]:
                        long_message = f'{their_username[values]} {their_points[values]} {their_singing[values]} {their_dancing[values]} {their_acting[values]} {their_variety[values]}'
                        f.write(f'\n{long_message}')
                f.close()
            elif skill == 'variety' and int(their_points[index]) >= 10000:
                await ctx.send(f'>>> Congratulations {ctx.author.mention}, you have improved your variety to level {str(int(their_variety[index]) + 1)}')
                f = open('idolquest.txt', 'w')
                big_message = f'{ctx.author.mention} {str(int(their_points[index]) - 10000)} {their_singing[index]} {their_dancing[index]} {their_acting[index]} {str(int(their_variety[index]) + 1)}'
                f.write(big_message)
                for values in range(count):
                    if ctx.author.mention != their_username[values]:
                        long_message = f'{their_username[values]} {their_points[values]} {their_singing[values]} {their_dancing[values]} {their_acting[values]} {their_variety[values]}'
                        f.write(f'\n{long_message}')
                f.close()
            elif int(their_points[index]) < 1000 and (skill == 'singing' or skill == 'dancing' or skill == 'acting' or skill =='variety'):
                await ctx.send(f'>>> Sorry {ctx.author.mention}, you have insufficient talent points to improve to the next level of {skill}')
        else:
            index = index + 1

# Idol Guess

# Initialising Variables for Idol Guess

theFinalGroup = []
theFinalName = []
theFinalPhoto = []
hasStarted = []
longScore = []


@client.command(help="Type .idolguess commands for more information about this command",aliases=['ig'])
async def idolguess(ctx, guess):
    if guess == 'commands':
        await ctx.send("```css\n\n.idolguess start - Starts the game\n\n.idolguess {the name of the person} - Make your guess (For example, type .idolguess chaekyung)\n\n.idolguess skip - Skips the current idol you have to guess at the cost of one life\n\n.idolguess quit - Quits the whole game overall```")
    elif guess == 'start' and len(hasStarted) == 0:
        hasStarted.append(0)
        f = open("kpop.txt", "r")
        theirGroup = []
        theirName = []
        theirPhoto = []

        for x in f:
            temp = x.split()
            theirGroup.append(temp[0])
            theirName.append(temp[1])
            theirPhoto.append(temp[2])

        f.close()
        # 163 kpop idols in txt file feb 13 2020
        theIndex = randint(0, 162)
        theFinalGroup.append(theirGroup[theIndex])
        theFinalName.append(theirName[theIndex])
        theFinalPhoto.append(theirPhoto[theIndex])

        await ctx.send(f">>> Who is this?\n{theFinalPhoto[0]}")
        await asyncio.sleep(30)

    elif guess.lower() == theFinalName[0].lower() and len(hasStarted) != 0:

        theFinalName.clear()
        theFinalGroup.clear()
        theFinalPhoto.clear()
        longScore.append(0)


        f = open("kpop.txt", "r")
        theirGroup = []
        theirName = []
        theirPhoto = []

        for x in f:
            temp = x.split()
            theirGroup.append(temp[0])
            theirName.append(temp[1])
            theirPhoto.append(temp[2])

        f.close()
        # 163 kpop idols in txt file feb 13 2020
        theIndex = randint(0, 162)
        theFinalGroup.append(theirGroup[theIndex])
        theFinalName.append(theirName[theIndex])
        theFinalPhoto.append(theirPhoto[theIndex])

        await ctx.send(f">>> Current score: {len(longScore)}\n\nWho is this?\n{theFinalPhoto[0]}")

    elif ( (guess.lower() != theFinalName[0].lower()  )  or (guess.lower() == 'skip') ) and len(hasStarted) != 0 and guess.lower() != 'quit' and guess.lower() != 'start':
        hasStarted.append(0)

        await ctx.send(f">>> Sorry, the answer was {theFinalName[0]} from {theFinalGroup[0]} ")

        if len(hasStarted) == 4:
            await ctx.send(f">>> You have lost...\n\nFinal score: {len(longScore)}")
            theFinalName.clear()
            theFinalGroup.clear()
            theFinalPhoto.clear()
            hasStarted.clear()
            longScore.clear()
            return

        await ctx.send(f">>> Lives remaining: {4 - len(hasStarted)}  ")
        theFinalName.clear()
        theFinalGroup.clear()
        theFinalPhoto.clear()

        f = open("kpop.txt", "r")
        theirGroup = []
        theirName = []
        theirPhoto = []

        for x in f:
            temp = x.split()
            theirGroup.append(temp[0])
            theirName.append(temp[1])
            theirPhoto.append(temp[2])


        f.close()
        # 163 kpop idols in txt file feb 13 2020
        theIndex = randint(0, 156)
        theFinalGroup.append(theirGroup[theIndex])
        theFinalName.append(theirName[theIndex])
        theFinalPhoto.append(theirPhoto[theIndex])

        await ctx.send(f">>> Current score: {len(longScore)}\n\nWho is this?\n{theFinalPhoto[0]}")

    elif guess.lower() == 'quit':
        await ctx.send(f">>> You have lost...\nThe answer was {theFinalName[0]} from {theFinalGroup[0]}\n\nFinal score: {len(longScore)}")
        theFinalName.clear()
        theFinalGroup.clear()
        theFinalPhoto.clear()
        hasStarted.clear()
        longScore.clear()

    else:
        await ctx.send(f">>> Sorry, that command is invalid for now...")

# Music Quiz

# Some commands just in case of technical difficulties with joining and/or leaving voice channels

@client.command(help="Makes the bot join the same voice channel you are in")
async def join(ctx):

    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await ctx.send(f"Joined {channel}")

@client.command(help="Makes the bot leave the same voice channel you are in")
async def leave(ctx):

    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send(f"Left {channel}")
    else:
        await ctx.send("Don't think I am in a voice channel")

# Initialising variables for the music quiz

music_quiz_status = []
music_quiz_score = []
music_quiz_lives = []
the_final_url = []
the_final_song_name = []


@client.command(help="Type .musicquiz commands for more information about this command",aliases=['mq'])
async def musicquiz(ctx, *, their_guess):

    if their_guess == 'commands':
        await ctx.send("```css\n\nRemember you have to join a voice channel first before using the commands\n\n.mq start - starts the music quiz game\n\n.mq {your guess} - This is how you guess the song. (For example, type .mq Bouncy)```")
        return

    elif their_guess == 'start':

        global voice

        channel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        await ctx.send(f">>> Joined {channel}")

        music_quiz_status.append(0)

        f = open("musicquiz.txt", "r")
        all_links = []
        all_names = []

        for x in f:
            temp = x.split()
            all_links.append(temp[0])
            temp.remove(temp[0])
            final_message = ""
            for item in temp:
                if item == temp[0]:
                    item = str(item)
                    final_message = final_message + item
                else:
                    item = str(item)
                    final_message = final_message + " " + item
            all_names.append(final_message)

        f.close()
        # 3 songs 2020
        theIndex = randint(0, 2)
        the_final_url.append(all_links[theIndex])
        the_final_song_name.append(all_names[theIndex])

        song_there = os.path.isfile("song.mp3")

        try:
            if song_there:
                os.remove("song.mp3")
                print("Removed old song file")
        except PermissionError:
            print("tried to delete song file but is being played")
            await ctx.send(">>> Error: Music Playing")
            return

        await ctx.send(">>> Getting everything ready now...\n\nNote: If you dont guess a song within 3 minutes, you will be disqualified...")

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([the_final_url[0]])

        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                name = file
                print(f"Renamed File: {file}\n")
                os.rename(file,"song.mp3")

        voice.play(discord.FFmpegPCMAudio("song.mp3"),after=lambda e: print(f"{name} has finished playing") )
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.07

        print("playing\n")
        await ctx.send(">>> What is the name of this song?")

        await asyncio.sleep(180)

        if voice and voice.is_playing():
            voice.stop()

            await ctx.send(f">>> You are disqualified {ctx.author.mention} since you have not made a guess in 3 minutes. the song was {the_final_song_name[0]}\n\nYour score: {len(music_quiz_score)}")

            music_quiz_status.clear()
            music_quiz_score.clear()
            music_quiz_lives.clear()
            the_final_url.clear()
            the_final_song_name.clear()

            voice = get(client.voice_clients, guild=ctx.guild)

            if voice and voice.is_connected():
                await voice.disconnect()

            return

    elif str(their_guess.lower()) == str(the_final_song_name[0].lower()):
        music_quiz_score.append(0)
        the_final_url.clear()
        the_final_song_name.clear()
        await ctx.send(f"You are correct {ctx.author.mention}\n\nYour score: {len(music_quiz_score)}")

        f = open("musicquiz.txt", "r")
        all_links = []
        all_names = []

        for x in f:
            temp = x.split()
            all_links.append(temp[0])
            temp.remove(temp[0])
            final_message = ""
            for item in temp:
                if item == temp[0]:
                    item = str(item)
                    final_message = final_message + item
                else:
                    item = str(item)
                    final_message = final_message + " " + item
            all_names.append(final_message)

        f.close()
        # 3 songs 2020
        theIndex = randint(0, 2)
        the_final_url.append(all_links[theIndex])
        the_final_song_name.append(all_names[theIndex])

        channel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)

        if voice and voice.is_playing():
            voice.stop()
            await voice.disconnect()

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        song_there = os.path.isfile("song.mp3")

        try:
            if song_there:
                os.remove("song.mp3")
                print("Removed old song file")
        except PermissionError:
            print("tried to delete song file but is being played")
            await ctx.send(">>> Error: Music Playing")
            return

        await ctx.send(">>> Getting everything ready now...")

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([the_final_url[0]])

        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                name = file
                print(f"Renamed File: {file}\n")
                os.rename(file, "song.mp3")

        voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print(f"{name} has finished playing"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.07


        print("playing\n")
        await ctx.send(">>> What is the name of this song?")

        await asyncio.sleep(180)

        if voice and voice.is_playing():
            voice.stop()


            await ctx.send(f">>> You are disqualified {ctx.author.mention} since you have not made a guess in 3 minutes. the song was {the_final_song_name[0]}\n\nYour score: {len(music_quiz_score)}")

            music_quiz_status.clear()
            music_quiz_score.clear()
            music_quiz_lives.clear()
            the_final_url.clear()
            the_final_song_name.clear()

            voice = get(client.voice_clients, guild=ctx.guild)

            if voice and voice.is_connected():
                await voice.disconnect()
            return

    elif str(their_guess.lower()) != str(the_final_song_name[0].lower()):
        await ctx.send(f">>> You are incorrect {ctx.author.mention}\n\n The answer was {the_final_song_name[0]}")

        music_quiz_lives.append(0)
        the_final_url.clear()
        the_final_song_name.clear()

        if len(music_quiz_lives) >= 3:
            await ctx.send(f">>> Game over {ctx.author.mention}...\n\nYour score: {len(music_quiz_score)}")

            music_quiz_status.clear()
            music_quiz_score.clear()
            music_quiz_lives.clear()

            voice = get(client.voice_clients, guild=ctx.guild)

            if voice and voice.is_connected():
                await voice.disconnect()

            return

        f = open("musicquiz.txt", "r")
        all_links = []
        all_names = []

        for x in f:
            temp = x.split()
            all_links.append(temp[0])
            temp.remove(temp[0])
            final_message = ""
            for item in temp:
                if item == temp[0]:
                    item = str(item)
                    final_message = final_message + item
                else:
                    item = str(item)
                    final_message = final_message + " " + item
            all_names.append(final_message)

        f.close()
        # 3 songs 2020
        theIndex = randint(0, 2)
        the_final_url.append(all_links[theIndex])
        the_final_song_name.append(all_names[theIndex])

        channel = ctx.message.author.voice.channel
        voice = get(client.voice_clients, guild=ctx.guild)

        if voice and voice.is_playing():
            voice.stop()
            await voice.disconnect()

        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()

        song_there = os.path.isfile("song.mp3")

        try:
            if song_there:
                os.remove("song.mp3")
                print("Removed old song file")
        except PermissionError:
            print("tried to delete song file but is being played")
            await ctx.send(">>> Error: Music Playing")
            return

        await ctx.send(">>> Getting everything ready now...")

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            print("Downloading audio now\n")
            ydl.download([the_final_url[0]])

        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                name = file
                print(f"Renamed File: {file}\n")
                os.rename(file, "song.mp3")

        voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print(f"{name} has finished playing"))
        voice.source = discord.PCMVolumeTransformer(voice.source)
        voice.source.volume = 0.07


        print("playing\n")
        await ctx.send(">>> What is the name of this song?")

        await asyncio.sleep(180)

        if voice and voice.is_playing():
            voice.stop()


            await ctx.send(f">>> You are disqualified {ctx.author.mention} since you have not made a guess in 3 minutes. the song was {the_final_song_name[0]}\n\nYour score: {len(music_quiz_score)}")

            music_quiz_status.clear()
            music_quiz_score.clear()
            music_quiz_lives.clear()
            the_final_url.clear()
            the_final_song_name.clear()

            voice = get(client.voice_clients, guild=ctx.guild)

            if voice and voice.is_connected():
                await voice.disconnect()

            return


##### End of Games #####


# Timed Messages

CHANNEL = your_channel_id_goes_here

pasta_one = '>>> Your copy pasta spam goes here'

pasta_two = '''
    
    
    >>> Your copy pasta spam goes here


'''

pasta_three = """


>>> Your copy pasta spam goes here


"""

pasta_four = ">>> Your copy pasta spam goes here"

pasta_five = ">>> Your copy pasta spam goes here"

pasta_six = ">>> Your copy pasta spam goes here"

pasta_seven = ">>> Your copy pasta spam goes here"

pasta_eight = ">>> Your copy pasta spam goes here"

pasta_nine = ">>> Your copy pasta spam goes here"

pasta_ten = ">>> Your copy pasta spam goes here"

@client.event
async def copy_pasta():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL)
    interval = 300

    while not client.is_closed():
        pastaArray = [pasta_one, pasta_two, pasta_three, pasta_four, pasta_five, pasta_six, pasta_seven, pasta_eight, pasta_nine, pasta_ten]
        await asyncio.sleep(1500)
        await channel.send(random.choice(pastaArray))
        await asyncio.sleep(interval)


@client.event
async def happy_feelings():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL)
    interval = 600

    while not client.is_closed():

        f = open("kpop.txt", "r")
        theirGroup = []
        theirName = []
        theirPhoto = []

        for x in f:
            temp = x.split()
            theirGroup.append(temp[0])
            theirName.append(temp[1])
            theirPhoto.append(temp[2])

        f.close()
        # 163 kpop idols in txt file jan 15 2020
        theIndex = randint(0, 162)
        finalGroup = theirGroup[theIndex]
        finalName = theirName[theIndex]

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

        messageTotal = f'>>> {random.choice(cheers)}\n{theirPhoto[theIndex]}'
        await asyncio.sleep(1200)
        await channel.send(messageTotal)
        await asyncio.sleep(interval)


@client.event
async def current_weather():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL)
    interval = 900

    while not client.is_closed():
        owm = pyowm.OWM('your_owm_API_goes_here')
        observation = owm.weather_at_place("your_city, your_country_abbreviation")
        w = observation.get_weather()
        temperature = w.get_temperature('celsius')
        detailed_description = w.get_detailed_status()
        cloud_coverage = w.get_clouds()
        wind = w.get_wind()
        humidity = w.get_humidity()
        pressures = w.get_pressure()
        uvi = owm.uvindex_around_coords(the_latitude_of_your_area, the_longitude_of_your_area)
        uv_level = uvi.get_value()
        exposure_risk = uvi.get_exposure_risk()
        current_time = uvi.get_reception_time(timeformat='date')

        if round(uv_level) >= 11:
            uv_message = "Extreme"
        elif round(uv_level) >= 8:
            uv_message = "Very High"
        elif round(uv_level) >= 6:
            uv_message = "High"
        elif round(uv_level) >= 3:
            uv_message = "Moderate"
        else:
            uv_message = "Low"

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

        big_message = f'>>> **Weather Forecast**    :earth_asia: \n\n**{detailed_description}**\n\n:dash: Wind Speed: {round(wind["speed"] * 1.6)} kilometres/hour {wind_direction} (@ {wind["deg"]}°)\n:thermometer_face: Current Temperature: {round(temperature["temp"])}°C, Maximum: {round(temperature["temp_max"])}°C, Minimum: {round(temperature["temp_min"])}°C\n:sweat_drops: Humidity: {humidity}% with {cloud_coverage}% cloud coverage\n:thermometer: Pressure: {pressures["press"]} hPa\n:sunny: UV Level: {round(uv_level)} ({uv_message}) with a {exposure_risk} exposure risk\n:clock: Current Time: {current_time}'
        await asyncio.sleep(900)
        await channel.send(big_message)
        await asyncio.sleep(interval)

@client.event
async def is_online():
    await client.wait_until_ready()
    channel = client.get_channel(your_channel_id_goes_here)
    interval = 3
    await channel.purge(limit=1)
    m0 = await channel.send('If the emoji is changing approximately 3 to 6 seconds, the bot is online\n\n:flushed:')

    while not client.is_closed():
        await asyncio.sleep(interval)
        emojis = [":rabbit:",":cat:",":dove:",":frog:",":deer:",":owl:",":fish:",":bat:",":swan:",":penguin:",":butterfly:",":wolf:"]
        final_choice = random.choice(emojis)
        await m0.edit(content=f'If the emoji is changing approximately 3 to 6 seconds, the bot is online\n\n{final_choice}')


client.loop.create_task(copy_pasta())
client.loop.create_task(happy_feelings())
client.loop.create_task(current_weather())
client.loop.create_task(is_online())


# Create a new trainer for the chatbot
#trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
#trainer.train("chatterbot.corpus.english")

# Train based on the english corpus
#trainer.train("chatterbot.corpus.english")

# Train based on english greetings corpus
#trainer.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
#trainer.train("chatterbot.corpus.english.conversations")


@client.command(help="Talk to sadbot about kpop",aliases=["sb"])
async def sadbot(ctx,*,input):

    # For "Chatterbot" Functionality

    chatbot = ChatBot('Sadbot')
    trainer = ListTrainer(chatbot)
    data = open('chatbot.txt').read()
    convos = data.strip().split('\n')
    trainer.train(convos)

    reply = chatbot.get_response(input)

    await ctx.send(f">>> {reply}")

    # Adds user replies to a text file for learning

    file = open('chatbot.txt', 'a')
    final_message = input + "\n"
    file.write(final_message)
    file.close()

client.run('YOUR_DISCORD_BOT_TOKEN_GOES_HERE')
