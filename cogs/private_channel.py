import discord
from discord.ext import commands


class CreateChannel(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel is None and after.channel is not None:
            if after.channel.id == 1359495573174091836:
                for guild in self.bot.guilds:
                    channel_cat = discord.utils.get(guild.categories, id=1359494887405387857)
                    channel = await guild.create_voice_channel(name = f'Channel {member.display_name}', category=channel_cat)
                    await channel.set_permissions(
                        member,
                        connect=True,
                        mute_members=True,
                        move_members=True,
                        manage_channels=True
                    )
                    await member.move_to(channel)
                    def check(x, y, z):
                        return len(channel.members) == 0
                    await self.bot.wait_for('voice_state_update', check=check)
                    await channel.delete()


def setup(bot):
    bot.add_cog(CreateChannel(bot))
