# -*- coding: utf-8 -*-
import discord
import asyncio

client = discord.Client()

async def powitanie(author, message):
    await client.login('MjQxOTM2MDM5NjcxODg5OTIy.CvZJLQ._Pqas317uMsN0sWNrClKgYjuLIc')
    user = author.name
    await client.send_message(message.channel, 'Witaj, %s ;)' %user)
    return

async def naukamowienia(author, message):
    await client.login('MjQxOTM2MDM5NjcxODg5OTIy.CvZJLQ._Pqas317uMsN0sWNrClKgYjuLIc')

    if (author.id == '225293594481655811'):
        await client.send_message(message.channel, "TATA!!!")
        return
    else:
        await client.send_message(message.channel, "Ty nie tata ;-;")
        return

async def kropek(author, message):
    await client.login('MjQxOTM2MDM5NjcxODg5OTIy.CvZJLQ._Pqas317uMsN0sWNrClKgYjuLIc')

    await client.send_message(message.channel, "...")
    return;