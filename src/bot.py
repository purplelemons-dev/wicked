
try:
    assert __name__ != "__main__"
except AssertionError:
    raise RuntimeError("This file should not be run directly. Please run `python -m wicked` instead.")

from typing import Any, Callable
import discord # Py-cord 2.4.0
from .utils import *
import time

class Bot(discord.Client):
    running:bool
    
    def __init__(self, *args, **kwargs) -> None:
        # I don't understand why i need to do kwargs["kwargs"].
        self.token = kwargs["kwargs"].pop("token")
        # Translates events to a list of tasks for that event.
        self.tasks:dict[str,list[Task]] = {
            "always": []
        }

        intents = discord.Intents.default()
        intents.message_content = True
        return super().__init__(intents=intents,*args, **kwargs)

    async def on_ready(self) -> None:
        print(f"Logged in as {self.user.name}#{self.user.discriminator}")
        self.test_channel = self.get_channel(888509258541461554)

        # main thread
        while self.running:
            for task in self.tasks["always"]:
                # idk this code is p cool ig, its nice using <class>.__call__
                await task()
                self.tasks["always"].remove(task)
            # maybe ill let people adjust the polling rate later, but .5 is fine for me ¯\_(ツ)_/¯
            time.sleep(.5)
        await self.close()

    def task(self,when:str="always",args:tuple=None) -> Callable:
        """
        This is a decorator that adds a task to the bot's main loop.
        Use it like this:
        ```
        @bot.task(when="always|...")
        def my_task():
            pass
        ```
        """
        def wrapper(func:Callable):
            self.tasks[when].append(Task(func,args))
            return func
        return wrapper

    def run(self, *args: Any, **kwargs: Any) -> None:
        self.running = True
        return super().run(token=self.token,*args, **kwargs)
