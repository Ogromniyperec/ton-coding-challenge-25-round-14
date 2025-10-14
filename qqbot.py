from nonebot import get_driver, on_command
from nonebot.adapters.onebot.v11 import Adapter
import nonebot

nonebot.init()
driver = get_driver()
driver.register_adapter(Adapter)

ping = on_command("ping")

@ping.handle()
async def _(bot, event):
    await ping.finish("pong")

if __name__ == "__main__":
    nonebot.run()
