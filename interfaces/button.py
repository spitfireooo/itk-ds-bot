import discord

from discord import Interaction
from discord.ui import View, button

from interfaces.modal import InnovationModal


class InnovationView(View):

    def __init__(self, ctx: discord.ApplicationContext):
        super().__init__(timeout=5)
        self.ctx = ctx


    @button(label="СОЗДАТЬ", emoji="❇️", style=discord.ButtonStyle.green, row=0)
    async def cardCallback(self, button, interaction: Interaction):
        await interaction.response.send_modal(modal=InnovationModal(self.ctx, title="Форма отправки предложения"))
