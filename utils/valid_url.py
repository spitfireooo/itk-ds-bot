import re

def is_valid_url(url: str) -> bool:
    regex = re.compile(
        r"^https://(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}(?:/[^\s]*)?$",
        re.IGNORECASE,
    )

    return bool(regex.match(url))