import discord
import asyncio
import os
import random
import linecache
import json
import youtube_dl
from discord.ext import commands

bot = commands.Bot(command_prefix=";;")

bots = 2
players = {}
queues = {}
noxp_channels = {
    "458350360193400832"
    "458699265426849793"
    "458699295382831134"
}


if not os.path.isfile("../txt_files/bot_token.txt"): #Authentication stuff
    print("Please insert your bot token")
    token = input()
    token_txt = open(r"../txt_files/bot_token.txt", "a+")
    token_txt.write(token)
    token_txt.close

@bot.event
async def on_member_join(member): #Welcome message
    server = member.server
    fmt = 'Hey {0.mention}, welcome to the {1.name}!\nPlease read the rules and have fun!'
    await bot.send_message(discord.Object(id='458347412910768128'), fmt.format(member, server))
    print(member, "joined the the", server)
    with open("../txt_files/users.json", "r") as f:
        users = json.load(f)
    await update_data(users, member)
    with open("../txt_files/users.json", "w") as f:
        json.dump(users, f)

@bot.event
async def on_member_remove(member):
    print("{} left the {}".format(member, member.server))

@bot.event #Startup message for host
async def on_ready():
    await bot.change_presence(game=discord.Game(name="with Yvar's sanity"))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True) 
async def r1(ctx): #R1 command
    """Displays rule 1"""
    embed=discord.Embed(title="Rule 1", description=linecache.getline("../txt_files/rules.txt", 1))
    await bot.say(embed=embed)
    print(ctx.message.author, "used the r1 command in the", ctx.message.channel, "channel")
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def r2(ctx): #R2 command
    """Displays rule 2"""
    embed=discord.Embed(title="Rule 2", description=linecache.getline("../txt_files/rules.txt", 2))
    await bot.say(embed=embed)
    print(ctx.message.author, "used the r2 command in the", ctx.message.channel, "channel")
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def r3(ctx): #R3 command
    """Displays rule 3"""
    embed=discord.Embed(title="Rule 3", description=linecache.getline("../txt_files/rules.txt", 3))
    await bot.say(embed=embed)
    print(ctx.message.author, "used the r3 command in the", ctx.message.channel, "channel")
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def r4(ctx): #R4 command
    """Displays rule 4"""
    embed=discord.Embed(title="Rule 4", description=linecache.getline("../txt_files/rules.txt", 4))
    await bot.say(embed=embed)
    print(ctx.message.author, "used the r4 command in the", ctx.message.channel, "channel")
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def r5(ctx): #R5 command
    """Displays rule 5"""
    embed=discord.Embed(title="Rule 5", description=linecache.getline("../txt_files/rules.txt", 5))
    await bot.say(embed=embed)
    print(ctx.message.author, "used the r5 command in the", ctx.message.channel, "channel")
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def r6(ctx): #R6 command
    """Displays rule 6"""
    embed=discord.Embed(title="Rule 6", description=linecache.getline("../txt_files/rules.txt", 6))
    await bot.say(embed=embed)
    print(ctx.message.author, "used the r6 command in the", ctx.message.channel, "channel")
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def r7(ctx): #R7 command
    """Displays rule 7"""
    embed=discord.Embed(title="Rule 7", description=linecache.getline("../txt_files/rules.txt", 7))
    await bot.say(embed=embed)
    print(ctx.message.author, "used the r7 command in the", ctx.message.channel, "channel")
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def r8(ctx): #R8 command
    """Displays rule 8"""
    embed=discord.Embed(title="Rule 8", description=linecache.getline("../txt_files/rules.txt", 8))
    await bot.say(embed=embed)
    print(ctx.message.author, "used the r8 command in the", ctx.message.channel, "channel")
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def naru(ctx): #Naru command
    """Naru command (for science)"""
    RNG = random.randint(0, 2)
    if RNG == 0:
        await bot.say("Cus itsa  SMALL DICK BOY")
    if RNG == 1:
        await bot.say("The creepy thing?")
    if RNG == 2:
        await bot.say("'I need yvar to wake tf up for this'\nNo you don't. Leave me the fuck alone")
    print(ctx.message.author, "used the naru command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def gny(ctx): #Gny command
    """Gny command (for science)"""
    RNG = random.randint(0, 2)
    if RNG == 0:
        await bot.say("Ya shaveing smooth and my crack hard to do")
    if RNG == 1:
        await bot.say("Ok hugs mmm u not still u know thinking ur bad right")
    if RNG == 2:
        await bot.say("Clenches butt cheeks so poop doesn't come out")
    print(ctx.message.author, "used the naru command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def hug(ctx, user: discord.Member):
    await bot.say("**hugs{0.mention}**".format(user))
    await bot.send_file(ctx.message.channel, "../imgs/hug.gif")

@bot.command(pass_context=True)
async def mantis(ctx): #Mantis command
    """Mantis commmand (for actual science)"""
    RNG = random.randint(1, 19)
    await bot.say(linecache.getline("../txt_files/mantis.txt", RNG))
    print(ctx.message.author, "used the mantis command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member): #Ban command
    """Ban a member"""
    await bot.ban(member)
    await bot.send_message(ctx.message.channel, "{0.mention} is now banned!".format(member))
    print(ctx.message.author, "banned", member)

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def kick(ctx, member: discord.Member): #Kick command
    """Kick a member"""
    await bot.kick(member)
    await bot.send_message(ctx.message.channel, "{0.mention} is now kicked!".format(member))
    print(ctx.message.author, "kick", member)

@bot.command(pass_context=True)
async def membercount(ctx): #Membercount command
    """Displays the total amount of members"""
    totalmembers = ctx.message.server.member_count-bots
    await bot.say(f"the {ctx.message.server} now has {totalmembers} members!")
    print(ctx.message.author, "used the membercount command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def poll(ctx): #Poll command
    await bot.add_reaction(ctx.message, "👍")
    await bot.add_reaction(ctx.message, "👎")
    print(ctx.message.author, "used the poll command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def quote(ctx, msg): #Quote command
    await bot.say(msg)
    await bot.delete_message(ctx.message)
    print(ctx.message.author, "used the quote command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
@commands.has_permissions(manage_nicknames=True)
async def nick(ctx, user: discord.Member, nick):
    await bot.change_nickname(user, nick)
    await bot.say("changed nickname to {}!".format(nick))
    print("{} changed {}'s nickname to {}".format(ctx.message.author, user, nick))

@bot.command(pass_context=True)
@commands.has_permissions(manage_nicknames=True)
async def checkuser(ctx, user: discord.Member):
    await bot.say("Username: {}\nUser ID: {}\nProfile picture: {}\nUser is a bot: {}\nDisplay name: {}\nDiscord account created at: {}".format(user.name, user.id, user.avatar_url, user.bot, user.display_name, user.created_at))
    print("{} used the checkuser command on {}".format(ctx.message.author, user))

@bot.command(pass_context=True)
@commands.has_permissions(manage_nicknames=True)
async def clearnick(ctx, user: discord.Member):
    await bot.change_nickname(user, "")
    await bot.say("cleared {}'s nickname!".format(user))
    print("{} cleared {}'s nickname".format(ctx.message.author, user))

@bot.command(pass_context=True)
@commands.has_permissions(manage_channels=True)
async def takevent(ctx, user: discord.Member): #Takevent command
    role = discord.utils.get(ctx.message.author.server.roles, name="no-vent")
    await bot.add_roles(user, role)
    await bot.say("{0.mention} cannot message in the vent channel anymore.".format(user))
    print(ctx.message.author, "took vent acces from", user)

@bot.command(pass_context=True)
@commands.has_permissions(manage_channels=True)
async def givevent(ctx, user: discord.Member): #Givevent command
    role = discord.utils.get(ctx.message.author.server.roles, name="no-vent")
    await bot.remove_roles(user, role)
    await bot.say("{0.mention} can now message in the vent channel again.".format(user))
    print(ctx.message.author, "gave vent acces back to", user)

@bot.event
async def on_message(message):
    with open("../txt_files/users.json", "r") as f:
        users = json.load(f)
    await update_data(users, message.author)
    await add_experience(users, message.author, 5)
    await level_up(users, message.author, message.channel)
    with open("../txt_files/users.json", "w") as f:
        json.dump(users, f)
    await bot.process_commands(message)

async def update_data(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]["experience"] = 0
        users[user.id]["level"] = 1

async def add_experience(users, user, exp):
    users[user.id]["experience"] += exp

async def level_up(users, user, channel):
    experience = users[user.id]["experience"]
    lvl_start = users[user.id]["level"]
    lvl_end = int(experience ** (1/4))
    if lvl_start < lvl_end:
        await bot.send_message(channel, "{} has leveled up to level {}!".format(user.mention, lvl_end))
        users[user.id]["level"] = lvl_end

def check_queue(id):
    if queues[id] != []:
        player = queues[id].pop(0)
        players[id] = player
        player.start()

@bot.command(pass_context=True)
async def join(ctx): #Join command
    channel = ctx.message.author.voice.voice_channel
    await bot.join_voice_channel(channel)
    await bot.say("Joined the {} channel".format(channel))
    print(ctx.message.author, "used the join command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def leave(ctx): #Leave command
    server = ctx.message.server
    channel = ctx.message.author.voice.voice_channel
    voice_client = bot.voice_client_in(server)
    await voice_client.disconnect()
    await bot.say("left the {} channel".format(channel))
    print(ctx.message.author, "used the leave command in the", ctx.message.channel, "channel")

@bot.command(pass_context=True)
async def play(ctx, url): #Play command
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
    players[server.id] = player
    player.start()
    bot.say("Now playing the song.")
    print(ctx.message.author, "is now playing a song in", ctx.message.author.voice.voice_channel, "in the", ctx.message.server)

@bot.command(pass_context=True)
async def pause(ctx): #Pause command
    id = ctx.message.server.id
    players[id].pause()
    await bot.say("Paused the music")

@bot.command(pass_context=True)
async def resume(ctx): #Resume command
    id = ctx.message.server.id
    players[id].resume()
    await bot.say("Resumed the music")

@bot.command(pass_context=True)
async def queue(ctx, url): #Queue command
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
    if server.id in queues:
        queues[server.id].append(player)
    else:
        queues[server.id] = [player]
    await bot.say("Song queued.")
    print(ctx.message.author, "is now playing a song in", ctx.message.author.voice.voice_channel, "in the", ctx.message.server)

@bot.command(pass_context=True)
async def skip(ctx):
    print()

token_txt = open(r"../txt_files/bot_token.txt", "r")
token = token_txt.read()
bot.run(token)
token_txt.close
