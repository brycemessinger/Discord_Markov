import os
import sys
import discord
from random import choice


def open_and_read_file(filenames):
    body = ''
    for filename in filenames:
        text_file = open(filename)
        body = body + text_file.read()
        text_file.close()

    return body


def make_chains(text_string):
    chains = {}

    words = text_string.split()
    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = words[i + 2]

        if key not in chains:
            chains[key] = []

        chains[key].append(value)

    return chains

def make_text(chains, char_limit=None):
    keys = list(chains.keys())
    key = choice(keys)
    words = [key[0], key[1]]
    while key in chains:
    
        if char_limit and len(' '.join(words)) > char_limit:
            break



        word = choice(chains[key])
        words.append(word)
        key = (key[1], word)

    return ' '.join(words)


filenames = sys.argv[1:]

text = open_and_read_file(filenames)

chains = make_chains(text)

client = discord.Client()


@client.event
async def on_ready():
    print(f'Successfully connected! Logged in as {client.user}.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # await message.channel.send(make_text(chains))
    await message.channel.send("Hello")


client.run(os.environ['DISCORD_TOKEN'])