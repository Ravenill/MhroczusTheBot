import discord
import asyncio
from _winapi import NULL
import os
import time
import linecache

client = discord.Client()

async def check(author, message):
    await client.login('MjQxOTM2MDM5NjcxODg5OTIy.CvZJLQ._Pqas317uMsN0sWNrClKgYjuLIc')
    istnieje = 0

    if os.path.isfile("check.mhro"):
        pass
    else:
        print("Plik nie Istnieje... \nTworzenie nowego pliku...")
        plik = open('check', "w")
        plik.close()    

    try:
        plik = open('check.mhro', "rU")
        try:
            ilosc = len(plik.readlines())
            print(ilosc)
            
            for i in range (2,ilosc,2):
                haslo = linecache.getline('check.mhro', i)
                autor = linecache.getline('check.mhro', i-1)

                print(i)
                print(haslo)

                if message.content == haslo:
                    await client.send_message(message.channel, "Dane skojarzenie dodano przez %s" %autor)
                    istnieje = 1

            if istnieje == 0:
                plik.close()
                plik = open('check.mhro', "a")

                plik.write(author.name)
                plik.write('\n')
                plik.write(message.content)
                plik.write('\n')

                print("%s - dodano przez %s" % (message.content, author.name))

        finally:
            plik.close()
            
    except IOError:
        print("Mamy bledy")