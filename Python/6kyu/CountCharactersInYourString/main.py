def count(s: str) -> dict:
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


print(count('aba'))
