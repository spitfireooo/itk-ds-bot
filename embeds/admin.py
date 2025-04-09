from discord import Embed


class AdminEmbed(Embed):

    def __init__(self, author, title, description, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = title
        self.description = f"`/{description}`"
        self.color = 0x00ff00
        if author.avatar:
            self.set_author(
                name=author.display_name,
                icon_url=author.avatar.url
            )
        else:
            self.set_author(name=author.display_name)
