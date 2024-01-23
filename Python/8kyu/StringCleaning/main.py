import re


def string_clean(s):
    """
    Function will return the cleaned string
    """
    return re.sub('[0-9]', '', s)


print(string_clean("Dsa32 cdsc34232 csa!!! 1I 4Am cool!"), "Dsa cdsc csa!!! I Am cool!")
