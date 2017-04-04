# -*- coding: utf-8 -*-
import discord
import asyncio
import wkurw
import mowa
import random
import linecache
import skojarzenia

client = discord.Client()

wnerwiaj = -1

@client.event
async def on_message(message):
    author = message.author
    mhroczus = client.user

    if author == mhroczus:
        return

    else:                      
        if message.content.find('ChannelID') > -1:
            await client.send_message(message.channel, message.channel.id)

        if message.content.find('Witaj, Mhroczusiu') > -1:
            await mowa.powitanie(author, message)

        if message.content.find('Powiedz tata, Mhroczusiu') > -1:
            await mowa.naukamowienia(author, message)

        if message.content.find('Możesz mówić, Mhroczusiu') > -1: 
            await wkurw.denerwuj(client, message, mhroczus)

        if message.content.startswith('...'):
            await mowa.kropek(author, message)

        if message.channel.id == '241958978446295040' or message.channel.id == '241580830898520074':
            if message.content.startswith('?'):
                await skojarzenia.check(author, message);
            
client.run('MjQxOTM2MDM5NjcxODg5OTIy.CvZJLQ._Pqas317uMsN0sWNrClKgYjuLIc')