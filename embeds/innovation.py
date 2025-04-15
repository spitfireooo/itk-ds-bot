from discord import Embed


class InnovationEmbed(Embed):

    def __init__(self, author, title, description, file, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = "🔭 Innovation"
        self.color = 0x346DF0
        self.add_field(name=title, value=f"` — {description if description else title}`")

        if file:
            if file.content_type and file.content_type.startswith("image"):
                self.set_image(url=file.url)
            self.add_field(name="", value=f"[Ссылка на файл]({file.url})", inline=False)

        if author.avatar:
            self.set_author(
                name=author.display_name,
                icon_url=author.avatar.url
            )
        else:
            self.set_author(name=author.display_name)
