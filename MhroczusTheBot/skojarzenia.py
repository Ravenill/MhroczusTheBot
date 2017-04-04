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
        try:
            plik = open('check.mhro', "rU")
            ilosc = len(plik.readlines())
            print("Ilosc wersow wczytanych: ", ilosc)
            
            for i in range (2,ilosc+1,2):
                haslo = linecache.getline('check.mhro', i)
                autor = linecache.getline('check.mhro', i-1)

                print("Obrot: ", i)
                print("Haslo wczytane: ", haslo)
                print("Autor: ", autor)
                print("User wprowadzil: " , message.content)                

                if (message.content + '\n') == haslo:
                    print("Haslo i haslo sie zgadzaja\n")
                    await client.send_message(message.channel, "Dane skojarzenie zostalo użyte przez %s" %autor)
                    istnieje = 1
                    break;

            print("Wartosc istnieje wynosi: ", istnieje)
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