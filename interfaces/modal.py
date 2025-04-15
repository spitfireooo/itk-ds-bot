import discord
from discord import InputTextStyle, Interaction
from discord.ui import Modal, InputText

from embeds.innovation import InnovationEmbed
from embeds.resourse import ResourceEmbed
from utils.valid_url import is_valid_url


class InnovationModal(Modal):

    def __init__(self, ctx: discord.ApplicationContext, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx = ctx

        self.add_item(InputText(
            style=InputTextStyle.short,
            label="Название, тема",
            placeholder="Введите название или тему",
            min_length=5,
            max_length=30,
            required=True
        ))

        self.add_item(InputText(
            style=InputTextStyle.long,
            label="Описание",
            placeholder="Объясните, как ваша идея может улучшить сервер",
            min_length=10,
            max_length=300,
            required=False
        ))

    async def callback(self, interaction: Interaction):
        title, description = map(lambda x: x.value, self.children)
        embed = InnovationEmbed(
            author=self.ctx.author,
            title=title,
            description=description,
            file=None
        )
        await interaction.respond(embed=embed)


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
