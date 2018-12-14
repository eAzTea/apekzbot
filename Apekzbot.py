import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Willkommen beim ApekZ Clan! Melde dich gleich bei einen Operator, dieser wird dir dann alles erklären. Wenn keiner online ist dann melde dich bei jemanden von der Leitung! Wir wünschen dir VIEL SPAß ')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='Willkommen in Apekz Clan'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '$help':
        await client.send_message(message.channel,'Wenn du neu bist melde dich zuerst bei einen Operator!')
client.run('NTIyNzg5Njc5ODcxODE5Nzg2.DvQFhw.INWP8K064raDypBIw5lw50ztT8M')
