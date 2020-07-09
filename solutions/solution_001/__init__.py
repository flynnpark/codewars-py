import re
import string


ALPHABET_PRESET = {v: k for k, v in enumerate(string.ascii_lowercase, start=1)}


def alphabet_position(text: str):
    return " ".join(
        [str(ALPHABET_PRESET[char.group()]) for char in re.finditer("[a-z]", text.lower())]
    )
