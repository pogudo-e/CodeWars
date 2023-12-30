def high(x):
    d, x = {}, x.split(' ')
    for i in x:
        s = 0
        for j in i:
            s += ord(j) - 96
        d[i] = s
    return max(d, key=d.get)


# print(ord('a')-96)
print(high('man i need a taxi up to ubud'), 'taxi')
