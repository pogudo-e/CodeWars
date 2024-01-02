def wave(people: str):
    res = []
    p = list(people)
    for i in range(len(p)):
        if p[i] != ' ':
            p[i] = p[i].upper()
            res.append(''.join(p))
            p = list(people)

    return res


print(wave('hello'))
