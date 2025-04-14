from discord import Embed


class InnovationEmbed(Embed):

    def __init__(self, author, title, description, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = "🔭 Innovation"
        self.color = 0x346DF0
        self.add_field(name=title, value=f"`— {description if description else title}`")
        if author.avatar:
            self.set_author(
                name=author.display_name,
                icon_url=author.avatar.url
            )
        else:
            self.set_author(name=author.display_name)
