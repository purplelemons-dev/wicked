
import builtins
from datetime import datetime as dt
from typing import Callable, Any

def log(*args, **kwargs) -> None:
    args = map(str, args)
    LOG_STR = dt.now().strftime("%H:%M:%S %Y/%m/%d")
    LOG_STR += " [WickedBot]"
    builtins.print(LOG_STR, *args, **kwargs)

# no i dont want to type log instead of print, its easier just to type print
# also i can just comment out the line in bot.py
def print(*args, **kwargs) -> None:
    log(*args, **kwargs)

class Task:
    def __init__(self,func:Callable,args:tuple[Any]=tuple(),kwargs:dict[str,Any]=dict()) -> None:
        self.func:Callable = func
        self.args:tuple[Any] = args
        self.kwargs:dict[str,Any] = kwargs

    def __str__(self) -> str:
        return f"{self.func.__name__}({self.args=},{self.kwargs=})"
    
    def __call__(self) -> Any:
        return self.func(*self.args,**self.kwargs)
