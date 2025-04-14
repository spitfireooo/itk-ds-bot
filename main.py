import discord
import os
from dotenv import load_dotenv
from colorama import Fore, Style
from embeds.exception import ExceptionEmbed

load_dotenv()

intents = discord.Intents.default()
# intents.message_content = True
# intents.members = True

bot = discord.Bot(intents=intents, debug_guilds=[1358958606468513864])

os.system('cls')
print(f'{Fore.YELLOW+Style.BRIGHT}Bot{Fore.RESET+Style.RESET_ALL} started status: \t{Fore.YELLOW}[STARTING]{Fore.RESET}\n')


@bot.slash_command(name="test", descirption="Test command")
async def test(ctx: discord.ApplicationContext):
    await ctx.respond("Hello")


@bot.event
async def on_ready():
    # os.system('cls')
    print(f'{Fore.YELLOW + Style.BRIGHT}Bot{Fore.RESET + Style.RESET_ALL} started status: \t{Fore.GREEN}[OK]{Fore.RESET}\n')


@bot.event
async def on_application_command_error(ctx: discord.ApplicationContext, error):
    embed = ExceptionEmbed(error)
    await ctx.respond(embed=embed, delete_after=15, ephemeral=True)


# load extension/cogs
for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")


if __name__ == "__main__":
    try:
        bot.run(os.getenv('BOT_TOKEN'))
    except:
        print(f'{Fore.YELLOW + Style.BRIGHT}Bot{Fore.RESET + Style.RESET_ALL} started status: {Fore.RED}[ERROR]{Fore.RESET}\n')
    finally:
        print(f'\n{Fore.YELLOW + Style.BRIGHT}Bot{Fore.RESET + Style.RESET_ALL} closed...')
