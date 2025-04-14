import discord

from embeds.innovation import InnovationEmbed
from utils.valid_url import is_valid_url
from colorama import Fore, Style
from discord import ApplicationContext

from embeds.resourse import ResourceEmbed


class UserCog(discord.Cog):

    def __init__(self, bot):
        self.bot = bot


    @discord.command(name="innovation", description="Create embed-message for your resource /innovation <title> <description>")
    async def innovation(
            self,
            ctx: discord.ApplicationContext,
            title: discord.Option(str, min_length=2, max_length=30, required=True),
            description: discord.Option(str, min_length=5, max_length=300, required=False)
    ):
        if ctx.channel_id != 1359496319466471625 and ctx.channel_id != 1359571389488566433:
            raise Exception("Bad channel")

        embed = InnovationEmbed(
            author=ctx.author,
            title=title,
            description=description
        )
        await ctx.respond(embed=embed)


    @discord.command(name="resource", description="Create embed-message for your resource /resource <title> <link>")
    async def resource(
            self,
            ctx: discord.ApplicationContext,
            url: discord.Option(str, min_length=10, required=True),
            title: discord.Option(str, min_length=2, max_length=100, required=False)
    ):
        if ctx.channel_id != 1359242612745310461:
            raise Exception("Bad channel")

        if not is_valid_url(url):
            raise Exception("Address not valid (only https)")

        embed = ResourceEmbed(
            author=ctx.author,
            title=title,
            link=url
        )
        await ctx.respond(embed=embed)


    async def cog_command_error(self, ctx: ApplicationContext, error: Exception):
        print("Raised in cog level!")
        print(type(error))


    @discord.Cog.listener("on_ready")
    async def on_ready(self):
        print(f"{Fore.YELLOW + Style.BRIGHT}User{Fore.RESET + Style.RESET_ALL}\tCog status: \t{Fore.GREEN}[OK]{Fore.RESET}")


def setup(bot: discord.Bot):
    bot.add_cog(UserCog(bot))