import re


def replace_exclamation(st):
    return re.sub(r'([aeiouAEIOU])', '!', st)


# aeiouAEIOU
print(replace_exclamation("ABCDE"), "!BCD!")
