import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
client = commands.Bot(command_prefix="!")
@client.event
async def on_ready():
    game = discord.Game("Amid Ye")
    if bot_public:
        print("Bot is public, disable this in the Discord Developer Dashboard.")
        exit
    await client.change_presence(status=discord.Status.online, activity=game)
    print("Bot is ready!")
    print("Signed in as Mercury: ")

@client.event
async def on_message(message):
    empty_array = []
    modmail_channel = discord.utils.get(client.get_all_channels(), name="modmail")

    if message.author == client.user:
        return
    if str(message.channel.type) == "private":
        if message.attachments != empty_array:
            files = message.attachments
            await modmail_channel.send("<@" + message.author.id + ">: ")

            for file in files:
                await modmail_channel.send(file.url)
        else:
            await modmail_channel.send("<@" + str(message.author.id) + ">: " + message.content)

    elif str(message.channel) == "modmail" and message.content.startswith("<"):
        member_object = message.mentions[0]
        if message.attachments != empty_array:
            files = message.attachments
            await member_object.send("**[MOD]** " + "**" + message.author.display_name + "**: ")

            for file in files:
                await member_object.send(file.url)
        else:
            index = message.content.index(" ")
            string = message.content
            mod_message = string[index:]
            await member_object.send("**[MOD]** " + "**" + message.author.display_name + "**: " + mod_message)

@client.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.green()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)

@client.command()
async def commands(ctx):
    embed = discord.Embed(
        title="Help Menu",
        description=" ",
        color=discord.Color.green()
    )
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/766016816710418473/e9f7ccddf1a708e96b503555df0ffc4c.png?size=128')
    embed.add_field(name="!help", value="The page you're looking at right now!", inline=True)
    embed.add_field(name="!server", value="Shows basic server information.", inline=True)
    #embed.add_field(name="Region", value=region, inline=True)
    #embed.add_field(name="Member Count", value=

    await ctx.send(embed=embed)


client.run('no leaks here- get your own token')
