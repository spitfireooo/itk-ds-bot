from discord import Embed


class ExceptionEmbed(Embed):

    def __init__(self, error, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = "📛 Exception"
        self.color = 0xff0000
        self.add_field(name="Type", value="type")
        self.add_field(name="Description", value="desc")
