import webbrowser
import discord
from discord import InputTextStyle, Interaction
from discord.ui import Modal, InputText, View, button

from embeds.resourse import ResourceEmbed
from utils.valid_url import is_valid_url


class ResourceModal(Modal):

    def __init__(self, ctx: discord.ApplicationContext, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx = ctx

        self.add_item(InputText(
            style=InputTextStyle.short,
            label="Название, заголовок",
            placeholder="Введите название или заголовок",
            min_length=5,
            max_length=30,
            required=True
        ))

        self.add_item(InputText(
            style=InputTextStyle.long,
            label="Ссылка",
            placeholder="https://your-address.com",
            required=False
        ))


    async def callback(self, interaction: Interaction):
        title, url = map(lambda x: x.value, self.children)

        if not is_valid_url(url):
            raise Exception("Address not valid (only https)")

        embed = ResourceEmbed(
            author=self.ctx.author,
            title=title,
            link=url,
            file=None
        )
        await interaction.respond(embed=embed)


class ResourceOpenInBrowserView(View):

    def __init__(self, ctx: discord.ApplicationContext, url):
        super().__init__(timeout=5)
        self.ctx = ctx
        self.url = url


    @button(label="ОТКРЫТЬ В БРАУЗЕРЕ", emoji="🧭", style=discord.ButtonStyle.blurple, row=0)
    async def cardCallback(self, button, interaction: Interaction):
        webbrowser.open_new_tab(self.url)
        await interaction.response.send_message("Cash")


class ResourceCreateView(View):

    def __init__(self, ctx: discord.ApplicationContext):
        super().__init__(timeout=5)
        self.ctx = ctx


    @button(label="СОЗДАТЬ", emoji="❇️", style=discord.ButtonStyle.blurple, row=0)
    async def cardCallback(self, button, interaction: Interaction):
        await interaction.response.send_modal(modal=ResourceModal(self.ctx, title="Форма отправки предложения"))