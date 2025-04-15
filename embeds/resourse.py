from discord import Embed


class BasisResourceEmbed(Embed):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = "🔭 Innovation"
        self.color = 0x346DF0


class ResourceEmbed(BasisResourceEmbed):

    def __init__(self, author, title, link, file, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_field(name=f"{title if title else 'Link'}", value=f'```{link}```')

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


class ResourceInfoEmbed(BasisResourceEmbed):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_field(name="", value="❓ Инструкция:\n— для публикации своего ресурса (ссылки), можно воспользоваться 3-мя способами", inline=False)
        self.add_field(name="> 1. Кнопка", value=f"Нажать на кнопку [СОЗДАТЬ] закрепленную к данному сообщению ниже", inline=False)
        self.add_field(name="> 2. Модальное окно", value=f"Ввести команду в чат ```/resource-modal``` вызванную форму, необходимо будет заполнить", inline=False)
        self.add_field(name="> 3. Inline-команда", value=f"Ввести команду в чат ```/resource <url> <title> <file>``` при вводе команды, будут всплывать подсказки, описание и файл являются не обязательными аргументами", inline=False)
