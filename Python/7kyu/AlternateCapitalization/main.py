import string


def capitalize(s):
    gena = ''.join([val.upper() if key % 2 == 0 else val for key, val in enumerate(s.lower())])
    return [gena, gena.swapcase()]


print(capitalize("abcdef"), ['AbCdEf', 'aBcDeF'])
