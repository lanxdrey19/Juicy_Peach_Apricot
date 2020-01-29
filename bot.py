import discord
import random
from random import randint
from discord.ext import commands, tasks
from itertools import cycle
import asyncio
import pyowm
import math





client = commands.Bot(command_prefix = '.')
status = cycle(['Milkshake (Korean Ver.)', 'Always Be Your Girl (너의 소녀가 되어줄게)', 'Snowman(스노우맨)', 'Hue', 'Colors', 'Bon Bon Chocolat', 'Oopsie My Bad', 'Woowa',  'Tiki-Taka (99%)', 'Beautiful Days (그 시절 우리가 사랑했던 우리) '])


@client.event
async def on_ready():
    change_status.start()
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Always Be Your Girl (너의 소녀가 되어줄게)'))
    print('Bot is ready.')
    print('We have logged in as {0.user}'.format(client))


@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


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
    coolWords11 = ["bye","Bye","BYE"]
    coolWords12 = ["!cd", "!ww"]



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
        if message.content.count(word) > 0:
            await message.channel.send(f'>>> Hello there {message.author.mention}! I am Sad Bot\nType **.commands** for the list of all commands\nFeel free to make suggestions in the **#suggestions** channel\n\nhttps://thumbs.gfycat.com/PhonySelfishArrowana.webp')
            emoji = '👋'
            # or '\U0001f44d' or '👍'
            await message.add_reaction(emoji)

    for word in coolWords4:
        if message.content.count(word) > 0:
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
            await message.channel.send(">>> Your free trial of Kokobot has ended. However, Sadbot will always be free. Use Sadbot today!\n\n https://scontent.fakl6-1.fna.fbcdn.net/v/t1.15752-9/82462694_272856383692002_507557532571533312_n.jpg?_nc_cat=105&_nc_ohc=T61ibjd8r44AX_9ZXSp&_nc_ht=scontent.fakl6-1.fna&oh=c8467554b6b0be0dc27bfee1e38cab98&oe=5E9F6FBF")

    await client.process_commands(message)


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')


@client.command()
async def ping(ctx):
    await ctx.send(f'>>> Pong!\nLatency: {round(client.latency * 1000)} ms')



@client.command()
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


@client.command(aliases=['8ball'])
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


@client.command()
async def match(ctx, *, question):
    await ctx.send(f'>>> Shipping {question}...\nCompatibility: {randint(0,100)}%')


@client.command()
async def dice(ctx):
    await ctx.send(f'>>> :game_die: **Rolls game die** :game_die:\n{randint(1,6)}')


@client.command()
async def commands(ctx):
    await ctx.send('```css\nGeneral Commands:\n\n.8ball - Ask it a question (Will not work if no arguments are entered)\n\n.about - Details of Sadbot\n\n.cheerup - Try this one if you are feeling down\n\n.dice - Rolls die\n\n.examszn - Get some words of wisdom from the bot if you are feeling stressed for your upcoming exams\n\n.hug - Try this one on someone. Remember to tag them when using this command\n\n.match - Ship yourself with your crush (Will not work if no arguments are entered)\n\n.piglatin {your message} - Convert your message to Pig Latin\n\n.ping - Checks latency\n\n.stanloona {your message} - Convert your message to let others know you really stan LOONA\n\nGame Commands:\n\n.idolguess commands - For Guess the Idol Game commands\n\n.idolquest commands - For Idol Quest Game commands\n\n.avalon commands - For Avalon Game commands```')


@client.command()
async def examszn(ctx):
    await ctx.send('>>> https://scontent.fakl6-1.fna.fbcdn.net/v/t1.15752-9/82079945_572354906648893_1092284134119702528_n.jpg?_nc_cat=103&_nc_ohc=w3g7WNcR28cAX-LNRS2&_nc_ht=scontent.fakl6-1.fna&oh=412aa5675422f10f2ad536699e319b2e&oe=5E8F79B7')


@client.command(aliases=['sl'])
async def stanloona(ctx,*,arg):
    temp = arg.split()
    big_message = ""
    for thing in temp:
        med_message = " Stan " + thing + " Loona "
        big_message = big_message + med_message
    await ctx.send(f">>> {big_message}")

@client.command(aliases=['pl'])
async def piglatin(ctx,*,arg):
    temp = arg.split()
    big_message = ""
    for thing in temp:
        med_message = thing[-1]  + thing[:-1] + "e"
        big_message = big_message + " " + med_message + " "
    await ctx.send(f">>> {big_message}")


@client.command()
async def about(ctx):
    await ctx.send(">>> https://gfycat.com/AchingLeanFalcon\n\nVersion: 0.3.2.3\nLatest Additions: Idol Guessing game and a few trivial commands\nNext Version: 0.3.3.0\nFuture Additions: TBA\nOwner: keed talk to 'em#2206\n\nSadbot has been made with lots of love!")

rounds_array = [ [2,2,2,3,3,3] , [3,3,3,4,4,4], [2,4,3,4,4,4] , [3,3,4,5,5,5], [3,4,4,5,5,5]]
avalon_players_mention = []
game_phase = []
no_votes = []
fail_votes = []
mission_participants = []
has_voted = []
game_score = []

mission_lock = []

turn_index = []
current_index = []
hammer_index = []
lady_index = []
lady_use = []

deciders = []

avalon_roles5 = ['Loyal', 'Percival', 'Merlin','Morgana', 'Assassin']
avalon_roles6 = ['Loyal', 'Loyal', 'Percival', 'Merlin', 'Morgana', 'Assassin']
avalon_roles7 = ['Loyal', 'Loyal', 'Percival', 'Merlin', 'Morgana', 'Assassin', 'Mordred']
avalon_roles8 = ['Loyal', 'Loyal', 'Loyal', 'Percival', 'Merlin', 'Morgana', 'Assassin', 'Mordred']
avalon_roles9 = ['Loyal', 'Loyal', 'Loyal', 'Loyal','Percival', 'Merlin', 'Morgana', 'Assassin', 'Mordred']
avalon_roles10 = ['Loyal', 'Loyal', 'Loyal', 'Loyal', 'Percival', 'Merlin', 'Morgana', 'Assassin','Mordred','Lackey']

@client.command()
async def choose(ctx,*,message):

    if mission_lock == 1:
        await ctx.send("The people that have been chosen can not be changed")
        return

    temp = message.split()

    y_axis = len(game_score)
    x_axis = len(avalon_players_mention) - 5


    some_message = ""

    for things in temp:

        mission_participants.append(things)
        some_message = some_message + f"{things}\n"

    people_needed = rounds_array[y_axis][x_axis]
    if (len(temp) == people_needed) and (ctx.author.mention == avalon_players_mention[current_index[0]]):
        await ctx.send(f">>> {some_message}\nhave been chosen for this mission. Type **.avalon no** to vote no for the mission or type **.avalon yes** to let this mission to continue ")
    else:
        await ctx.send(f"Sorry... It is either not your turn or you entered the wrong number of people...")





@client.command()
async def lady(ctx, index : discord.Member):

    if len(lady_use) < 1:
        if ctx.author.mention == index.mention:
            if len(game_score) >= 2 and len(avalon_players_mention) == len(avalon_roles5):
                if avalon_roles5[avalon_players_mention.index(index.mention)] == "Morgana" or avalon_roles5[avalon_players_mention.index(index.mention)] == "Assassin":
                    await ctx.author.send(f">>> {index.mention} is bad")
                else:
                    await ctx.author.send(f">>> {index.mention} is good")
                lady_index.pop(0)
                lady_index.append(index.mention)
                lady_use.append(1)
                await ctx.send(f"{index.mention} now has the lady of the lake")
            elif len(game_score) >= 2 and len(avalon_players_mention) == len(avalon_roles6):
                if avalon_roles6[avalon_players_mention.index(index.mention)] == "Morgana" or avalon_roles6[avalon_players_mention.index(index.mention)] == "Assassin":
                    await ctx.author.send(f">>> {index.mention} is bad")
                else:
                    await ctx.author.send(f">>> {index.mention} is good")
                lady_index.pop(0)
                lady_index.append(index.mention)
                lady_use.append(1)
                await ctx.send(f"{index.mention} now has the lady of the lake")
            elif len(game_score) >= 2 and len(avalon_players_mention) == len(avalon_roles7):

                if avalon_roles7[avalon_players_mention.index(index.mention)] == "Morgana" or avalon_roles7[avalon_players_mention.index(index.mention)] == "Assassin" or avalon_roles7[avalon_players_mention.index(index.mention)] == "Mordred":
                    await ctx.author.send(f">>> {index.mention} is bad")
                else:
                    await ctx.author.send(f">>> {index.mention} is good")
                lady_index.pop(0)
                lady_index.append(index.mention)
                lady_use.append(1)
                await ctx.send(f"{index.mention} now has the lady of the lake")
            elif len(game_score) >= 2 and len(avalon_players_mention) == len(avalon_roles8):
                if avalon_roles8[avalon_players_mention.index(index.mention)] == "Morgana" or avalon_roles8[avalon_players_mention.index(index.mention)] == "Assassin" or avalon_roles8[avalon_players_mention.index(index.mention)] == "Mordred":
                    await ctx.author.send(f">>> {index.mention} is bad")
                else:
                    await ctx.author.send(f">>> {index.mention} is good")
                lady_index.pop(0)
                lady_index.append(index.mention)
                lady_use.append(1)
                await ctx.send(f"{index.mention} now has the lady of the lake")
            elif len(game_score) >= 2 and len(avalon_players_mention) == len(avalon_roles9):
                if avalon_roles9[avalon_players_mention.index(index.mention)] == "Morgana" or avalon_roles9[avalon_players_mention.index(index.mention)] == "Assassin" or avalon_roles9[avalon_players_mention.index(index.mention)] == "Mordred":
                    await ctx.author.send(f">>> {index.mention} is bad")
                else:
                    await ctx.author.send(f">>> {index.mention} is good")
                lady_index.pop(0)
                lady_index.append(index.mention)
                lady_use.append(1)
                await ctx.send(f"{index.mention} now has the lady of the lake")
            elif len(game_score) >= 2 and len(avalon_players_mention) == len(avalon_roles10):
                if avalon_roles10[avalon_players_mention.index(index.mention)] == "Morgana" or avalon_roles10[avalon_players_mention.index(index.mention)] == "Assassin" or avalon_roles10[avalon_players_mention.index(index.mention)] == "Mordred" or avalon_roles10[avalon_players_mention.index(index.mention)] == "Lackey":
                    await ctx.author.send(f">>> {index.mention} is bad")
                else:
                    await ctx.author.send(f">>> {index.mention} is good")
                lady_index.pop(0)
                lady_index.append(index.mention)
                lady_use.append(1)
                await ctx.send(f"{index.mention} now has the lady of the lake")
        else:
            await ctx.send("You do not have the lady of the lake")
    else:
        await ctx.send("The lady of the lake has already been used this round")


@client.command()
async def merlin(ctx, member: discord.Member):

    if len(game_phase) == 2:

        if len(avalon_roles5) == len(avalon_players_mention):


            if avalon_roles5[avalon_players_mention.index(member.mention)] == 'Merlin':

                await ctx.send(">>> **Bad people win**")
                avalon_players_mention.clear()
                game_phase.clear()
                no_votes.clear()
                fail_votes.clear()
                mission_participants.clear()
                has_voted.clear()
                game_score.clear()
                turn_index.clear()
                current_index.clear()
                hammer_index.clear()
                lady_index.clear()
                deciders.clear()
                mission_lock.clear()

            else:

                await ctx.send(">>> **Good people win**")
                avalon_players_mention.clear()
                game_phase.clear()
                no_votes.clear()
                fail_votes.clear()
                mission_participants.clear()
                has_voted.clear()
                game_score.clear()
                turn_index.clear()
                current_index.clear()
                hammer_index.clear()
                lady_index.clear()
                deciders.clear()
                mission_lock.clear()


        elif len(avalon_roles6) == len(avalon_players_mention):
            if avalon_roles6[avalon_players_mention.index(member.mention)] == 'Merlin':
                await ctx.send(">>> **Bad people win**")
                avalon_players_mention.clear()
                game_phase.clear()
                no_votes.clear()
                fail_votes.clear()
                mission_participants.clear()
                has_voted.clear()
                game_score.clear()
                turn_index.clear()
                current_index.clear()
                hammer_index.clear()
                lady_index.clear()
                deciders.clear()
                mission_lock.clear()

            else:
                await ctx.send(">>> **Good people win**")
                avalon_players_mention.clear()
                game_phase.clear()
                no_votes.clear()
                fail_votes.clear()
                mission_participants.clear()
                has_voted.clear()
                game_score.clear()
                turn_index.clear()
                current_index.clear()
                hammer_index.clear()
                lady_index.clear()
                deciders.clear()
                mission_lock.clear()

        elif len(avalon_roles7) == len(avalon_players_mention):
            if avalon_roles7[avalon_players_mention.index(member.mention)] == 'Merlin':
                await ctx.send(">>> **Bad people win**")
                avalon_players_mention.clear()
                game_phase.clear()
                no_votes.clear()
                fail_votes.clear()
                mission_participants.clear()
                has_voted.clear()
                game_score.clear()
                turn_index.clear()
                current_index.clear()
                hammer_index.clear()
                lady_index.clear()
                deciders.clear()
                mission_lock.clear()

            else:
                await ctx.send(">>> **Good people win**")
                avalon_players_mention.clear()
                game_phase.clear()
                no_votes.clear()
                fail_votes.clear()
                mission_participants.clear()
                has_voted.clear()
                game_score.clear()
                turn_index.clear()
                current_index.clear()
                hammer_index.clear()
                lady_index.clear()
                deciders.clear()
                mission_lock.clear()

        elif len(avalon_roles8) == len(avalon_players_mention):
            if avalon_roles8[avalon_players_mention.index(member.mention)] == 'Merlin':
                await ctx.send(">>> **Bad people win**")
                avalon_players_mention.clear()
                game_phase.clear()
                no_votes.clear()
                fail_votes.clear()
                mission_participants.clear()
                has_voted.clear()
                game_score.clear()
                turn_index.clear()
                current_index.clear()
                hammer_index.clear()
                lady_index.clear()
                deciders.clear()
                mission_lock.clear()

            else:
                await ctx.send(">>> **Good people win**")
                avalon_players_mention.clear()
                game_phase.clear()
                no_votes.clear()
                fail_votes.clear()
                mission_participants.clear()
                has_voted.clear()
                game_score.clear()
                turn_index.clear()
                current_index.clear()
                hammer_index.clear()
                lady_index.clear()
                deciders.clear()
                mission_lock.clear()

        elif len(avalon_roles9) == len(avalon_players_mention):
            if avalon_roles9[avalon_players_mention.index(member.mention)] == 'Merlin':
                await ctx.send(">>> **Bad people win**")
                avalon_players_mention.clear()
                game_phase.clear()
                no_votes.clear()
                fail_votes.clear()
                mission_participants.clear()
                has_voted.clear()
                game_score.clear()
                turn_index.clear()
                current_index.clear()
                hammer_index.clear()
                lady_index.clear()
                deciders.clear()
                mission_lock.clear()

            else:
                await ctx.send(">>> **Good people win**")
                avalon_players_mention.clear()
                game_phase.clear()
                no_votes.clear()
                fail_votes.clear()
                mission_participants.clear()
                has_voted.clear()
                game_score.clear()
                turn_index.clear()
                current_index.clear()
                hammer_index.clear()
                lady_index.clear()
                deciders.clear()
                mission_lock.clear()

        elif len(avalon_roles10) == len(avalon_players_mention):
            if avalon_roles10[avalon_players_mention.index(member.mention)] == 'Merlin':
                await ctx.send(">>> **Bad people win**")
                avalon_players_mention.clear()
                game_phase.clear()
                no_votes.clear()
                fail_votes.clear()
                mission_participants.clear()
                has_voted.clear()
                game_score.clear()
                turn_index.clear()
                current_index.clear()
                hammer_index.clear()
                lady_index.clear()
                deciders.clear()
                mission_lock.clear()

            else:
                await ctx.send(">>> **Good people win**")
                avalon_players_mention.clear()
                game_phase.clear()
                no_votes.clear()
                fail_votes.clear()
                mission_participants.clear()
                has_voted.clear()
                game_score.clear()
                turn_index.clear()
                current_index.clear()
                hammer_index.clear()
                lady_index.clear()
                deciders.clear()
                mission_lock.clear()

        else:
            await ctx.send(">>> This command is not valid for now...")
    else:
        await ctx.send(">>> This command is not valid for now...")

@client.command()
async def avalon(ctx, reply):

    if reply == 'commands':
        await ctx.send("```css\n\n.avalon join - Join Avalon Matchmaking\n\n.avalon start - Commences an Avalon game\n\n.avalon myrole - Your Avalon role will be sent to you via a direct message from Sadbot\n\n.choose {participants} - Nominate who you want to go undertake the current mission. Remember to tag them when using this command\n\n.avalon yes - Vote yes to approve of the mission participants\n\n.avalon no - Vote no to not approve of the mission participants\n\n.avalon pass - Pass the mission\n\n.avalon fail - Fail the mission\n\n.lady {person you want to find the alliance of} - Checks the role of the person using the Lady of the Lake. Remember to tag them when using this command\n\n.merlin {person who you think is Merlin} - The bad people to win the game if they guess who the Merlin is correctly. Remember to tag them when using this command```")


    elif reply == 'join':

        if len(game_phase) <= 0:
            for name in avalon_players_mention:
                if name == ctx.author.mention:
                    await ctx.send(f'>>> {ctx.author.mention}, you have already joined matchmaking... ')
                    return

            if len(avalon_players_mention) == 10:
                await ctx.send(f">>> Sorry. Ten people is the maximum number of players for Avalon")
                return

            avalon_players_mention.append(ctx.author.mention)
            current_players = len(avalon_players_mention)

            await ctx.send(f'>>> You have joined the game {ctx.author.mention}\n\nCurrent number of players: {current_players} ')

        elif len(game_phase) > 0:
            await ctx.send(f">>> Game has already started. Wait for the next game")
            return

    elif reply == 'leave':
        if len(game_phase) <= 0:
            for name in avalon_players_mention:
                if name == ctx.author.mention:
                    avalon_players_mention.remove(name)
                    await ctx.send(f'>>> You have left Avalon matchmaking {ctx.author.mention} ')
                    return
            await ctx.send(f'>>> You have not joined Avalon matchmaking yet {ctx.author.mention}')

        elif len(game_phase) > 0:
            await ctx.send(">>> You can not leave the game once it has started")

    elif reply == 'start':
        if len(game_phase) <= 0:

            if len(avalon_players_mention) < 5:
                await ctx.send(f">>> Sorry {ctx.author.mention}, Avalon needs at least five players :cry:")
                return
            elif len(avalon_players_mention) >= 5:
                game_phase.append(0)
                await ctx.send(f">>> The game of Avalon has begun\n\nType **.avalon myrole** to find out your role")
                index_counter = 0
                verylong_message = ""
                for name in avalon_players_mention:

                    verylong_message = verylong_message + f"{index_counter}: {name} "

                    index_counter = index_counter + 1


                turn_index = range(len(avalon_players_mention))
                current_index.append(random.choice(turn_index))
                if int(current_index[0]) - 1 == -1:
                    lady_index.append(avalon_players_mention[len(avalon_players_mention) - 1])
                else:
                    lady_index.append(avalon_players_mention[int(current_index[0]) - 1])

                hammer_index.append((int(current_index[0]) + 4) % len(avalon_players_mention))


                await ctx.send(f">>> Round {len(game_score) + 1}\n\nCurrent Players:\n\n:arrow_left: {verylong_message} :arrow_right:")
                await ctx.send(f">>> The person who starts is {avalon_players_mention[current_index[0]]}\n\n The person who has lady of the lake is one place to the left of the person that starts {avalon_players_mention[lady_index[0]]}\n\nHammer falls on {avalon_players_mention[hammer_index[0]]}\n\nWhen people have decided who is going on a mission, type  **.mission** [number of people going on a mission] e.g. **.mission 3**\n\nTo use the lady of the lake type **.lady [their_index_number]** e.g. **.lady 3**")

                y_axis = len(game_score)
                x_axis = len(avalon_players_mention) - 5

                people_needed = rounds_array[y_axis][x_axis]
                await ctx.send(f">>> Choose {people_needed} people you want on this mission. Type **.choose @koko** to choose e.g. **.choose @denny3sacrowd @koko @sleo081 or .choose @sleo081 or .choose @sleo081 @denny3sacrowd** ")
                return

        elif len(game_phase) > 0:
            await ctx.send(f">>> The game of Avalon has already started...")

    elif reply == 'yes':
        if len(game_phase) != 1:
            await ctx.send(">>> This command is not valid for now")
            return
        for name in deciders:
            if name == ctx.author.mention:
                await ctx.send(">>> You have already voted no...")
                return
        deciders.append(ctx.author.mention)
        no_votes.append('yes')
        if len(deciders) == len(avalon_players_mention):
            await ctx.send(">>> Counting Votes...")
            await ctx.send(f">>> This is who voted for what:\n{deciders}\n{no_votes}")
            no_count = 0
            for vote in no_votes:
                if vote == 'no':
                    no_count = no_count + 1

            if no_count >= math.ceil(float(len(avalon_players_mention)) / float(2.0)):
                await ctx.send(">>> Please let the next person decide who goes on a mission")


                temp = current_index[0]

                new_num = (temp + 1) % len(avalon_players_mention)

                current_index.pop(0)

                current_index.append(new_num)

                if current_index[0] == hammer_index[0]:
                    await ctx.send(
                        f">>> {avalon_players_mention[current_index[0]]} gets to choose who goes in the mission without any objections. Type **.avalon no** to vote no for the mission or type **.avalon yes** to let this mission to continue")
                    game_phase.append(0)
                    deciders.clear()
                    no_votes.clear()


                else:
                    await ctx.send(f">>> It is now {avalon_players_mention[current_index[0]]}'s turn")
                    mission_participants.clear()
                    deciders.clear()
                    no_votes.clear()
            else:
                await ctx.send(">>> This mission will be undertaken soon.")
                mission_lock.append(0)

                game_phase.append(0)
                deciders.clear()
                no_votes.clear()

            return

        else:
            await ctx.send(f">>> Needs {len(avalon_players_mention) - len(no_votes)} more votes to reveal whether this mission is to be undertaken or not")

    elif reply == 'no':
        if len(game_phase) != 1:
            await ctx.send(">>> This command is not valid for now")
            return
        for name in deciders:
            if name == ctx.author.mention:
                await ctx.send(">>> You have already voted no...")
                return
        deciders.append(ctx.author.mention)
        no_votes.append("no")

        if len(deciders) == len(avalon_players_mention):
            await ctx.send(">>> Counting Votes...")
            await ctx.send(f">>> This is who voted for what:\n{deciders}\n{no_votes}")
            no_count = 0
            for vote in no_votes:
                if vote == 'no':
                    no_count = no_count + 1

            if no_count >= math.ceil(float(len(avalon_players_mention)) / float(2.0)):
                await ctx.send(">>> Please let the next person decide who goes on a mission")

                temp = current_index[0]

                new_num = (temp + 1) % len(avalon_players_mention)

                current_index.pop(0)

                current_index.append(new_num)

                if current_index[0] == hammer_index[0]:
                    await ctx.send(
                        f">>> {avalon_players_mention[current_index[0]]} gets to choose who goes in the mission without any objections. Type **.avalon no** to vote no for the mission or type **.avalon yes** to let this mission to continue")
                    game_phase.append(0)
                    deciders.clear()
                    no_votes.clear()
                    mission_lock.append(0)


                else:
                    await ctx.send(f">>> It is now {avalon_players_mention[current_index[0]]}'s turn")
                    mission_participants.clear()
                    deciders.clear()
                    no_votes.clear()
            else:
                await ctx.send(">>> This mission will be undertaken soon.")
                deciders.clear()
                no_votes.clear()
                mission_lock.append(0)
                game_phase.append(0)
            return
        else:
            await ctx.send(
                f">>> Needs {len(avalon_players_mention) - len(no_votes)} more votes to reveal whether this mission is to be undertaken or not")

    elif reply == 'fail':

        await ctx.channel.purge(limit=1)
        if len(game_phase) != 2:
            await ctx.send(">>> This command is not valid for now")
            return
        for name in has_voted:
            if name == ctx.author.mention:
                await ctx.send(">>> You have already voted")
                return
        county = 0
        for name in mission_participants:
            if name == ctx.author.mention:
                county = county + 1
        await ctx.send(f"{mission_participants}")
        if county == 0:
            await ctx.send(f">>> You are not selected for this mission or no one hasn't been nominated yet for this mission")
            return
        has_voted.append(ctx.author.mention)
        fail_votes.append(1)
        if len(game_score) == 3 and len(fail_votes) >= 2 and len(avalon_players_mention) >= 7 and len(mission_participants) == len(has_voted):
            await ctx.send(">>> **The mission has failed**")
            mission_lock.clear()
            game_phase.remove(0)
            mission_participants.clear()
            has_voted.clear()
            fail_votes.clear()
            game_score.append(0)
            lady_use.clear()
            hammer_index.pop(0)
            hammer_index.append((int(current_index[0]) + 4) % len(avalon_players_mention))
            index_counter = 0
            verylong_message = ""
            for name in avalon_players_mention:
                verylong_message = verylong_message + f"{index_counter}: {name} "

                index_counter = index_counter + 1

            passes = 0
            fails = 0
            for item in game_score:
                if item == 1:
                    passes = passes + 1
                elif item == 0:
                    fails = fails + 1
            if fails == 3:
                await ctx.send(">>> **The Bad people win.**")
                avalon_players_mention.clear()
                game_phase.clear()
                no_votes.clear()
                fail_votes.clear()
                mission_participants.clear()
                has_voted.clear()
                game_score.clear()

                current_index.clear()
                hammer_index.clear()
                lady_index.clear()
                deciders.clear()
                mission_lock.clear()

                return
            await ctx.send(f">>> Round {len(game_score) + 1}\n\nCurrent Players:\n\n:arrow_left: {verylong_message} :arrow_right:\n\nIt is now {avalon_players_mention[current_index[0]]}'s turn\n\nThe hammer lands on {avalon_players_mention[hammer_index[0]]}")
            y_axis = len(game_score)
            x_axis = len(avalon_players_mention) - 5

            people_needed = rounds_array[y_axis][x_axis]
            await ctx.send(f">>> Choose {people_needed} people you want on this mission. Type **.choose [person]** to choose e.g. **.choose @denny3sacrowd @koko @sleo081 or .choose @sleo081 or .choose @sleo081 @denny3sacrowd**")
            return
        elif len(fail_votes) >= 1 and len(mission_participants) == len(has_voted):
            await ctx.send(">>> **The mission has failed**")
            mission_lock.clear()
            game_phase.remove(0)
            mission_participants.clear()
            has_voted.clear()
            fail_votes.clear()
            game_score.append(0)
            lady_use.clear()
            hammer_index.pop(0)
            hammer_index.append((int(current_index[0]) + 4) % len(avalon_players_mention))
            index_counter = 0
            verylong_message = ""
            for name in avalon_players_mention:
                verylong_message = verylong_message + f"{index_counter}: {name} "

                index_counter = index_counter + 1


            passes = 0
            fails = 0
            for item in game_score:
                if item == 1:
                    passes = passes + 1
                elif item == 0:
                    fails = fails + 1
            if fails == 3:
                await ctx.send(">>> **The Bad people win.**")
                avalon_players_mention.clear()
                game_phase.clear()
                no_votes.clear()
                fail_votes.clear()
                mission_participants.clear()
                has_voted.clear()
                game_score.clear()

                current_index.clear()
                hammer_index.clear()
                lady_index.clear()
                deciders.clear()
                mission_lock.clear()

                return
            await ctx.send(f">>> Round {len(game_score) + 1}\n\nCurrent Players:\n\n:arrow_left: {verylong_message} :arrow_right:\n\nIt is now {avalon_players_mention[current_index[0]]}'s turn\n\nThe hammer lands on {avalon_players_mention[hammer_index[0]]}")
            y_axis = len(game_score)
            x_axis = len(avalon_players_mention) - 5

            people_needed = rounds_array[y_axis][x_axis]
            await ctx.send(f">>> Choose {people_needed} people you want on this mission. Type **.choose [person]** to choose e.g. **.choose @denny3sacrowd @koko @sleo081 or .choose @sleo081 or .choose @sleo081 @denny3sacrowd** ")
            return

    elif reply == 'pass':
        await ctx.channel.purge(limit=1)
        if len(game_phase) != 2:
            await ctx.send(">>> This command is not valid for now")
            return
        for name in has_voted:
            if name == ctx.author.mention:
                await ctx.send(">>> You have already voted")
                return
        county = 0
        for name in mission_participants:
            if name == ctx.author.mention:
                county = county + 1
        await ctx.send(f"{mission_participants}")
        if county == 0:
            await ctx.send(f">>> You are not selected for this mission or no one hasn't been nominated yet for this mission")
            return
        has_voted.append(ctx.author.mention)
        if len(mission_participants) == len(has_voted) and len(fail_votes) < 2 and len(avalon_players_mention) >= 7 and len(game_score) == 3:
            await ctx.send(">>> **The mission has passed**")
            mission_lock.clear()
            game_phase.remove(0)
            mission_participants.clear()
            has_voted.clear()
            game_score.append(1)
            lady_use.clear()
            hammer_index.pop(0)
            hammer_index.append((int(current_index[0]) + 4) % len(avalon_players_mention))
            index_counter = 0
            verylong_message = ""
            for name in avalon_players_mention:
                verylong_message = verylong_message + f"{index_counter}: {name} "

                index_counter = index_counter + 1

            passes = 0
            fails = 0
            for item in game_score:
                if item == 1:
                    passes = passes + 1
                elif item == 0:
                    fails = fails + 1
            if passes == 3:

                await ctx.send(">>> The Bad people have one more chance to win if they guess who the Merlin is. Type **.merlin @person** to guess")
                return
            await ctx.send(f">>> Round {len(game_score) + 1}\n\nCurrent Players:\n\n:arrow_left: {verylong_message} :arrow_right:\n\nIt is now {avalon_players_mention[current_index[0]]}'s turn\n\nThe hammer lands on {avalon_players_mention[hammer_index[0]]}")
            y_axis = len(game_score)
            x_axis = len(avalon_players_mention) - 5

            people_needed = rounds_array[y_axis][x_axis]
            await ctx.send(f">>> Choose {people_needed} people you want on this mission. Type **.choose [person]** to choose e.g. **.choose @denny3sacrowd @koko @sleo081 or .choose @sleo081 or .choose @sleo081 @denny3sacrowd**")
            return
        elif len(mission_participants) == len(has_voted) and len(fail_votes) < 1:
            await ctx.send(">>> **The mission has passed**")
            mission_lock.clear()
            game_phase.remove(0)
            mission_participants.clear()
            has_voted.clear()
            game_score.append(1)
            lady_use.clear()
            hammer_index.pop(0)
            hammer_index.append((int(current_index[0]) + 4) % len(avalon_players_mention))
            index_counter = 0
            verylong_message = ""
            for name in avalon_players_mention:
                verylong_message = verylong_message + f"{index_counter}: {name} "

                index_counter = index_counter + 1

            passes = 0
            fails = 0
            for item in game_score:
                if item == 1:
                    passes = passes + 1
                elif item == 0:
                    fails = fails + 1
            if passes == 3:

                await ctx.send(">>> The Bad people have one more chance to win if they guess who the Merlin is. Type **.merlin @person** to guess")
                return
            await ctx.send(f">>> Round {len(game_score) + 1}\n\nCurrent Players:\n\n:arrow_left: {verylong_message} :arrow_right:\n\nIt is now {avalon_players_mention[current_index[0]]}'s turn\n\nThe hammer lands on {avalon_players_mention[hammer_index[0]]}")
            y_axis = len(game_score)
            x_axis = len(avalon_players_mention) - 5

            people_needed = rounds_array[y_axis][x_axis]
            await ctx.send(f">>> Choose {people_needed} people you want on this mission. Type **.choose [person]** to choose e.g. **.choose @denny3sacrowd @koko @sleo081 or .choose @sleo081 or .choose @sleo081 @denny3sacrowd**")
            return


    elif reply == 'myrole':
        if len(game_phase) >= 1:

            if len(avalon_players_mention) == 5:

                avalon_roles = ['Loyal', 'Percival', 'Merlin','Morgana', 'Assassin']
                await ctx.author.send(f'>>> The roles are\n\nGood:\nLoyal\nPercival\nMerlin\n\nBad:\nMorgana\nAssassin')

                random.shuffle(avalon_roles5)
                random.shuffle(avalon_roles5)
                random.shuffle(avalon_roles5)
                random.shuffle(avalon_roles5)
                random.shuffle(avalon_roles5)

                their_index = avalon_players_mention.index(ctx.author.mention)

                their_role = avalon_roles5[their_index]

                the_merlin_index = avalon_roles5.index("Merlin")

                the_merlin = avalon_players_mention[the_merlin_index]

                the_morgana_index = avalon_roles5.index("Morgana")

                the_morgana = avalon_players_mention[the_morgana_index]

                the_assassin_index = avalon_roles5.index("Assassin")

                the_assassin = avalon_players_mention[the_assassin_index]

                merlinmorganaArray = [the_merlin, the_morgana]

                the_index_zero = avalon_players_mention.index(merlinmorganaArray[0])

                the_index_one = avalon_players_mention.index(merlinmorganaArray[1])

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

            elif len(avalon_players_mention) == 6:

                avalon_roles = ['Loyal', 'Loyal', 'Percival', 'Merlin', 'Morgana', 'Assassin']
                await ctx.author.send(f'>>> The roles are\n\nGood:\nLoyal\nLoyal\nPercival\nMerlin\n\nBad:\nMorgana\nAssassin')

                random.shuffle(avalon_roles6)
                random.shuffle(avalon_roles6)
                random.shuffle(avalon_roles6)
                random.shuffle(avalon_roles6)
                random.shuffle(avalon_roles6)

                their_index = avalon_players_mention.index(ctx.author.mention)

                their_role = avalon_roles6[their_index]

                the_merlin_index = avalon_roles6.index("Merlin")

                the_merlin = avalon_players_mention[the_merlin_index]

                the_morgana_index = avalon_roles6.index("Morgana")

                the_morgana = avalon_players_mention[the_morgana_index]

                the_assassin_index = avalon_roles6.index("Assassin")

                the_assassin = avalon_players_mention[the_assassin_index]

                merlinmorganaArray = [the_merlin, the_morgana]

                the_index_zero = avalon_players_mention.index(merlinmorganaArray[0])

                the_index_one = avalon_players_mention.index(merlinmorganaArray[1])

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

            elif len(avalon_players_mention) == 7:

                avalon_roles = ['Loyal', 'Loyal', 'Percival', 'Merlin', 'Morgana', 'Assassin', 'Mordred']
                await ctx.author.send(f'>>> The roles are\n\nGood:\nLoyal\nLoyal\nPercival\nMerlin\n\nBad:\nMorgana\nAssassin\nMordred')

                random.shuffle(avalon_roles7)
                random.shuffle(avalon_roles7)
                random.shuffle(avalon_roles7)
                random.shuffle(avalon_roles7)
                random.shuffle(avalon_roles7)

                their_index = avalon_players_mention.index(ctx.author.mention)

                their_role = avalon_roles7[their_index]

                the_merlin_index = avalon_roles7.index("Merlin")

                the_merlin = avalon_players_mention[the_merlin_index]

                the_morgana_index = avalon_roles7.index("Morgana")

                the_morgana = avalon_players_mention[the_morgana_index]

                the_assassin_index = avalon_roles7.index("Assassin")

                the_assassin = avalon_players_mention[the_assassin_index]

                the_mordred_index = avalon_roles7.index("Mordred")

                the_mordred = avalon_players_mention[the_mordred_index]

                merlinmorganaArray = [the_merlin, the_morgana]

                the_index_zero = avalon_players_mention.index(merlinmorganaArray[0])

                the_index_one = avalon_players_mention.index(merlinmorganaArray[1])

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

            elif len(avalon_players_mention) == 8:

                avalon_roles = ['Loyal', 'Loyal', 'Loyal', 'Percival', 'Merlin', 'Morgana', 'Assassin', 'Mordred']
                await ctx.author.send(
                    f'>>> The roles are\n\nGood:\nLoyal\nLoyal\nLoyal\nPercival\nMerlin\n\nBad:\nMorgana\nAssassin\nMordred')

                random.shuffle(avalon_roles8)
                random.shuffle(avalon_roles8)
                random.shuffle(avalon_roles8)
                random.shuffle(avalon_roles8)
                random.shuffle(avalon_roles8)

                their_index = avalon_players_mention.index(ctx.author.mention)

                their_role = avalon_roles8[their_index]

                the_merlin_index = avalon_roles8.index("Merlin")

                the_merlin = avalon_players_mention[the_merlin_index]

                the_morgana_index = avalon_roles8.index("Morgana")

                the_morgana = avalon_players_mention[the_morgana_index]

                the_assassin_index = avalon_roles8.index("Assassin")

                the_assassin = avalon_players_mention[the_assassin_index]

                the_mordred_index = avalon_roles8.index("Mordred")

                the_mordred = avalon_players_mention[the_mordred_index]

                merlinmorganaArray = [the_merlin, the_morgana]

                the_index_zero = avalon_players_mention.index(merlinmorganaArray[0])

                the_index_one = avalon_players_mention.index(merlinmorganaArray[1])

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
            elif len(avalon_players_mention) == 9:

                avalon_roles = ['Loyal', 'Loyal', 'Loyal', 'Loyal','Percival', 'Merlin', 'Morgana', 'Assassin', 'Mordred']
                await ctx.author.send(
                    f'>>> The roles are\n\nGood:\nLoyal\nLoyal\nLoyal\nLoyal\nPercival\nMerlin\n\nBad:\nMorgana\nAssassin\nMordred')

                random.shuffle(avalon_roles9)
                random.shuffle(avalon_roles9)
                random.shuffle(avalon_roles9)
                random.shuffle(avalon_roles9)
                random.shuffle(avalon_roles9)

                their_index = avalon_players_mention.index(ctx.author.mention)

                their_role = avalon_roles9[their_index]

                the_merlin_index = avalon_roles9.index("Merlin")

                the_merlin = avalon_players_mention[the_merlin_index]

                the_morgana_index = avalon_roles9.index("Morgana")

                the_morgana = avalon_players_mention[the_morgana_index]

                the_assassin_index = avalon_roles9.index("Assassin")

                the_assassin = avalon_players_mention[the_assassin_index]

                the_mordred_index = avalon_roles9.index("Mordred")

                the_mordred = avalon_players_mention[the_mordred_index]

                merlinmorganaArray = [the_merlin, the_morgana]

                the_index_zero = avalon_players_mention.index(merlinmorganaArray[0])

                the_index_one = avalon_players_mention.index(merlinmorganaArray[1])

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

            elif len(avalon_players_mention) == 10:

                avalon_roles = ['Loyal', 'Loyal', 'Loyal', 'Loyal', 'Percival', 'Merlin', 'Morgana', 'Assassin',
                                'Mordred','Lackey']
                await ctx.author.send(
                    f'>>> The roles are\n\nGood:\nLoyal\nLoyal\nLoyal\nLoyal\nPercival\nMerlin\n\nBad:\nMorgana\nAssassin\nMordred\nLackey')

                random.shuffle(avalon_roles10)
                random.shuffle(avalon_roles10)
                random.shuffle(avalon_roles10)
                random.shuffle(avalon_roles10)
                random.shuffle(avalon_roles10)

                their_index = avalon_players_mention.index(ctx.author.mention)

                their_role = avalon_roles10[their_index]

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

                the_index_zero = avalon_players_mention.index(merlinmorganaArray[0])

                the_index_one = avalon_players_mention.index(merlinmorganaArray[1])

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

        elif len(game_phase) < 1:
            await ctx.send(f'>>> {ctx.author.mention} Avalon matchmaking is not finished yet...')


@client.command(aliases=['iq'])
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

                if int(their_singing[index]) >= threshold:
                    actingBoost = 0.5
                else:
                    actingBoost = 1

                if int(their_singing[index]) >= threshold:
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
                # 157 kpop idols in txt file jan 24 2020
                theIndex = randint(0, 156)
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

                    await ctx.send(f'>>> Competing against {group_name} {member_name}...\n{theirPhoto[theIndex]}\n\n')
                    await ctx.send(f'>>> Congratulations {ctx.author.mention}, you won against {group_name} {member_name}\n\n{extra_message}\n\nTotal Points: {str(int(their_points[index]) + extra_bonus)}')

                    f = open('idolquest.txt', 'w')
                    big_message = f'{ctx.author.mention} {str(int(their_points[index]) + extra_bonus )} {their_singing[index]} {their_dancing[index]} {their_acting[index]} {their_variety[index]}'
                    f.write(big_message)

                    for values in range(count):

                        if ctx.author.mention != their_username[values]:
                            long_message = f'{their_username[values]} {their_points[values]} {their_singing[values]} {their_dancing[values]} {their_acting[values]} {their_variety[values]}'

                            f.write(f'\n{long_message}')

                    f.close()
                else:

                    participation_bonus = 1
                    await ctx.send(f'>>> Competing against {group_name} {member_name}...\n{theirPhoto[theIndex]}\n\n')
                    await ctx.send(f'>>> {group_name} {member_name} has won. Sorry {ctx.author.mention}\n\nBonus Points:\nParticipation + 1\n\nTotal Points: {str(int(their_points[index]) + participation_bonus)}')

                    f = open('idolquest.txt', 'w')
                    big_message = f'{ctx.author.mention} {str(int(their_points[index]) + participation_bonus )} {their_singing[index]} {their_dancing[index]} {their_acting[index]} {their_variety[index]}'
                    f.write(big_message)

                    for values in range(count):

                        if ctx.author.mention != their_username[values]:
                            long_message = f'{their_username[values]} {their_points[values]} {their_singing[values]} {their_dancing[values]} {their_acting[values]} {their_variety[values]}'

                            f.write(f'\n{long_message}')

                    f.close()
            else:
                index = index + 1


@client.command()
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


theFinalGroup = []
theFinalName = []
theFinalPhoto = []
hasStarted = []
longScore = []

@client.command(aliases=['ig'])
async def idolguess(ctx, guess):
    if guess == 'commands':
        await ctx.send("```css\n\n.idolquess start - Starts the game\n\n.idolguess {the name of the person} - Make your guess (For example, type .idolguess chaekyung)\n\n.idolguess skip - Skips the current idol you have to guess at the cost of one life\n\n.idolquest quit - Quits the whole game overall```")
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
        # 157 kpop idols in txt file jan 15 2020
        theIndex = randint(0, 156)
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
        # 157 kpop idols in txt file jan 15 2020
        theIndex = randint(0, 156)
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
        # 157 kpop idols in txt file jan 15 2020
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

    else:
        await ctx.send(f">>> Sorry, that command is invalid for now...")


@client.command()
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
    # 157 kpop idols in txt file jan 15 2020
    theIndex = randint(0,156)
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

CHANNEL = your_channel_ID_goes here

pasta_one = '>>> IMPORTANT SERVER ANNOUNCEMENT:\n\nLet people know that they should sleep on their bed and not on Nayoung\n\nThank you for your cooperation\n\nhttps://www.youtube.com/watch?v=c4fkgRTe71Q\n\n'

pasta_two = '''
    
    
    >>> WHY CHOERRY SHOULD BE YOUR BIAS: An extensive guide on why Choi Yerim should be your bias.

As a conflicted Hyejoo-Yerim stan, I would like to clarify that Choerry isn't my ult bias. Anyway, here are reasons why Yerim should be YOUR bias.

1. Cockroach Control
Choerry has exhibited the skill of manipulating cockroaches and using them according to her will. It has been said that she speaks to them at night, ordering them to listen to the other girls speak to each other. This is why she knows all the other girl's secrets. She has also been seen by a hanbit, whispering to something on her shoulder during Line&Up. It is said that Choerry has cockroaches around the world, with a decicated cockroach army in LA. This makes her superior over the other girls.

2. Dimensional Traveler
Choerry can travel between dimensions, explaining her current hair color being black again. Choerry had purple hair but suddenly her hair went back to being black again, coincidence? I think not. Past Choerry went forward in time to kill purple haired Yerim, in order to prevent a nuclear war in South East Asia. Furthermore, she has not aged a day since we have first met her.

3. Non-transparent
Choerry is bubbly and innocent on the outside, exhibiting a radiant and positive personality. But that is all we know of it. According to another hanbit, who did not make it out alive when they met Choerry during a fansign, Choerry whispered dark incantations in the hanbits ear. This hanbit has since turned into a Potato Corndog, cursed to crunchy-flavorful mukbang goodness for all eternity.



'''

pasta_three = """


>>> To be fair, you have to have a very high IQ to understand LOONA. The LOONAVERSE is extremely subtle, and without a solid grasp of music theory, a basic understanding of quantum physics and genetics, and lore development, most of the narrative will go over a typical stan's head. There's also Yves’s narcissistic outlook, which is deftly woven into her characterisation - her personal philosophy draws heavily from John Appleby literature, for instance. The fans understand this stuff; they have the intellectual capacity to truly appreciate the depths of the lore, to realize that they're not just stories- they say something deep about LIFE. As a consequence, other people wouldn't appreciate, for instance, the subtlety in Haseul’s existencial lyric "dari tteugo, naneun niga doeeo ganeyo," which itself is a cryptic reference to Harper Lee's American classic The Catcher in the Rye. And yes by the way, I DO have a 이달의 소녀 tattoo. And no, you cannot see it. 



"""

pasta_four = ">>> This is a Yukika Discord Server Fanclub now. I’m quitting Sadboiclique\n\nhttps://scontent.fakl6-1.fna.fbcdn.net/v/t1.0-9/60687052_2186537251454307_3625354170539704320_o.jpg?_nc_cat=111&_nc_ohc=OJaMVrdvlbIAX9KZdt2&_nc_ht=scontent.fakl6-1.fna&oh=be8e87a8b2844c8f24633a1623dce8da&oe=5EA26B77"

pasta_five = ">>> Hosting a Cup-sleeve event for the three members of Yukika Discord Server Fanclub :muscle_tone5: :fire: :100: :ok_hand_tone5:"

pasta_six = ">>> We love an english-speaking queen\n\nhttps://www.youtube.com/watch?v=7_ARMGdeQOM"

pasta_seven = ">>> Oi Felix, chuck us a muzz!\n\nhttps://www.youtube.com/watch?v=f-PK7MbHrfA"

pasta_eight = ">>> Saving kpop hours\n\nhttps://www.youtube.com/watch?v=B54wPt-vbF0"

pasta_nine = ">>> **Male teacher calls my name in the roll**\n\nMe: https://www.youtube.com/watch?v=4RijMAvIawY"

pasta_ten = ">>> Stay safe on the road\n\nhttps://www.youtube.com/watch?v=wsXf9P4hR2s"

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
        # 157 kpop idols in txt file jan 15 2020
        theIndex = randint(0, 156)
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
        owm = pyowm.OWM('YOUR_OWM_API_GOES_HERE')
        observation = owm.weather_at_place("your_city,your_country_abbreviation")
        w = observation.get_weather()
        temperature = w.get_temperature('celsius')
        detailed_description = w.get_detailed_status()
        cloud_coverage = w.get_clouds()
        wind = w.get_wind()
        humidity = w.get_humidity()
        pressures = w.get_pressure()
        uvi = owm.uvindex_around_coords(latitude, longtitude)
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

        big_message = f'>>> **Weather Forecast**   \n\nObservations:    :mag:\n{detailed_description}\n\nWind:    :dash:\nSpeed - {round(wind["speed"] * 1.6)} kilometres/hour\nDirection - {wind_direction} @ {wind["deg"]}°\n\nTemperature:    :thermometer_face:\nCurrent - {round(temperature["temp"])}°C\nMaximum - {round(temperature["temp_max"])}°C\nMinimum - {round(temperature["temp_min"])}°C\n\nHumidity and Clouds:    :cloud:\nHumidity - {humidity}%\nCloud Coverage - {cloud_coverage}%\n\nAtmospheric Pressure:    :thermometer:\nCurrent Pressure - {pressures["press"]} hPa\n\nUV:    :sunny:\nLevel - {round(uv_level)}   ({uv_message})\nExposure Risk - {exposure_risk}\n\nTime:    :clock:\nCurrent Time in 24H Format: {current_time}'
        await asyncio.sleep(900)
        await channel.send(big_message)
        await asyncio.sleep(interval)


client.loop.create_task(copy_pasta())
client.loop.create_task(happy_feelings())
client.loop.create_task(current_weather())

client.run('YOUR_DISCORD_BOT_TOKEN_GOES_HERE')
