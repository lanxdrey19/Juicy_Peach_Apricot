import discord
import random
from random import randint
from discord.ext import commands, tasks
from itertools import cycle
import asyncio
import pyowm

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
            await message.channel.send('>>> Hello there! I am Sad Bot\nType **.commands** for the list of all commands\nFeel free to make suggestions in the **#suggestions** channel')
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
    await ctx.send(f'>>> OwO (>^.^)> (っ´∀｀)っ (っ⇀⑃↼)っ {member} ⊂(・﹏・⊂) ლ(･ω･*ლ) <(^.^<) OwO')


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
    await ctx.send('```css\n.8ball - Ask it a question (Will not work if no arguments are entered)\n\n.cheerup - Try this one if you are feeling down\n\n.dice - Rolls die\n\n.hug - Try this one on someone. Remember to tag them when using this command\n\n.ping - Checks latency\n\n.match - Ship yourself with your crush (Will not work if no arguments are entered)\n\n```')


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
    # 131 kpop idols in txt file jan 15 2020
    theIndex = randint(0,130)
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

    await ctx.send(">>> :blush: Here's another photo to cheer you up! :blush:\n\n")
    await ctx.send(f'>>> {random.choice(cheers)}')
    await ctx.send(f'{theirPhoto[theIndex]}')

CHANNEL = THE_CHANNEL_ID_GOES_HERE

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
>>> To be fair, you have to have a very high IQ to understand LOONA. The LOONAVERSE is extremely subtle, and without a solid grasp of music theory, a basic understanding of quantum physics and genetics, and lore development, most of the narrative will go over a typical stan's head. There's also Yves’s narcissistic outlook, which is deftly woven into her characterisation - her personal philosophy draws heavily from John Appleby literature, for instance. The fans understand this stuff; they have the intellectual capacity to truly appreciate the depths of the lore, to realize that they're not just stories- they say something deep about LIFE. As a consequence people who dislike Loona truly ARE idiots- of course they wouldn't appreciate, for instance, the subtlety in Haseul’s existencial lyric "dari tteugo, naneun niga doeeo ganeyo," which itself is a cryptic reference to Harper Lee's American classic The Catcher in the Rye I'm smirking right now just imagining one of those addlepated simpletons scratching their heads in confusion as Jaden Jeong's genius unfolds itself on their mobile phone screens. What fools... how I pity them. 😂 And yes by the way, I DO have a 이달의 소녀 tattoo. And no, you cannot see it. It's for the ladies' eyes only- And even they have to demonstrate that they're within 18.6 IQ points of my own (preferably lower) beforehand.
"""

pasta_four = ">>> This is a Yukika Discord Server Fanclub now. I’m quitting Sadboiclique\n\nhttps://scontent.fakl6-1.fna.fbcdn.net/v/t1.0-9/60687052_2186537251454307_3625354170539704320_o.jpg?_nc_cat=111&_nc_ohc=OJaMVrdvlbIAX9KZdt2&_nc_ht=scontent.fakl6-1.fna&oh=be8e87a8b2844c8f24633a1623dce8da&oe=5EA26B77"

pasta_five = ">>> Hosting a Cup-sleeve event for the three members of Yukika Discord Server Fanclub :muscle_tone5: :fire: :100: :ok_hand_tone5:"

pasta_six = ">>> https://www.youtube.com/watch?v=7_ARMGdeQOM"

pasta_seven = ">>> https://www.youtube.com/watch?v=f-PK7MbHrfA"

pasta_eight = ">>> Saving kpop hours\n\nhttps://www.youtube.com/watch?v=B54wPt-vbF0"


@client.event
async def copy_pasta():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL)
    interval = 895

    while not client.is_closed():
        pastaArray = [pasta_one, pasta_two, pasta_three, pasta_four, pasta_five, pasta_six, pasta_seven, pasta_eight]
        await asyncio.sleep(5)
        await channel.send(random.choice(pastaArray))
        await asyncio.sleep(interval)


@client.event
async def happy_feelings():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL)
    interval = 590

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
        # 131 kpop idols in txt file jan 15 2020
        theIndex = randint(0, 130)
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
        await asyncio.sleep(10)
        await channel.send(messageTotal)
        await asyncio.sleep(interval)


@client.event
async def current_weather():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL)
    interval = 1200

    while not client.is_closed():
        owm = pyowm.OWM('YOUR_OPEN_WEATHER_MAP_API_GOES_HERE')
        observation = owm.weather_at_place("YOUR_CITY_GOES_HERE,YOUR_COUNTRY_IN_INITIAlS_GOES_HERE")
        w = observation.get_weather()
        temperature = w.get_temperature('celsius')
        detailed_description = w.get_detailed_status()
        cloud_coverage = w.get_clouds()
        wind = w.get_wind()
        humidity = w.get_humidity()
        pressures = w.get_pressure()
        uvi = owm.uvindex_around_coords(36.8485, 174.7633)
        exposure_risk = uvi.get_exposure_risk()

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

        big_message = f'>>> **Weather Forecast in Auckland, New Zealand**\n\nDescription:\n{detailed_description}\n\nWind:\nSpeed - {round(wind["speed"] * 1.6)} kilometres/hour\nDirection - {wind_direction} @ {wind["deg"]}°\n\nTemperature:\nCurrent - {temperature["temp"]}°C\nMax - {temperature["temp_max"]}°C\nMin - {temperature["temp_min"]}°C\n\nHumidity and Clouds:\nHumidity - {humidity}%\nCloud coverage - {cloud_coverage}%\n\nAtmospheric Pressure:\nCurrent Pressure - {pressures["press"]} hPa\n\nUV:\nExposure Risk - {exposure_risk}\n\n'
        await channel.send(big_message)
        await asyncio.sleep(interval)


client.loop.create_task(copy_pasta())
client.loop.create_task(happy_feelings())
client.loop.create_task(current_weather())

client.run('YOUR_DISCORD_BOT_TOKEN_GOES_HERE')
