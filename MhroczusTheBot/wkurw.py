# -*- coding: utf-8 -*-
import discord
import asyncio
import linecache
import random

client = discord.Client()

async def denerwuj(bot, message, mhroczus):
    await client.login('MjQxOTM2MDM5NjcxODg5OTIy.CvZJLQ._Pqas317uMsN0sWNrClKgYjuLIc')

    print("Uruchomiono tryb wnerwiania")

    while(1):
        #print("While")
        msg = await bot.wait_for_message()
        #print(msg.content)

        if msg.author == mhroczus:
            #print("Mhroczus jest autorem")
            pass

        else:
            if msg.content.find('WYSTARCZY') > -1:
                if (msg.author.id == '225293594481655811'):
                    await client.send_message(message.channel, "No dobra...")
                    print("Wyjscie z trybu wnerwiania")
                    break;
                else:
                    await client.send_message(message.channel, "Słucham się tylko Ojca!")
            else:
                ilosc = len(open('wkurw.mhro', 'rU').readlines())

                losowanie = random.randint(1, ilosc)
                tekst = linecache.getline('wkurw.mhro', losowanie)
    
                await client.send_message(message.channel, tekst)