
# This script is executed from `python -m wicked`.
# This should be used if you are not very familiar
# with Python and/or Discord.py. If you are, you
# can read through the source code and modify it
# to your liking.

from .vars import *
from json import dump, load
from pyfiglet import Figlet
from threading import Thread
from .bot import Bot
from asyncio import run as async_run
from .utils import *

print(Figlet().renderText("Wicked Bot Engine   > : )"))
print(WELCOME_MESSAGE)

# The bot can be set up pretty much entirely from .wikedconfig.json

try:
    with open(CONFIG_NAME) as f:
        config = f.read()
# We can make a config file.
except FileNotFoundError:
    print("No `.wickedconfig.json` file found. Creating one...")
    with open(CONFIG_NAME, "w") as f:
        dump({
            "token": input("Enter your bot token: ")
        }, f, indent=4)
    print("Done! Please fill out the appropriate fields in the config file and restart the bot.")

# Read config and load bot with settings.
with open(CONFIG_NAME) as f:
    bot = Bot(kwargs=load(f))

bot_run_thread = Thread(target=bot.run)
bot_run_thread.start()

async def main():
    while True:
        user_input = input(">>> ")
        if user_input == "exit":
            bot.running = False
            break
        else:
            try:
                task = Task(
                    func = bot.test_channel.send,
                    args = (user_input,)
                )
                bot.tasks["always"].append(task)
            except Exception as e:
                # we want to fail silently because i (and probably other people)
                # send commands to the console before the bot is set up
                print(e)

async_run(main())
