import discord

from colorama import Fore, Style
from discord import ApplicationContext


class UserCog(discord.Cog):

    def __init__(self, bot):
        self.bot = bot


    async def cog_command_error(self, ctx: ApplicationContext, error: Exception):
        print("Raised in cog level!")
        print(type(error))


    @discord.Cog.listener("on_ready")
    async def on_ready(self):
        print(f"{Fore.YELLOW + Style.BRIGHT}User{Fore.RESET + Style.RESET_ALL}\tCog status: \t{Fore.GREEN}[OK]{Fore.RESET}")


def setup(bot: discord.Bot):
    bot.add_cog(UserCog(bot))