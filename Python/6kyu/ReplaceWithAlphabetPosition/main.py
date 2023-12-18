import string


def alphabet_position(text: str) -> str:
    # alphb = list(string.ascii_lowercase)
    # res = []
    # for i in text.lower():
    #     if i in alphb:
    #         res.append(alphb.index(i)+1)
    # return res
    return ' '.join(
        map(str, [string.ascii_lowercase.index(i) + 1 for i in text.lower() if i in string.ascii_lowercase]))


print(alphabet_position("The sunset sets at twelve o' clock."))
