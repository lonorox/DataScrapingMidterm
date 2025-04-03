import re
import html


def cleaner(text):
    if not text:
        return ""
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"<.*?>", "", text)  #
    return text


def parser(_string):
    match = re.search(r'\d+\.\d+|\d+', _string)
    if match:
        num_str = match.group()
        num = float(num_str) if '.' in num_str else int(num_str)
        return num
    return match
