# for discord functionality

import discord
from discord.ext import commands, tasks
import asyncio

# for weather updates
import pyowm

# miscellaneous

import math
import random
from itertools import cycle
from random import randint

#
from datetime import datetime, timedelta
import time
import sched

# role assignment
from discord.ext.commands import Bot
import discord
from discord.utils import get

# Bot prefix

client = commands.Bot(command_prefix = '.')

# Token
token = YOUR_TOKEN_GOES_HERE

# For the bot's status

status = cycle(['Fiesta | Type ".commands" for the list of commands','Hands Up | Type ".commands" for the list of commands', 'Nun Nu Nan Na | Type ".commands" for the list of commands', 'Crossroads | Type ".commands" for the list of commands', 'Wish | Type ".commands" for the list of commands', 'So What | Type ".commands" for the list of commands', 'Dun Dun | Type ".commands" for the list of commands','Cool | Type ".commands" for the list of commands',  'Bouncy | Type ".commands" for the list of commands', 'Say My Name | Type ".commands" for the list of commands','Scream | Type ".commands" for the list of commands', 'My Universe | Type ".commands" for the list of commands', 'Dazzle Dazzle | Type ".commands" for the list of commands', 'Timing | Type ".commands" for the list of commands', 'Queen | Type ".commands" for the list of commands','Jackpot | Type ".commands" for the list of commands', 'Lie | Type ".commands" for the list of commands', 'Plant | Type ".commands" for the list of commands', 'VALENTi | Type ".commands" for the list of commands', 'Future | Type ".commands" for the list of commands', 'ASSA | Type ".commands" for the list of commands', 'Oh my God | Type ".commands" for the list of commands','DUMHDURUM | Type ".commands" for the list of commands','LALALILALA | Type ".commands" for the list of commands'])
@client.event
async def on_ready():
    change_status.start()
    # await client.change_presence(status=discord.Status.online, activity=discord.Game('Always Be Your Girl (너의 소녀가 되어줄게)'))
    print('Bot is ready.')
    print('We have logged in as {0.user}'.format(client))


@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


# Events that get triggered

@client.event
async def on_raw_reaction_add(payload):
    global role
    message_id = payload.message_id
    if message_id == message_id_goes_here:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if payload.emoji.name == 'sujeongconcernyoinked':
            role = discord.utils.get(guild.roles, name="Kpop Updates")
        elif payload.emoji.name == 'suyunpout':
            role = discord.utils.get(guild.roles, name="Instruction")

        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)
            else:
                print("member not found")
        else:
            print("role not found")

@client.event
async def on_raw_reaction_remove(payload):
    global role
    message_id = payload.message_id
    if message_id == message_id_goes_here:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        if payload.emoji.name == 'sujeongconcernyoinked':
            role = discord.utils.get(guild.roles, name="Kpop Updates")
        elif payload.emoji.name == 'suyunpout':
            role = discord.utils.get(guild.roles, name="Instruction")

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

    if message.author == client.user:
        return

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


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')


# Commands
@client.command(help="create general announcement")
async def generalannounce(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send(">>> @everyone")
    f = open("generalannouncement.txt", "r")
    lines = f.readlines()
    for line in lines:
        await ctx.send(f">>> {line}")


@client.command(help="create kpop announcement")
async def kpopannounce(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send(">>> <@&721507758637056102>")
    f = open("kpopannouncement.txt", "r")
    lines = f.readlines()
    for line in lines:
        await ctx.send(f">>> {line}")

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
        '```css\nGeneral Commands:\n\n.8ball {your_question} - Ask the bot a question\n\n.cheerup - Try this one if you are feeling down\n\n.conway - A Conway Game of Life Simulator\n\n.dice - Rolls die\n\n.examszn - Get some words of wisdom from the bot if you are feeling stressed for your upcoming exams\n\n.hug {@person} - Try this one on someone. This will only work if you ping the user you want to hug\n\n.isonline - Check whether the bot is online\n\n.match {person1 and person2} - Ship yourself with your crush (For example, type .match Me and Sojin)\n\n.piglatin {your message} - Convert your message to Pig Latin\n\n.ping - Checks latency\n\n.stanloona {your message} - Convert your message to let others know you really stan LOOΠΔ\n\n.weather - Get the current weather in Auckland\n\nGame Commands:\n\n.idolguess commands - Displays the Guess the Idol Game commands\n\nProfile Commands:\n\n.profile commands - Displays all of the profile commands```')


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
    await ctx.send(f'>>> Question: {question}?\nAnswer: {random.choice(responses)}')


@client.command(
    help="Ship yourself with your crush (For example, type .match Thomas and Nayeon)Displays details of Sadbot")
async def match(ctx, *, question):
    await ctx.send(f'>>> Shipping {question}...\nCompatibility: {randint(0, 100)}%')


@client.command(help="Rolls die")
async def dice(ctx):
    await ctx.send(f'>>> :game_die: **Rolls game die** :game_die:\n{randint(1, 6)}')


@client.command(help="Get some words of wisdom from the bot if you are feeling stressed for your upcoming exams")
async def examszn(ctx):
    await ctx.send(
        '>>> https://scontent.fakl6-1.fna.fbcdn.net/v/t1.15752-9/82276376_604105316813162_5652167650046902272_n.jpg?_nc_cat=110&_nc_ohc=sJgWVpNAbHAAX-17ANX&_nc_ht=scontent.fakl6-1.fna&oh=0da1366686ae449cf1c6f4a1e6f68d20&oe=5EBE1A66')


@client.command(help="Convert your message to let others know you really stan LOONA", aliases=['sl'])
async def stanloona(ctx, *, arg):
    temp = arg.split()
    big_message = ""
    for thing in temp:
        med_message = " Stan " + thing + " Loona "
        big_message = big_message + med_message
    await ctx.send(f">>> {big_message}")


@client.command(help="Convert your message to Pig Latin", aliases=['pl'])
async def piglatin(ctx, *, arg):
    temp = arg.split()
    big_message = ""
    for thing in temp:
        med_message = thing[-1] + thing[:-1] + "e"
        big_message = big_message + " " + med_message + " "
    await ctx.send(f">>> {big_message}")


online_counter = [0]


@client.command(help="Find out whether the bot is online or not", aliases=['io'])
async def isonline(ctx):
    await client.wait_until_ready()

    interval = 3
    m0 = await ctx.send('If the emoji is changing approximately 3 to 6 seconds, the bot is online\n\n:flushed:')

    await asyncio.sleep(interval)
    while not client.is_closed():
        f = '%H:%M'
        now = datetime.strftime(datetime.now(), f)
        await asyncio.sleep(interval)
        emojis = [":rabbit:",":cat:",":dove:",":frog:",":deer:",":owl:",":fish:",":bat:",":swan:",":penguin:",":butterfly:",":wolf:"]
        final_choice = random.choice(emojis)
        final_choice2 = random.choice(emojis)
        final_choice3 = random.choice(emojis)
        final_choice4 = random.choice(emojis)
        final_choice5 = random.choice(emojis)
        await m0.edit(content=f'Look at these animals :relaxed:\n\n{final_choice} {final_choice2} {final_choice3} {final_choice4} {final_choice5}')
        online_counter.append(0)
        if len(online_counter) == 5:
            await asyncio.sleep(interval)
            await m0.edit(content=f"Bot is online :relaxed:. Last updated at: {now}")
            return

cheerup_players = []
slides = [0]

@client.command(help="Try this one if you are feeling down")
async def cheerup(ctx):
    for people in cheerup_players:
        if people == ctx.author.mention:
            await ctx.send('You already have a slideshow going on...')
            return
    cheerup_players.append(ctx.author.mention)
    f = open("kpop.txt", "r")
    theirGroup = []
    theirName = []
    theirPhoto = []
    counterNumber = 0
    for x in f:
        counterNumber = counterNumber + 1
        temp = x.split()
        theirPhoto.append(temp[len(temp) - 1])
        temp.remove(temp[len(temp) - 1])
        idol_group = ""
        idol_name = ""
        count_one = []
        for item in temp:
            if item != 'ge' and len(count_one) == 0:
                idol_group = idol_group + item
                count_one.append(0)
            elif item != 'ge' and len(count_one) == 1:
                idol_group = idol_group + " " + item
            elif item == 'ge':
                count_one.append(0)
            elif len(count_one) == 2:
                idol_name = idol_name + item
                count_one.append(0)
            elif len(count_one) == 3:
                idol_name = idol_name + " " + item
        count_one.clear()

        theirGroup.append(idol_group)
        theirName.append(idol_name)

    f.close()

    theIndex = randint(0, counterNumber - 1)
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


    msg1 = await ctx.send(f">>> :blush: Here is a photo to cheer you up! :blush:\n\n")
    msg2 = await ctx.send(f'>>> {random.choice(cheers)}')
    msg3 = await ctx.send(f'{theirPhoto[theIndex]}')

    interval = 5
    await asyncio.sleep(interval)


    while not client.is_closed():
        await asyncio.sleep(interval)

        f = open("kpop.txt", "r")
        theirGroup = []
        theirName = []
        theirPhoto = []

        for x in f:
            temp = x.split()
            theirPhoto.append(temp[len(temp) - 1])
            temp.remove(temp[len(temp) - 1])
            idol_group = ""
            idol_name = ""
            count_one = []
            for item in temp:
                if item != 'ge' and len(count_one) == 0:
                    idol_group = idol_group + item
                    count_one.append(0)
                elif item != 'ge' and len(count_one) == 1:
                    idol_group = idol_group + " " + item
                elif item == 'ge':
                    count_one.append(0)
                elif len(count_one) == 2:
                    idol_name = idol_name + item
                    count_one.append(0)
                elif len(count_one) == 3:
                    idol_name = idol_name + " " + item
            count_one.clear()

            theirGroup.append(idol_group)
            theirName.append(idol_name)

        f.close()

        theIndex = randint(0, counterNumber - 1)
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


        await msg1.edit(content=f">>> :blush: Here is another photo to cheer you up! :blush:\n\n")
        await msg2.edit(content=f'>>> {random.choice(cheers)}')
        await msg3.edit(content=f'{theirPhoto[theIndex]}')
        slides.append(0)
        if len(slides) == 10:
            await ctx.send(f">>> You may start a new slideshow {ctx.author.mention}")
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
            await ctx.send('You already have a simulation going on...')
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

@client.command(help="Get a current update of the weather in Auckland",aliases=['w'])
async def weather(ctx):

    await client.wait_until_ready()

    #while not client.is_closed():
    owm = pyowm.OWM(YOUR_TOKEN_GOES_HERE)
    observation = owm.weather_at_place("Auckland, NZ")
    w = observation.get_weather()
    temperature = w.get_temperature('celsius')
    detailed_description = w.get_detailed_status().capitalize()
    cloud_coverage = w.get_clouds()
    wind = w.get_wind()
    humidity = w.get_humidity()
    pressures = w.get_pressure()
    uvi = owm.uvindex_around_coords(36.8485, 174.7633)
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

    big_message = f'>>> **Weather Forecast in Auckland, New Zealand**    :earth_asia:  :flag_nz:\n\n**{detailed_description}**\n\n:dash: Wind Speed: {round(wind["speed"] * 1.6)} kilometres/hour {wind_direction} (@ {wind["deg"]}°)\n:thermometer_face: Current Temperature: {round(temperature["temp"])}°C, Maximum: {round(temperature["temp_max"])}°C, Minimum: {round(temperature["temp_min"])}°C\n:sweat_drops: Humidity: {humidity}% with {cloud_coverage}% cloud coverage\n:thermometer: Pressure: {pressures["press"]} hPa\n:sunny: UV Level: {round(uv_level)} ({uv_message}) with a {exposure_risk} exposure risk\n:clock: Current Time: {current_time}'
    await ctx.send(big_message)

# Profile

@client.command(help="Displays your profile details",aliases=['p'])
async def profile(ctx,*,message):


    messageLength = message.split()


    if len(messageLength) == 1:
        if message.lower() == 'commands':
            await ctx.send(
                "```css\n\n.profile self - Displays your profile\n\n.profile {@user} - Displays the profile of the specified user\n\n.profile changename {Your name} - Changes what is displayed as your name in your profile\n\n.profile changedegree {Your degree and major} - Changes what is displayed as your degree and major in your profile\n\n.profile changegroups {Your favourite kpop groups} - Changes which groups are displayed as your favorite groups in your profile\n\n.profile changeidols {Your favourite idols} - Changes who is displayed as your favourite idols in your profile\n\n.profile changelistening {Who you have been listening to} - Changes which artists you have been listening to in your profile\n\n.profile changesomething {Something you want us to know} - Changes what is displayed as something you would like everyone to know in your profile```")
        elif message.lower() == 'self':
            f = open("profiles.txt", "r")

            isFound = False
            for x in f:

                temp = x.split()
                if ctx.author.mention == temp[0]:

                    isFound = True
                    count = 0
                    theirDiscordID = ""
                    name = ""
                    degreeMajor = ""
                    favGroups = ""
                    favIdols = ""
                    listeningTo = ""
                    something = ""

                    for item in temp:

                        if item == "$toP":
                            count = count + 1
                        elif count == 0:
                            theirDiscordID = theirDiscordID + " " + item
                        elif count == 1:
                            name = name + " " + item
                        elif count == 2:
                            degreeMajor = degreeMajor + " " + item
                        elif count == 3:
                            favGroups = favGroups + " " + item
                        elif count == 4:
                            favIdols = favIdols + " " + item
                        elif count == 5:
                            listeningTo = listeningTo + " " + item
                        elif count == 6:
                            something = something + " " + item
                    f.close()

                    await ctx.send(f">>> Profile for {theirDiscordID}\n\nName: {name}\n\nDegree and Major: {degreeMajor}\n\nFavourite Groups: {favGroups}\n\nFavourite Idols: {favIdols}\n\nCurrently Listening To: {listeningTo}\n\nSomething I would like you to know: {something}")

            if isFound == False:
                f.close()

                name = "ADD YOUR NAME HERE"
                degreeMajor = "ADD YOUR DEGREE AND MAJOR HERE"
                favGroups = "ADD YOUR FAVOURITE GROUPS HERE"
                favIdols = "ADD YOUR FAVORITE IDOLS HERE"
                listeningTo = "ADD THE SONGS YOU ARE CURRENTLY LISTENING TO HERE"
                something = "ADD SOMETHING YOU WOULD LOVE EVERYONE TO KNOW ABOUT"

                largeMessage = f"{ctx.author.mention} $toP {name} $toP {degreeMajor} $toP {favGroups} $toP {favIdols} $toP {listeningTo} $toP {something}"
                f = open('profiles.txt', 'a')
                f.write(largeMessage)

                await ctx.send(f">>> Profile for {ctx.author.mention}\n\nName: {name}\n\nDegree and Major: {degreeMajor}\n\nFavourite Groups: {favGroups}\n\nFavourite Idols: {favIdols}\n\nCurrently Listening To: {listeningTo}\n\nSomething I would like you to know: {something}")
                f.close()
        else:
            f = open("profiles.txt", "r")

            isFound = False
            for x in f:

                temp = x.split()
                if message == temp[0]:

                    isFound = True
                    count = 0
                    theirDiscordID = ""
                    name = ""
                    degreeMajor = ""
                    favGroups = ""
                    favIdols = ""
                    listeningTo = ""
                    something = ""

                    for item in temp:

                        if item == "$toP":
                            count = count + 1
                        elif count == 0:
                            theirDiscordID = theirDiscordID + " " + item
                        elif count == 1:
                            name = name + " " + item
                        elif count == 2:
                            degreeMajor = degreeMajor + " " + item
                        elif count == 3:
                            favGroups = favGroups + " " + item
                        elif count == 4:
                            favIdols = favIdols + " " + item
                        elif count == 5:
                            listeningTo = listeningTo + " " + item
                        elif count == 6:
                            something = something + " " + item
                    f.close()

                    await ctx.send(
                        f">>> Profile for {theirDiscordID}\n\nName: {name}\n\nDegree and Major: {degreeMajor}\n\nFavourite Groups: {favGroups}\n\nFavourite Idols: {favIdols}\n\nCurrently Listening To: {listeningTo}\n\nSomething I would like you to know: {something}")

            if isFound == False:
                if ctx.author.mention == message:

                    name = "ADD YOUR NAME HERE"
                    degreeMajor = "ADD YOUR DEGREE AND MAJOR HERE"
                    favGroups = "ADD YOUR FAVOURITE GROUPS HERE"
                    favIdols = "ADD YOUR FAVORITE IDOLS HERE"
                    listeningTo = "ADD THE SONGS YOU ARE CURRENTLY LISTENING TO HERE"
                    something = "ADD SOMETHING YOU WOULD LOVE EVERYONE TO KNOW ABOUT"

                    largeMessage = f"{ctx.author.mention} $toP {name} $toP {degreeMajor} $toP {favGroups} $toP {favIdols} $toP {listeningTo} $toP {something}"
                    f = open('profiles.txt', 'a')
                    f.write(largeMessage)

                    await ctx.send(
                        f">>> Profile for {ctx.author.mention}\n\nName: {name}\n\nDegree and Major: {degreeMajor}\n\nFavourite Groups: {favGroups}\n\nFavourite Idols: {favIdols}\n\nCurrently Listening To: {listeningTo}\n\nSomething I would like you to know: {something}")
                    f.close()
                else:
                    await ctx.send(f">>> Sorry, the user: {message} can not be found... Please try again.")

    else:
        if messageLength[0].lower() == 'changename':
            f = open("profiles.txt", "r")
            infoArray = []
            arrayCount = 0
            isFound = False
            for x in f:
                arrayCount = arrayCount + 1
                temp = x.split()
                if ctx.author.mention != temp[0]:
                    infoArray.append(x)

                if ctx.author.mention == temp[0]:

                    isFound = True
                    count = 0
                    theirDiscordID = ""
                    name = ""
                    degreeMajor = ""
                    favGroups = ""
                    favIdols = ""
                    listeningTo = ""
                    something = ""

                    for item in temp:

                        if item == "$toP":
                            count = count + 1
                        elif count == 0:
                            theirDiscordID = theirDiscordID + " " + item
                        elif count == 1:
                            name = name + " " + item
                        elif count == 2:
                            degreeMajor = degreeMajor + " " + item
                        elif count == 3:
                            favGroups = favGroups + " " + item
                        elif count == 4:
                            favIdols = favIdols + " " + item
                        elif count == 5:
                            listeningTo = listeningTo + " " + item
                        elif count == 6:
                            something = something + " " + item
                    f.close()

                    newName = ""
                    for item in messageLength:
                        if item != 'changename':
                            newName = newName + item + " "

                    await ctx.send(">>> Your details has been successfully changed. Please type .profile self to view your changes")
                    f = open('profiles.txt', 'w')
                    largeMessage = f"{ctx.author.mention} $toP {newName} $toP {degreeMajor} $toP {favGroups} $toP {favIdols} $toP {listeningTo} $toP {something}"
                    f.write(largeMessage)
                    for item in infoArray:
                        f.write(item)
                    f.close()
            if isFound == False:
                f.close()

                name = "ADD YOUR NAME HERE"
                degreeMajor = "ADD YOUR DEGREE AND MAJOR HERE"
                favGroups = "ADD YOUR FAVOURITE GROUPS HERE"
                favIdols = "ADD YOUR FAVORITE IDOLS HERE"
                listeningTo = "ADD THE SONGS YOU ARE CURRENTLY LISTENING TO HERE"
                something = "ADD SOMETHING YOU WOULD LOVE EVERYONE TO KNOW ABOUT"

                newName = ""
                for item in messageLength:
                    if item != 'changename':
                        newName = newName + item + " "


                largeMessage = f"{ctx.author.mention} $toP {newName} $toP {degreeMajor} $toP {favGroups} $toP {favIdols} $toP {listeningTo} $toP {something}"
                f = open('profiles.txt', 'a')
                f.write(largeMessage)

                await ctx.send(
                    ">>> Your details has been successfully changed. Please type\n\n.profile self \n\nto view your changes")
                f.close()
        elif messageLength[0].lower() == 'changedegree':
            f = open("profiles.txt", "r")
            infoArray = []
            arrayCount = 0
            isFound = False
            for x in f:
                arrayCount = arrayCount + 1
                temp = x.split()
                if ctx.author.mention != temp[0]:
                    infoArray.append(x)

                if ctx.author.mention == temp[0]:

                    isFound = True
                    count = 0
                    theirDiscordID = ""
                    name = ""
                    degreeMajor = ""
                    favGroups = ""
                    favIdols = ""
                    listeningTo = ""
                    something = ""

                    for item in temp:

                        if item == "$toP":
                            count = count + 1
                        elif count == 0:
                            theirDiscordID = theirDiscordID + " " + item
                        elif count == 1:
                            name = name + " " + item
                        elif count == 2:
                            degreeMajor = degreeMajor + " " + item
                        elif count == 3:
                            favGroups = favGroups + " " + item
                        elif count == 4:
                            favIdols = favIdols + " " + item
                        elif count == 5:
                            listeningTo = listeningTo + " " + item
                        elif count == 6:
                            something = something + " " + item
                    f.close()

                    newDegree = ""
                    for item in messageLength:
                        if item.lower() != 'changedegree':
                            newDegree = newDegree + item + " "

                    await ctx.send(
                        ">>> Your details has been successfully changed. Please type .profile self to view your changes")
                    f = open('profiles.txt', 'w')
                    largeMessage = f"{ctx.author.mention} $toP {name} $toP {newDegree} $toP {favGroups} $toP {favIdols} $toP {listeningTo} $toP {something}"
                    f.write(largeMessage)
                    for item in infoArray:
                        f.write(item)
                    f.close()
            if isFound == False:
                f.close()

                name = "ADD YOUR NAME HERE"
                degreeMajor = "ADD YOUR DEGREE AND MAJOR HERE"
                favGroups = "ADD YOUR FAVOURITE GROUPS HERE"
                favIdols = "ADD YOUR FAVORITE IDOLS HERE"
                listeningTo = "ADD THE SONGS YOU ARE CURRENTLY LISTENING TO HERE"
                something = "ADD SOMETHING YOU WOULD LOVE EVERYONE TO KNOW ABOUT"

                newDegree = ""
                for item in messageLength:
                    if item.lower() != 'changedegree':
                        newDegree = newDegree + item + " "

                largeMessage = f"{ctx.author.mention} $toP {name} $toP {newDegree} $toP {favGroups} $toP {favIdols} $toP {listeningTo} $toP {something}"
                f = open('profiles.txt', 'a')
                f.write(largeMessage)

                await ctx.send(
                    ">>> Your details has been successfully changed. Please type\n\n.profile self \n\nto view your changes")
                f.close()
        elif messageLength[0].lower() == 'changegroups':
            f = open("profiles.txt", "r")
            infoArray = []
            arrayCount = 0
            isFound = False
            for x in f:
                arrayCount = arrayCount + 1
                temp = x.split()
                if ctx.author.mention != temp[0]:
                    infoArray.append(x)

                if ctx.author.mention == temp[0]:

                    isFound = True
                    count = 0
                    theirDiscordID = ""
                    name = ""
                    degreeMajor = ""
                    favGroups = ""
                    favIdols = ""
                    listeningTo = ""
                    something = ""

                    for item in temp:

                        if item == "$toP":
                            count = count + 1
                        elif count == 0:
                            theirDiscordID = theirDiscordID + " " + item
                        elif count == 1:
                            name = name + " " + item
                        elif count == 2:
                            degreeMajor = degreeMajor + " " + item
                        elif count == 3:
                            favGroups = favGroups + " " + item
                        elif count == 4:
                            favIdols = favIdols + " " + item
                        elif count == 5:
                            listeningTo = listeningTo + " " + item
                        elif count == 6:
                            something = something + " " + item
                    f.close()

                    newFavGroups = ""
                    for item in messageLength:
                        if item.lower() != 'changegroups':
                            newFavGroups = newFavGroups+ item + " "

                    await ctx.send(
                        ">>> Your details has been successfully changed. Please type .profile self to view your changes")
                    f = open('profiles.txt', 'w')
                    largeMessage = f"{ctx.author.mention} $toP {name} $toP {degreeMajor} $toP {newFavGroups} $toP {favIdols} $toP {listeningTo} $toP {something}"
                    f.write(largeMessage)
                    for item in infoArray:
                        f.write(item)
                    f.close()
            if isFound == False:
                f.close()

                name = "ADD YOUR NAME HERE"
                degreeMajor = "ADD YOUR DEGREE AND MAJOR HERE"
                favGroups = "ADD YOUR FAVOURITE GROUPS HERE"
                favIdols = "ADD YOUR FAVORITE IDOLS HERE"
                listeningTo = "ADD THE SONGS YOU ARE CURRENTLY LISTENING TO HERE"
                something = "ADD SOMETHING YOU WOULD LOVE EVERYONE TO KNOW ABOUT"

                newFavGroups = ""
                for item in messageLength:
                    if item.lower() != 'changegroups':
                        newFavGroups = newFavGroups + item + " "

                largeMessage = f"{ctx.author.mention} $toP {name} $toP {degreeMajor} $toP {newFavGroups} $toP {favIdols} $toP {listeningTo} $toP {something}"
                f = open('profiles.txt', 'a')
                f.write(largeMessage)

                await ctx.send(
                    ">>> Your detailshas been successfully changed. Please type\n\n.profile self \n\nto view your changes")
                f.close()
        elif messageLength[0].lower() == 'changeidols':
            f = open("profiles.txt", "r")
            infoArray = []
            arrayCount = 0
            isFound = False
            for x in f:
                arrayCount = arrayCount + 1
                temp = x.split()
                if ctx.author.mention != temp[0]:
                    infoArray.append(x)

                if ctx.author.mention == temp[0]:

                    isFound = True
                    count = 0
                    theirDiscordID = ""
                    name = ""
                    degreeMajor = ""
                    favGroups = ""
                    favIdols = ""
                    listeningTo = ""
                    something = ""

                    for item in temp:

                        if item == "$toP":
                            count = count + 1
                        elif count == 0:
                            theirDiscordID = theirDiscordID + " " + item
                        elif count == 1:
                            name = name + " " + item
                        elif count == 2:
                            degreeMajor = degreeMajor + " " + item
                        elif count == 3:
                            favGroups = favGroups + " " + item
                        elif count == 4:
                            favIdols = favIdols + " " + item
                        elif count == 5:
                            listeningTo = listeningTo + " " + item
                        elif count == 6:
                            something = something + " " + item
                    f.close()

                    newFavIdols = ""
                    for item in messageLength:
                        if item.lower() != 'changeidols':
                            newFavIdols = newFavIdols + item + " "

                    await ctx.send(
                        ">>> Your details has been successfully changed. Please type .profile self to view your changes")
                    f = open('profiles.txt', 'w')
                    largeMessage = f"{ctx.author.mention} $toP {name} $toP {degreeMajor} $toP {favGroups} $toP {newFavIdols} $toP {listeningTo} $toP {something}"
                    f.write(largeMessage)
                    for item in infoArray:
                        f.write(item)
                    f.close()
            if isFound == False:
                f.close()

                name = "ADD YOUR NAME HERE"
                degreeMajor = "ADD YOUR DEGREE AND MAJOR HERE"
                favGroups = "ADD YOUR FAVOURITE GROUPS HERE"
                favIdols = "ADD YOUR FAVORITE IDOLS HERE"
                listeningTo = "ADD THE SONGS YOU ARE CURRENTLY LISTENING TO HERE"
                something = "ADD SOMETHING YOU WOULD LOVE EVERYONE TO KNOW ABOUT"

                newFavIdols = ""
                for item in messageLength:
                    if item.lower() != 'changeidols':
                        newFavIdols = newFavIdols + item + " "

                largeMessage = f"{ctx.author.mention} $toP {name} $toP {degreeMajor} $toP {favGroups} $toP {newFavIdols} $toP {listeningTo} $toP {something}"
                f = open('profiles.txt', 'a')
                f.write(largeMessage)

                await ctx.send(
                    ">>> Your details has been successfully changed. Please type\n\n.profile self \n\nto view your changes")
                f.close()
        elif messageLength[0].lower() == 'changelistening':
            f = open("profiles.txt", "r")
            infoArray = []
            arrayCount = 0
            isFound = False
            for x in f:
                arrayCount = arrayCount + 1
                temp = x.split()
                if ctx.author.mention != temp[0]:
                    infoArray.append(x)

                if ctx.author.mention == temp[0]:

                    isFound = True
                    count = 0
                    theirDiscordID = ""
                    name = ""
                    degreeMajor = ""
                    favGroups = ""
                    favIdols = ""
                    listeningTo = ""
                    something = ""

                    for item in temp:

                        if item == "$toP":
                            count = count + 1
                        elif count == 0:
                            theirDiscordID = theirDiscordID + " " + item
                        elif count == 1:
                            name = name + " " + item
                        elif count == 2:
                            degreeMajor = degreeMajor + " " + item
                        elif count == 3:
                            favGroups = favGroups + " " + item
                        elif count == 4:
                            favIdols = favIdols + " " + item
                        elif count == 5:
                            listeningTo = listeningTo + " " + item
                        elif count == 6:
                            something = something + " " + item
                    f.close()

                    newListening = ""
                    for item in messageLength:
                        if item.lower() != 'changelistening':
                            newListening = newListening + item + " "

                    await ctx.send(
                        ">>> Your details has been successfully changed. Please type .profile self to view your changes")
                    f = open('profiles.txt', 'w')
                    largeMessage = f"{ctx.author.mention} $toP {name} $toP {degreeMajor} $toP {favGroups} $toP {favIdols} $toP {newListening} $toP {something}"
                    f.write(largeMessage)
                    for item in infoArray:
                        f.write(item)
                    f.close()
            if isFound == False:
                f.close()

                name = "ADD YOUR NAME HERE"
                degreeMajor = "ADD YOUR DEGREE AND MAJOR HERE"
                favGroups = "ADD YOUR FAVOURITE GROUPS HERE"
                favIdols = "ADD YOUR FAVORITE IDOLS HERE"
                listeningTo = "ADD THE SONGS YOU ARE CURRENTLY LISTENING TO HERE"
                something = "ADD SOMETHING YOU WOULD LOVE EVERYONE TO KNOW ABOUT"

                newListening = ""
                for item in messageLength:
                    if item.lower() != 'changelistening':
                        newListening = newListening + item + " "

                largeMessage = f"{ctx.author.mention} $toP {name} $toP {degreeMajor} $toP {favGroups} $toP {favIdols} $toP {newListening} $toP {something}"
                f = open('profiles.txt', 'a')
                f.write(largeMessage)

                await ctx.send(
                    ">>> Your details has been successfully changed. Please type\n\n.profile self \n\nto view your changes")
                f.close()
        elif messageLength[0].lower() == 'changesomething':
            f = open("profiles.txt", "r")
            infoArray = []
            arrayCount = 0
            isFound = False
            for x in f:
                arrayCount = arrayCount + 1
                temp = x.split()
                if ctx.author.mention != temp[0]:
                    infoArray.append(x)

                if ctx.author.mention == temp[0]:

                    isFound = True
                    count = 0
                    theirDiscordID = ""
                    name = ""
                    degreeMajor = ""
                    favGroups = ""
                    favIdols = ""
                    listeningTo = ""
                    something = ""

                    for item in temp:

                        if item == "$toP":
                            count = count + 1
                        elif count == 0:
                            theirDiscordID = theirDiscordID + " " + item
                        elif count == 1:
                            name = name + " " + item
                        elif count == 2:
                            degreeMajor = degreeMajor + " " + item
                        elif count == 3:
                            favGroups = favGroups + " " + item
                        elif count == 4:
                            favIdols = favIdols + " " + item
                        elif count == 5:
                            listeningTo = listeningTo + " " + item
                        elif count == 6:
                            something = something + " " + item
                    f.close()

                    newSomething = ""
                    for item in messageLength:
                        if item.lower() != 'changesomething':
                            newSomething = newSomething + item + " "

                    await ctx.send(
                        ">>> Your details has been successfully changed. Please type .profile self to view your changes")
                    f = open('profiles.txt', 'w')
                    largeMessage = f"{ctx.author.mention} $toP {name} $toP {degreeMajor} $toP {favGroups} $toP {favIdols} $toP {listeningTo} $toP {newSomething}"
                    f.write(largeMessage)
                    for item in infoArray:
                        f.write(item)
                    f.close()
            if isFound == False:
                f.close()

                name = "ADD YOUR NAME HERE"
                degreeMajor = "ADD YOUR DEGREE AND MAJOR HERE"
                favGroups = "ADD YOUR FAVOURITE GROUPS HERE"
                favIdols = "ADD YOUR FAVORITE IDOLS HERE"
                listeningTo = "ADD THE SONGS YOU ARE CURRENTLY LISTENING TO HERE"
                something = "ADD SOMETHING YOU WOULD LOVE EVERYONE TO KNOW ABOUT"

                newSomething = ""
                for item in messageLength:
                    if item.lower() != 'changesomething':
                        newSomething = newSomething + item + " "

                largeMessage = f"{ctx.author.mention} $toP {name} $toP {degreeMajor} $toP {favGroups} $toP {favIdols} $toP {listeningTo} $toP {newSomething}"
                f = open('profiles.txt', 'a')
                f.write(largeMessage)

                await ctx.send(
                    ">>> Your details has been successfully changed. Please type\n\n.profile self \n\nto view your changes")
                f.close()
# Idol Guess

# Initialising Variables for Idol Guess

theFinalGroup = []
theFinalName = []
theFinalPhoto = []
hasStarted = []
longScore = []


@client.command(help="Type .idolguess commands for more information about this command", aliases=['ig'])
async def idolguess(ctx, *, guess):
    if guess == 'commands':
        await ctx.send(
            "```css\n\n.idolguess start - Starts the game\n\n.idolguess {the name of the person} - Make your guess (For example, type .idolguess sojin)\n\n.idolguess skip - Skips the current idol you have to guess at the cost of one life\n\n.idolguess quit - Quits the whole game overall```")
    elif guess == 'start' and len(hasStarted) == 0:
        hasStarted.append(0)
        f = open("kpop.txt", "r")
        theirGroup = []
        theirName = []
        theirPhoto = []
        counterNumber = 0;

        for x in f:
            counterNumber = counterNumber + 1
            temp = x.split()
            theirPhoto.append(temp[len(temp) - 1])
            temp.remove(temp[len(temp) - 1])
            idol_group = ""
            idol_name = ""
            count_one = []
            for item in temp:
                if item != 'ge' and len(count_one) == 0:
                    idol_group = idol_group + item
                    count_one.append(0)
                elif item != 'ge' and len(count_one) == 1:
                    idol_group = idol_group + " " + item
                elif item == 'ge':
                    count_one.append(0)
                elif len(count_one) == 2:
                    idol_name = idol_name + item
                    count_one.append(0)
                elif len(count_one) == 3:
                    idol_name = idol_name + " " + item
            count_one.clear()

            theirGroup.append(idol_group)
            theirName.append(idol_name)

        f.close()

        theIndex = randint(0, counterNumber - 1)
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
        counterNumber = 0

        for x in f:
            counterNumber = counterNumber + 1
            temp = x.split()
            theirPhoto.append(temp[len(temp) - 1])
            temp.remove(temp[len(temp) - 1])
            idol_group = ""
            idol_name = ""
            count_one = []
            for item in temp:
                if item != 'ge' and len(count_one) == 0:
                    idol_group = idol_group + item
                    count_one.append(0)
                elif item != 'ge' and len(count_one) == 1:
                    idol_group = idol_group + " " + item
                elif item == 'ge':
                    count_one.append(0)
                elif len(count_one) == 2:
                    idol_name = idol_name + item
                    count_one.append(0)
                elif len(count_one) == 3:
                    idol_name = idol_name + " " + item
            count_one.clear()

            theirGroup.append(idol_group)
            theirName.append(idol_name)

        f.close()

        theIndex = randint(0, counterNumber - 1)
        theFinalGroup.append(theirGroup[theIndex])
        theFinalName.append(theirName[theIndex])
        theFinalPhoto.append(theirPhoto[theIndex])

        await ctx.send(f">>> Current score: {len(longScore)}\n\nWho is this?\n{theFinalPhoto[0]}")

    elif ((guess.lower() != theFinalName[0].lower()) or (guess.lower() == 'skip')) and len(
            hasStarted) != 0 and guess.lower() != 'quit' and guess.lower() != 'start':
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
        counterNumber = 0

        for x in f:
            counterNumber = counterNumber + 1
            temp = x.split()
            theirPhoto.append(temp[len(temp) - 1])
            temp.remove(temp[len(temp) - 1])
            idol_group = ""
            idol_name = ""
            count_one = []
            for item in temp:
                if item != 'ge' and len(count_one) == 0:
                    idol_group = idol_group + item
                    count_one.append(0)
                elif item != 'ge' and len(count_one) == 1:
                    idol_group = idol_group + " " + item
                elif item == 'ge':
                    count_one.append(0)
                elif len(count_one) == 2:
                    idol_name = idol_name + item
                    count_one.append(0)
                elif len(count_one) == 3:
                    idol_name = idol_name + " " + item
            count_one.clear()

            theirGroup.append(idol_group)
            theirName.append(idol_name)

        f.close()
        theIndex = randint(0, counterNumber - 1)
        theFinalGroup.append(theirGroup[theIndex])
        theFinalName.append(theirName[theIndex])
        theFinalPhoto.append(theirPhoto[theIndex])

        await ctx.send(f">>> Current score: {len(longScore)}\n\nWho is this?\n{theFinalPhoto[0]}")

    elif guess.lower() == 'quit':
        await ctx.send(
            f">>> You have lost...\nThe answer was {theFinalName[0]} from {theFinalGroup[0]}\n\nFinal score: {len(longScore)}")
        theFinalName.clear()
        theFinalGroup.clear()
        theFinalPhoto.clear()
        hasStarted.clear()
        longScore.clear()

    else:
        await ctx.send(f">>> Sorry, that command is invalid for now...")

pasta_eight = ">>> :astonished: \n\nhttps://scontent.fakl5-1.fna.fbcdn.net/v/t1.15752-9/99294388_247869029612059_3078739987789774848_n.jpg?_nc_cat=106&_nc_sid=b96e70&_nc_ohc=u9DVNYVFf9IAX_k-55Z&_nc_ht=scontent.fakl5-1.fna&oh=a1a452a18aaf694a24c1a97174b8ef4c&oe=5EEF5B60"

pasta_nine = ">>> Never forget this team :triumph:\n\n https://www.youtube.com/watch?v=Hbhq7M0PG3Y"

pasta_ten = ">>> :v: :thumbsup:  \n\nhttps://scontent.fakl5-1.fna.fbcdn.net/v/t1.15752-9/99291141_2921626921291871_4966866104270979072_n.jpg?_nc_cat=105&_nc_sid=b96e70&_nc_ohc=ous0fhh0_UgAX_VxHLA&_nc_ht=scontent.fakl5-1.fna&oh=2e985e37fca82e9cf7c75c366e27164b&oe=5EEC16FC"

CHANNEL = your_channel_number_goes_here

@client.event
async def copy_pasta():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL)
    interval = 60

    while not client.is_closed():
        pastaArray = [pasta_eight, pasta_nine, pasta_ten]
        await asyncio.sleep(interval)
        await channel.send(random.choice(pastaArray))
        await asyncio.sleep(interval)


client.loop.create_task(copy_pasta())

client.run(token)
