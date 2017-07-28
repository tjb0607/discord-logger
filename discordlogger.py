#!/usr/bin/python3

# WARNING: by using this, you are violating Discord's ToS and potentially putting yourself at risk of being banned!

import http.client
import json
import urllib
import time
import getpass
import os.path
import datetime
import sys
from dateutil.parser import parse

print("usage: python3 discordlogger.py <channel id>")

after = 0
channel = sys.argv[1]

if ( os.path.isfile('./.discord-' + channel + '.log.lastmessageid') ):
	infile = open('./.discord-' + channel + '.log.lastmessageid', 'r')
	after = int(infile.read())
	infile.close()

c = http.client.HTTPSConnection('discordapp.com', 443)

email = input("Email: ")
password = getpass.getpass("Password: ")
token = ""
c.request("POST", "https://discordapp.com/api/auth/login", json.dumps({"email": email, "password": password}), {"Content-type": "application/json"})
password = ""
response = json.loads(c.getresponse().read().decode("utf-8"))
if "mfa" in response and "ticket" in response:
	code = input("2FA code: ")
	c.request("POST", "https://discordapp.com/api/auth/mfa/totp", json.dumps({"ticket": response["ticket"], "code": code}), {"Content-type": "application/json"})
	response = json.loads(c.getresponse().read().decode("utf-8"))
token = response["token"]

outfile = open("./discord-" + channel + ".log", "a")
done = 0
while done == 0:
	c.request("GET", "https://discordapp.com/api/channels/" + channel + "/messages?" + urllib.parse.urlencode({"after": str(after), "limit": "50", "token": token}))
	response = c.getresponse()
	if response.status == 200:
		messages = json.loads(response.read().decode("utf-8"))
		if len(messages) > 0:
			for message in reversed(messages):
				outfile.write("[" + parse(message['timestamp']).astimezone(tz=None).strftime('%Y-%m-%d %H:%M:%S') + "] <" + message['author']['username'] + "> " + message['content'] + "\n")
				for a in message['attachments']:
					outfile.write('[[ attachment: ' + a['url'] + ' ]]\n')
			after = messages[0]['id']
		else:
			print("Last message ID: " + after)
			done = 1
	else:
		print("fatal error: api responded with status " + str(response.status))
		done = 1
	time.sleep(0.25)
outfile.close()

outfile = open("./.discord-" + channel + ".log.lastmessageid", "w")
outfile.write(after)
outfile.close()
