#!/usr/bin/env python3

import discord
import time
import asyncio
from collections import OrderedDict
from discord.ext import commands

token = token = open("token.txt","r").readline()
client = commands.Bot(command_prefix = '!')

def get_int(user):
	global n
	f = open(f'n/{str(user)}','r')
	n = f.read()
	if len(n) > 2000:
		n = n[:1950]
	f.close()
	return n
            
def write_int(user):
    f = open('n/{}'.format(str(user)), 'w')
    c = n+1
    count = str(c)
    
    f.write(count)
    f.close

def rw(user):
    get_int(user)
    write_int(user)

def rem_dup(word):
	return "".join(OrderedDict.fromkeys(word))

def get_ncount(user):
	get_int('{}'.format(str(user)))
	print(n)
	global msg
	msg = 'This user has said {} Words'.format(n)
	return msg

@client.command()
async def test(ctx):
	await ctx.send('Alive')

@client.command()
async def count(ctx, user):
	uid = user
	get_ncount(uid)
	await ctx.send(msg)
	
@client.event
async def on_ready():
	print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	await client.process_commands(message)

	print(message.content)
	msgcon = message.content.casefold()
	print(msgcon)
	msgcon = msgcon.replace(" ","")
	print(msgcon)
	msgcon = rem_dup(msgcon)
	print(msgcon)

	if '' in msgcon or '' in msgcon or '' in msgcon or msgcon == '':
		print('Detected')
		print(message.author, message.author.id,'\n')
		uid = message.author.id
		rw(uid)
		

client.run(token)
