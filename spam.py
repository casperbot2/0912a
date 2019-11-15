import discord
import time
import random
import sys

client = discord.Client()

@client.event
async def on_ready():
	await send()

async def berichtKiezer():
	bericht = input("# Message: ")
	message = bericht
	return message

async def chooseChannel():
	keuze = input("# Spam a server or user? (s/u) ")
	if keuze == "s":
		channelID = input("# Channel ID: ")
		kanaal = client.get_channel(channelID)
		return kanaal
	elif keuze == "u":
		userID = input("# User ID: ")
		server = input("# Server ID: ") #Random server where both you and the target are in
		kanaal = client.get_server(server).get_member(userID)
		return kanaal
	else:
		print("! You can only choose between s or u!")
		print("! As a punishment, you have to relad the script!")
		sys.exit()

async def aantalKiezer():
	aantal = input("# Message count: ")
	try:
		aantal = int(aantal)
		return aantal
	except ValueError:
		print("! This is not a valid number!")
		print("! As a punishment, you have to reload the script!")
		sys.exit()

async def send():
	kanaal = await chooseChannel()
	message = await berichtKiezer()
	aantal = await aantalKiezer()
	count = 0
	while (count < aantal):
		number = str(random.randint(1, 9)) #Every message ends with a random number. You can get banned for sending the same message over and over. So this way all the messages are slightly different
		await client.send_message(kanaal, (message + " " + number))
		count = count + 1
	opnieuw = input("# Wanna spam again? (Y/n)")
	if opnieuw == 'Y':
		await send()
	else:
		print("! OK. You can close this window now.")

client.run("insert_token_here", bot=False)