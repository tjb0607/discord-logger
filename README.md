# discord-logger
WARNING: Self-botting is technically against the rules, so this script could potentially get you banned.

This script is intended for logging private messages, but should work with any other channels, including group chats. It fetches 200 messages per second, so it will take a quite while to download longer chat logs.

## usage
```
python3 /path/to/discordlogger.py <channel id>
```
to find the channel id, the easiest way is to open discord in your browser and take the number at the end of the url.

## output

it will output to `./discord-<channel id>.log`, and also create a hidden file called `./.discord-<channel id>.log.lastmessageid` containing the last message id. If you run the script again on the same channel, it will continue where it last finished.

## missing features

I'm too lazy to add these things:

* actually listening to discord ratelimit errors(!!!!!!!)

* ability to resume after being interrupted (e.g. by ctrl+c)

* proper command line args, like the ability to specify a message id to start at, or the ability to choose a specific outfile location, or an option to show the messages to stdout as they're being saved

I won't be actively developing this, but feel free to fork it yourself.

## example output file
```
[2017-07-28 03:43:50] <tjb0607> i love jade harley <3
[2017-07-28 03:45:26] <tjb0607> 
[[ attachment: https://cdn.discordapp.com/attachments/304892646395084801/340444637498048522/my_wife.png ]]
[2017-07-28 03:47:38] <tjb_alt> shes so cute
```
