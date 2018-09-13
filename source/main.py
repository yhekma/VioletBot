import discord
import asyncio
import os
import random
import linecache
import json
import youtube_dl
from discord.ext import commands

def warnmember(member, warnmsg):
    global member_warns
    with open("../txt_files/warns.json", "r") as f:
        warns = json.load(f)
    if not member in warns:
        warns[member] = {}
        member_warns = 0
    if "warn" not in warns[member]:
        warns[member]["warn"] = warnmsg
        member_warns = 1
    elif "warn1" not in warns[member]:
        warns[member]["warn1"] = warnmsg
        member_warns = 2
    elif "warn2" not in warns[member]:
        warns[member]["warn2"] = warnmsg
        member_warns = 3
    elif "warn3" not in warns[member]:
        warns[member]["warn3"] = warnmsg
        member_warns = 4
    elif "warn4" not in warns[member]:
        warns[member]["warn4"] = warnmsg
        member_warns = 5
    with open("../txt_files/warns.json", "w") as f:
        json.dump(warns, f)

bot = commands.Bot(command_prefix=";;")

bots = 1
players = {}
queues = {}

if not os.path.isfile("../txt_files/bot_token.txt"): #Authentication stuff
    print("Please insert your bot token")
    token = input()
    token_txt = open(r"../txt_files/bot_token.txt", "a+")
    token_txt.write(token)
    token_txt.close

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def warn(ctx, member: discord.Member, warnmsg):
    warnmember(member.id, warnmsg)
    await bot.say("{}, you've been warned for the reason '{}', this is your {}th warning!".format(member, warnmsg, member_warns))
    print("{} warned {} for the reason '{}'".format(ctx.message.author, member, warnmsg))
    if member_warns == 3:
        await bot.kick(member)
        await bot.say("{} got an automated kick.".format(member))
        print("{} got an automated kick.".format(member))
    if member_warns == 5:
        await bot.ban(member)
        await bot.say("{} got an automated ban.".format(member))
        print("{} got an automated ban".format(member))

@bot.event
async def on_member_join(member): #Welcome message
    server = member.server
    fmt = 'Hey {0.mention}, welcome to the {1.name}!\nPlease read the rules and have fun!\nAlso, here, have a cookie! 🍪'
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
async def r(ctx, ruleNumb: int): #Rule command
    if ruleNumb < 9 and ruleNumb > 0:
        embed=discord.Embed(title="Rule {}".format(ruleNumb), description=linecache.getline("../txt_files/rules.txt", ruleNumb))
        await bot.say(embed=embed)
        print("{} used the r{} command in #{}".format(ctx.message.author, ruleNumb, ctx.message.channel))
        await bot.delete_message(ctx.message)
    else:
        await bot.say("{}, rule {} doesn't exist!".format(ctx.message.author, ruleNumb))
        print("{} tried to display rule {} in #{}".format(ctx.message.author, ruleNumb, ctx.message.channel))

@bot.command(pass_context=True)
async def naru(ctx): #Naru command
    RNG = random.randint(0, 2)
    if RNG == 0:
        await bot.say("Cus itsa  SMALL DICK BOY")
    if RNG == 1:
        await bot.say("The creepy thing?")
    if RNG == 2:
        await bot.say("'I need yvar to wake tf up for this'\nNo you don't. Leave me the fuck alone")
    print("{} used the naru command in #{}".format(ctx.message.author, ctx.message.channel))

@bot.command(pass_context=True)
async def gny(ctx): #Gny command
    RNG = random.randint(0, 2)
    if RNG == 0:
        await bot.say("Ya shaveing smooth and my crack hard to do")
    if RNG == 1:
        await bot.say("Ok hugs mmm u not still u know thinking ur bad right")
    if RNG == 2:
        await bot.say("Clenches butt cheeks so poop doesn't come out")
    print("{} used the gny command in #{}")

@bot.command(pass_context=True)
async def hug(ctx, member: discord.Member=None): #Hug command
    if member == None:
        member = ctx.message.author
    await bot.say("**hugs {}**".format(member.display_name))
    await bot.send_file(ctx.message.channel, "../imgs/hug.gif")
    print("{} hugged {} in #{}".format(ctx.message.author, member, ctx.message.channel))

@bot.command(pass_context=True)
async def mantis(ctx): #Mantis command
    RNG = random.randint(1, 19)
    await bot.say(linecache.getline("../txt_files/mantis.txt", RNG))
    print("{} used the mantis command in #{}".format(ctx.message.author, ctx.message.channel))

@bot.command(pass_context=True)
async def ban(ctx, member: discord.Member=None): #Ban command
    if ctx.message.author.server_permissions.ban_members:
        if member != ctx.message.author:
            await bot.ban(member)
            await bot.send_message(ctx.message.channel, "{} is now banned!".format(member))
            print("{} banned {} in #{}".format(ctx.message.author, member, ctx.message.channel))
        else:
            await bot.say("Please don't try to ban yourself, {}".format(ctx.message.author.display_name))
            print("{} tried to ban themselves in #{}".format(ctx.message.author, ctx.message.channel))
    else:
        await bot.say("You don't have permissions to use this command!")
        print("{} tried using the ban command without permissions in #{}".format(ctx.message.author, ctx.message.channel))

@bot.command(pass_context=True)
async def kick(ctx, member:discord.Member): #Kick command
    if ctx.message.author.server_permissions.ban_members:
        if member != ctx.message.author:
            await bot.kick(member)
            await bot.send_message(ctx.message.channel, "{} is now kicked!".format(member))
            print("{} kicked {} in #{}".format(ctx.message.author, member, ctx.message.channel))
        else:
            await bot.say("Please don't try to kick yourself, {}".format(ctx.message.author.display_name))
    else:
        await bot.say("You don't have permissions to use this command!")
        print("{} tried using the kick command without permissions in #{}".format(ctx.message.author, ctx.message.channel))

@bot.command(pass_context=True)
async def membercount(ctx): #Membercount command
    totalmembers = ctx.message.server.member_count-bots
    await bot.say("the {} now has {} members!".format(ctx.message.server, totalmembers))
    print("{} used the membercount command in #{}".format(ctx.message.author, ctx.message.channel))

@bot.command(pass_context=True)
async def poll(ctx): #Poll command
    await bot.add_reaction(ctx.message, "👍")
    await bot.add_reaction(ctx.message, "👎")
    print("{} used the poll command in #{}".format(ctx.message.author, ctx.message.channel))

@bot.command(pass_context=True)
async def quote(ctx, msg): #Quote command
    if ctx.message.author.server_permissions.manage_messages:
        await bot.say(msg)
        await bot.delete_message(ctx.message)
        print("{} made the bot say '{}' in #{}".format(ctx.message.author, msg, ctx.message.channel))
    else:
        await bot.say("You don't have permissions to use this command!")
        print("{} tried to let the bot say '{}' in #{} without permissions".format(ctx.message.author, msg, ctx.message.channel))

@bot.command(pass_context=True)
async def change_playing(ctx, game): #Change_playing command
    if ctx.message.author.server_permissions.administrator:
        await bot.change_presence(game=discord.Game(name=game))
        await bot.say("Changed playing message to '{}'".format(game))
        print("{} changed the playing message to '{}' in #{}".format(ctx.message.author, game, ctx.message.channel))
    else:
        await bot.say("You don't have permissions to use this command!")
        print("{} tried to change the playing message to '{}' in #{} without permissions!".format(ctx.message.author, game, ctx.message.channel))

@bot.command(pass_context=True)
async def nick(ctx, member: discord.Member, nick): #Nick command
    if ctx.message.author.server_permissions.manage_nicknames:
        await bot.change_nickname(member, nick)
        await bot.say("changed nickname to {}!".format(nick))
        print("{} changed {}'s nickname to {} in #{}".format(ctx.message.author, member, nick, ctx.message.channel))
    else:
        await bot.say("You don't have permissions to use this command!")
        print("{} tried changing {}'s nickname to {} in #{} without permissions!".format(ctx.message.author, member, nick, ctx.message.channel))

@bot.command(pass_context=True)
async def checkuser(ctx, member: discord.Member=None): #Checkuser command
    if member == None:
        member = ctx.message.author
    if ctx.message.author.server_permissions.manage_nicknames and member != ctx.message.author:
        await bot.say("Username: {}\nUser ID: {}\nProfile picture: {}\nUser is a bot: {}\nDisplay name: {}\nDiscord account created at: {}".format(member.name, member.id, member.avatar_url, member.bot, member.display_name, member.created_at))
        print("{} used the checkuser command on {} in #{}".format(ctx.message.author, member, ctx.message.channel))
    elif member == ctx.message.author:
        await bot.say("Username: {}\nUser ID: {}\nProfile picture: {}\nUser is a bot: {}\nDisplay name: {}\nDiscord account created at: {}".format(member.name, member.id, member.avatar_url, member.bot, member.display_name, member.created_at))
        print("{} used the checkuser command on themselves in #{}".format(ctx.message.author, ctx.message.channel))
    else:
        await bot.say("You don't have permissions to use this command!")
        print("{} tried checkuser on {} in #{} without permissions".format(ctx.message.author, member, ctx.message.channel))

@bot.command(pass_context=True)
async def clearnick(ctx, member: discord.Member=None): #Clearnick command
    if ctx.message.author.server_permissions.manage_nicknames:
        if member == None:
            member = ctx.message.author
        await bot.change_nickname(member, "")
        await bot.say("cleared {}'s nickname!".format(member))
        print("{} cleared {}'s nickname in #{}".format(ctx.message.author, member, ctx.message.channel))

@bot.command(pass_context=True)
async def takevent(ctx, member: discord.Member): #Takevent command
    if ctx.message.author.server_permissions.manage_channels:
        role = discord.utils.get(ctx.message.author.server.roles, name="no-vent")
        await bot.add_roles(member, role)
        await bot.say("{0.mention} cannot message in the vent channel anymore.".format(member))
        print("{} took vent acces from {} in #{}".format(ctx.message.author, member, ctx.message.channel))
    else:
        await bot.say("You don't have permissions to use this command!")
        print("{} tried to use the takevent command on {} in #{}".format(ctx.message.author, member, ctx.message.channel))

@bot.command(pass_context=True)
@commands.has_permissions(manage_channels=True)
async def givevent(ctx, member: discord.Member): #Givevent command
    if ctx.message.author.server_permissions.manage_channels:
        role = discord.utils.get(ctx.message.author.server.roles, name="no-vent")
        await bot.remove_roles(member, role)
        await bot.say("{0.mention} can now message in the vent channel again.".format(member))
        print("{} gave vent acces back to {} in #{}".format(ctx.message.author, member, ctx.message.channel))
    else:
        await bot.say("You don't have permissions to use this command!")
        print("{} tried to use the givevent command on {} in #{}".format(ctx.message.author, member, ctx.message.channel))

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
    print("{} used the join command in #{} to make the bot join {}".format(ctx.message.author, ctx.message.channel, channel))

@bot.command(pass_context=True)
async def leave(ctx): #Leave command
    server = ctx.message.server
    channel = ctx.message.author.voice.voice_channel
    voice_client = bot.voice_client_in(server)
    await voice_client.disconnect()
    await bot.say("left the {} channel".format(channel))
    print("{} used the leave command in #{} to make the bot leave {}".format(ctx.message.author, ctx.message.channel, channel))

@bot.command(pass_context=True)
async def play(ctx, url): #Play command
    server = ctx.message.server
    channel = ctx.message.author.voice.voice_channel
    voice_client = bot.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
    players[server.id] = player
    player.start()
    bot.say("Now playing a song in {}".format(channel))
    print("{} used the play command in #{} to play a song in {}".format(ctx.message.author, ctx.message.channel, channel))

@bot.command(pass_context=True)
async def pause(ctx): #Pause command
    id = ctx.message.server.id
    channel = ctx.message.author.voice.voice_channel
    players[id].pause()
    await bot.say("Paused the music playing in {}".format(channel))
    print("{} used the pause command in #{} to pause the music in {}".format(ctx.message.author, ctx.message.channel, channel))

@bot.command(pass_context=True)
async def resume(ctx): #Resume command
    id = ctx.message.server.id
    channel = ctx.message.author.voice.voice_channel
    players[id].resume()
    await bot.say("Resumed the music playing in {}".format(channel))
    print("{} used the resume command in #{} to resume the music in {}".format(ctx.message.author, ctx.message.channel, channel))

@bot.command(pass_context=True)
async def queue(ctx, url): #Queue command
    server = ctx.message.server
    channel = ctx.message.author.voice.voice_channel
    voice_client = bot.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
    if server.id in queues:
        queues[server.id].append(player)
    else:
        queues[server.id] = [player]
    await bot.say("Song queued.")
    print("{} used the queue command in #{} to queue a song to play in {}".format(ctx.message.author, ctx.message.channel, channel))

token_txt = open(r"../txt_files/bot_token.txt", "r")
token = token_txt.read()
bot.run(token)
token_txt.close
