import discord

from colorama import Fore, Style
from discord import ApplicationContext, Attachment

from embeds.resourse import ResourceEmbed
from interfaces.modal import ResourceModal
from utils.valid_url import is_valid_url


class ResourceCog(discord.Cog):

    def __init__(self, bot):
        self.bot = bot


    @discord.command(name="resource", description="Create embed-message for your resource /resource <title> <link>")
    async def resource(
            self,
            ctx: discord.ApplicationContext,
            url: discord.Option(str, min_length=10, required=True),
            title: discord.Option(str, min_length=2, max_length=100, required=False),
            file: discord.Option(Attachment, required=False)
    ):
        if ctx.channel_id != 1359242612745310461 and ctx.channel_id != 1359571389488566433:
            raise Exception("Bad channel")

        if not is_valid_url(url):
            raise Exception("Address not valid (only https)")

        embed = ResourceEmbed(
            author=ctx.author,
            title=title,
            link=url,
            file=file if file else None
        )
        await ctx.respond(embed=embed)


    @discord.command(name="resource-modal", description="Create embed-message for your resource /resource-modal")
    async def resource_modal(self, ctx: discord.ApplicationContext):
        if ctx.channel_id != 1359496319466471625 and ctx.channel_id != 1359571389488566433:
            raise Exception("Bad channel")

        modal = ResourceModal(ctx, title="Форма отправки внешнего ресурса/ссылки")
        await ctx.send_modal(modal=modal)


    async def cog_command_error(self, ctx: ApplicationContext, error: Exception):
        print("Raised in cog level!")
        print(type(error))


    @discord.Cog.listener("on_ready")
    async def on_ready(self):
        print(f"{Fore.YELLOW + Style.BRIGHT}Source{Fore.RESET + Style.RESET_ALL}\tCog status: \t{Fore.GREEN}[OK]{Fore.RESET}")


def setup(bot: discord.Bot):
    bot.add_cog(ResourceCog(bot))