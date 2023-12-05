import re


def disemvowel(string_: str):
    return re.sub(r'([eiaouEIAOU])', '', string_)


print(disemvowel("This website is for losers LOL!"))
