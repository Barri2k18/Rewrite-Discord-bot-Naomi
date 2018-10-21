import os
import sys
import time
import asyncio
import traceback
import aiohttp

import discord
from discord.ext import commands

prefix = os.getenv("PREFIX")

class Naomi(commands.AutoShardedBot):
    def __init__(self, **kwargs):
        super().__init__(command_prefix=commands.when_mentioned_or(kwargs.pop("PREFIX")), case_insensitive=kwargs.pop("CINS"), fetch_offline_members=kwargs.pop("FOM"))
        
        self.session = aiohttp.ClientSession(loop=self.loop)
        self.game_activity = 'playing'
        self.extensions = ['cogs.member.fun',
                           'cogs.member.info',
                           'cogs.member.music',
                           'cogs.member.utils',
                           'cogs.system.error_handler',
                           'cogs.system.logger',
                           'cogs.admin',
                           'cogs.owner']

        self.messages = [f'{len(self.guilds)} серверов!',
                         f'{len(self.users)} участников!',
                         f'{len(self.emojis)} эмодзи!',
                         f'{len([x.name for x in self.commands if not x.hidden])} команд!',
                         f'{kwargs.pop("PREFIX")}help']
                         
    def __repr__(self):
        return "Я - Бот Наоми :)"

    async def presence(self):
        while not self.is_closed():
            for msg in messages:
                if game_activity == 'streaming':
                    await self.change_presence(activity=discord.Streaming(name=msg, url='https://www.twitch.tv/%none%'))
                    await asyncio.sleep(10)
                if game_activity == 'playing':
                    await self.change_presence(activity=discord.Game(name=msg))
                    await asyncio.sleep(10)
    
    def run(self):
        self.remove_command('help')
        for extension in self.extensions:
            try:
                self.load_extension(extension)
            except Exception as e:
                print(f'[{time.ctime()}] Не удалось загрузить модуль {extension}.', file=sys.stderr)
                traceback.print_exc()
        super().run(os.getenv('TOKEN'), reconnect=True)
        
    async def on_ready(self):
        print(f'[{time.ctime()}] Подключение успешно осуществлено!\nВ сети: {self.user}')
        self.loop.create_task(presence())

if __name__ == '__main__':
    Naomi().run(**{"PREFIX": os.getenv("PREFIX"), "CINS": True, "FOM": False})
