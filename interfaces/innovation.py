import discord
from discord import InputTextStyle, Interaction
from discord.ui import Modal, InputText, View, button

from embeds.innovation import InnovationEmbed


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


class InnovationView(View):

    def __init__(self, ctx: discord.ApplicationContext):
        super().__init__(timeout=5)
        self.ctx = ctx


    @button(label="СОЗДАТЬ", emoji="❇️", style=discord.ButtonStyle.green, row=0)
    async def cardCallback(self, button, interaction: Interaction):
        await interaction.response.send_modal(modal=InnovationModal(self.ctx, title="Форма отправки предложения"))
