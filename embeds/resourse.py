from discord import Embed


class ResourceEmbed(Embed):

    def __init__(self, author, title, link, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = "📦 Resource"
        self.color = 0xFFB810
        self.add_field(name=f"{title if title else 'Link'}", value=f'```{link}```')
        if author.avatar:
            self.set_author(
                name=author.display_name,
                icon_url=author.avatar.url
            )
        else:
            self.set_author(name=author.display_name)
