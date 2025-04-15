import discord

from discord.ext import commands
from embeds.innovation import InnovationEmbed, InnovationInfoEmbed
from interfaces.innovation import InnovationView
from interfaces.innovation import InnovationModal
from discord import ApplicationContext, Attachment

from utils.cog_status_printer import status_printer
from utils.add_reaction import add_reaction_on_message


class InnovationCog(discord.Cog):

    def __init__(self, bot):
        self.bot = bot


    @discord.command(name="innovation-info", description="Open instruction of create innovation /innovation-info")
    @commands.is_owner()
    async def innovation_info(self, ctx: discord.ApplicationContext):
        if ctx.channel_id != 1359496319466471625 and ctx.channel_id != 1359571389488566433:
            raise Exception("Bad channel")
        await ctx.respond(embed=InnovationInfoEmbed(), view=InnovationView(ctx))


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
        message = await ctx.respond(embed=embed)
        await add_reaction_on_message(message, "👍", "👎")


    @discord.command(name="innovation-modal", description="Create embed-message for your innovation /innovation")
    async def innovation_modal(self, ctx: discord.ApplicationContext):
        if ctx.channel_id != 1359496319466471625 and ctx.channel_id != 1359571389488566433:
            raise Exception("Bad channel")

        modal = InnovationModal(ctx, title="Форма отправки предложения")
        await ctx.send_modal(modal=modal)


    async def cog_command_error(self, ctx: ApplicationContext, error: Exception):
        print("Raised in cog level!")
        print(type(error))


    @discord.Cog.listener("on_ready")
    async def on_ready(self):
        status_printer("Innov")


def setup(bot: discord.Bot):
    bot.add_cog(InnovationCog(bot))