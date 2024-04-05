import discord
import config
from discord.ext import commands
# Define the intents
intents = discord.Intents.all()
# Setting the message content intent to True is necessary to receive messages
intents.messages = True

# Initialize the client with the specified intents
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix=config.COMMAND_PREFIX, intents=intents)

async def on_ready():
    print(f'We have logged in as {bot.user}')

    bot.load_extension('my_cog')
    bot.load_extension('my_cog2')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('MTIyNTcyODg0MzE4NTM5MzY3OA.G1I0Dm.uWmcxFJmI7fjbl_XKGSUcJiSZV61hAMrhQgUCg')
