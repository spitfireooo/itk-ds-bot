import discord

from embeds.innovation import InnovationEmbed
from interfaces.button import InnovationModal
from colorama import Fore, Style
from discord import ApplicationContext, Attachment



class InnovationCog(discord.Cog):

    def __init__(self, bot):
        self.bot = bot


    @discord.command(name="innovation", description="Create embed-message for your innovation /innovation <title> <description>")
    async def innovation(
            self,
            ctx: discord.ApplicationContext,
            title: discord.Option(str, min_length=2, max_length=30, required=True),
            description: discord.Option(str, min_length=5, max_length=300, required=False),
            file: discord.Option(Attachment, required=False)
    ):
        if ctx.channel_id != 1359496319466471625 and ctx.channel_id != 1359571389488566433:
            raise Exception("Bad channel")

        embed = InnovationEmbed(
            author=ctx.author,
            title=title,
            description=description,
            file=file if file else None
        )
        await ctx.respond(embed=embed)

    @discord.command(name="innovation-modal", description="Create embed-message for your innovation /innovation")
    async def innovation_modal(self, ctx: discord.ApplicationContext,):
        if ctx.channel_id != 1359496319466471625 and ctx.channel_id != 1359571389488566433:
            raise Exception("Bad channel")

        modal = InnovationModal(ctx, title="Форма отправки предложения")
        await ctx.send_modal(modal=modal)


    async def cog_command_error(self, ctx: ApplicationContext, error: Exception):
        print("Raised in cog level!")
        print(type(error))


    @discord.Cog.listener("on_ready")
    async def on_ready(self):
        print(f"{Fore.YELLOW + Style.BRIGHT}Innov{Fore.RESET + Style.RESET_ALL}\tCog status: \t{Fore.GREEN}[OK]{Fore.RESET}")


def setup(bot: discord.Bot):
    bot.add_cog(InnovationCog(bot))