# -*- coding: utf-8 -*-
import discord
import asyncio
import linecache
import random

client = discord.Client()

async def denerwuj(message):
    await client.login('MjQxOTM2MDM5NjcxODg5OTIy.CvZJLQ._Pqas317uMsN0sWNrClKgYjuLIc')

    print("Uruchomiono tryb wnerwiania")

    while(true):
        if message.content.find('WYSTARCZY') > -1:
            if (author.id == '225293594481655811'):
                await client.send_message(message.channel, "No dobra...")
                break;
            else:
                await client.send_message(message.channel, "Słucham się tylko Ojca!")
        else:
            ilosc = len(open('wkurw.mhro', 'rU').readlines())

            losowanie = random.randint(1, ilosc)
            tekst = linecache.getline('wkurw.mhro', losowanie)
    
            await client.send_message(message.channel, tekst)