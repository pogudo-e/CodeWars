def capitals(word, count: int = 0):
    res = []
    for i in word:
        if i.isupper():
            res.append(count)
        count += 1
    return res


print(capitals('CodEWaRs'))
