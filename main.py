import discord
from discord import app_commands
from discord.ext import commands

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())


class abot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=819767461330944010))
        self.synced = True
        print("I'm ready!")


bot = abot()
tree = app_commands.CommandTree(bot)


@tree.command(name="ping", description="pings the user", guild=discord.Object(id=819767461330944010))
async def self(interaction: discord.Interaction):
    await interaction.response.send_message("Pong")


@tree.command(name="fu", description="pings the user", guild=discord.Object(id=819767461330944010))
async def self(interaction: discord.Interaction):
    await interaction.response.send_message("Ur mom")


with open('token.txt') as f:
    TOKEN = f.readline()

bot.run('MTA1NTI0NjA3MDgzMTEzMjczMw.Ggi4zi.ULCL_Ht5JGSFiO4Hn_yRDANECbxd8rok0E2VVc')