def mango(quantity, price):
    i = 0
    res = 0
    while quantity>0:
        i += 1
        if i > 2:
            res -= price
            i = 0
        res += price
        quantity -= 1
    return res
