import discord

from colorama import Fore, Style
from discord import ApplicationContext

from utils.cog_status_printer import status_printer


class UserCog(discord.Cog):

    def __init__(self, bot):
        self.bot = bot


    async def cog_command_error(self, ctx: ApplicationContext, error: Exception):
        print("Raised in cog level!")
        print(type(error))


    @discord.Cog.listener("on_ready")
    async def on_ready(self):
        status_printer("User")


def setup(bot: discord.Bot):
    bot.add_cog(UserCog(bot))