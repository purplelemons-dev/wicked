
from typing import Any


class Testclass:
    def __init__(self,thing):
        self.thing = thing

    def __call__(self, who:str="this guy") -> Any:
        def wrapper(func):
            print(who)
            self.thing = who
            return func
        return wrapper

a = Testclass("thing")
print(f"{a.thing=}")

@a(who="a guy")
def testfunc(): 
    print("testfunc run")

testfunc()
print(f"{a.thing=}")
