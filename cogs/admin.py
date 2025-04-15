import asyncio

import discord
from discord import ApplicationContext
from discord.ext import commands
from datetime import timedelta

from embeds.admin import AdminEmbed
from utils.cog_status_printer import status_printer


class AdminCog(discord.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.is_allowed_to_file = False


    @discord.command(name="clear", description="Chat clearing /clear <channel> <amount>")
    @commands.is_owner()
    async def clear(
        self,
        ctx: discord.ApplicationContext,
        channel: discord.Option(
            discord.TextChannel,
            name="channel",
            name_localizations={"ru": "канал"},
            description='Select channel for clearing messages',
            description_localizations={"ru": "Выберите канал для отчистки сообщений"},
            required=False
        ),
        amount: discord.Option(
            int,
            min_value=1,
            max_value=100,
            default=10,
            name="amount",
            name_localizations={"ru": "количество"},
            description="Enter amount messages, for her deleting",
            description_localizations={"ru": "Введите количество сообщений, которые будут удалены"}
        )
    ):
        channel = channel if channel is not None else ctx.channel
        await channel.purge(limit=amount)

        embed = AdminEmbed(
            author=ctx.author,
            title=f"Clearing {amount} messages",
            description=f"clear {channel} {amount}"
        )
        await ctx.respond(delete_after=5, embed=embed, ephemeral=True)


    @discord.command(name="kick", description="Kick user /kick <user>")
    @commands.is_owner()
    async def kick(
        self,
        ctx: discord.ApplicationContext,
        member: discord.Option(discord.Member, required=True),
        reason: discord.Option(str, min_length=3, max_length=100, required=False)
    ):
        await member.kick(reason=reason)
        embed = AdminEmbed(
            author=ctx.author,
            title=f"Kick {member} user",
            description=f"Kicked {member}"
        )
        await ctx.respond(delete_after=5, embed=embed)


    @discord.command(name="mute", description="Mute user /mute <user> <time> <type> <reason>")
    @commands.is_owner()
    async def mute(
        self,
        ctx: discord.ApplicationContext,
        member: discord.Option(discord.Member, required=True),
        time: discord.Option(int, min_value=1, max_value=1000000, default=1),
        cat: discord.Option(
            str,
            choices=["minute", "hour", "day"],
            default="minute"
        ),
        reason: discord.Option(str, min_length=3, max_length=100, required=False)
    ):
        minutes = time if cat == "minute" else time * 60 if cat == "hour" else time * 60 * 24
        duration = timedelta(minutes=int(minutes))
        await member.timeout_for(duration, reason=reason)
        await ctx.respond(f"User muted: {member.name} on {time} {cat[0]}.", delete_after=5)


    @discord.command(name="unmute", description="Unmute user /unmute <user>")
    @commands.is_owner()
    async def unmute(
        self,
        ctx: discord.ApplicationContext,
        member: discord.Option(discord.Member, required=True),
        reason: discord.Option(str, min_length=3, max_length=100, required=False)
    ):
        await member.remove_timeout(reason=reason)
        await ctx.respond(f"User un muted: {member.name}", delete_after=5)


    @discord.command(name="ban", description="Ban user /ban <user> <time> <type> <reason>")
    @commands.is_owner()
    async def ban(
        self,
        ctx: discord.ApplicationContext,
        member: discord.Option(discord.Member, required=True),
        time: discord.Option(int, min_value=1, max_value=1000000, default=1),
        cat: discord.Option(
            str,
            choices=["minute", "hour", "day", "infinity"],
            default="infinity"
        ),
        reason: discord.Option(str, min_length=3, max_length=100, required=False)
    ):
        await ctx.guild.ban(member, reason=reason)
        if cat != "infinity":
            duration = time if cat == "minute" else time * 60 if cat == "hour" else time * 60 * 24
            await asyncio.sleep(duration)
            await ctx.guild.unban(member)
            await ctx.respond(f"User banned: {member.name} on {time} {cat[0]}.", delete_after=5)
        await ctx.respond(f"User banned: {member.name} on infinity.", delete_after=5)


    @discord.command(name="unban", description="Unban user /unban <user> <reason>")
    @commands.is_owner()
    async def unban(
            self,
            ctx: discord.ApplicationContext,
            member: discord.Option(discord.Member, required=True),
            reason: discord.Option(str, min_length=3, max_length=100, required=False)
    ):
        await ctx.guild.unban(member.id, reason=reason)
        await ctx.respond(f"User unbanned: {member.name}.", delete_after=5)


    @clear.error
    async def on_clear_error(self, ctx: discord.ApplicationContext, error):
        if isinstance(error, commands.errors.NotOwner):
            await ctx.respond("Bad permissions")
        else:
            raise error
        print("The exception was raised", type(error))


    async def cog_command_error(self, ctx: ApplicationContext, error: Exception):
        print("Raised in cog level!")
        print(type(error))


    @discord.Cog.listener("on_ready")
    async def on_ready(self):
        status_printer("Admin")


def setup(bot: discord.Bot):
    bot.add_cog(AdminCog(bot))
