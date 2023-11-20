def flick_switch(lst: str):
    res = []
    b = True
    for l in lst:
        if l == 'flick':
            if b:
                b = False
            else:
                b = True
        res.append(b)
    return res
