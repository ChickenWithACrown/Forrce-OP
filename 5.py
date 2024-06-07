import asyncio
import random
import sys
import time
from mineflayer_py import MinecraftClient
from mineflayer_py.bot import Bot

class MyBot(Bot):
    async def on_spawn(self):
        self.stealth = True
        self.set_gamemode('spectator')

    async def on_chat(self, username, message):
        if username == self.username:
            self.chat(message)
        elif self.username in message:
            self.chat('REDACTED')

async def main():
    username = 'ChickenWithCrown'
    server = 'hypixel.net'
    auth = 'sessions.json'
    bot = MyBot(server, username, auth)

    try:
        await bot.start()
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        await bot.stop()

if __name__ == '__main__':
    asyncio.run(main())
