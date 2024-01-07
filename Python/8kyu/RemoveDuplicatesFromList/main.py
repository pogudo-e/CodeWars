def distinct(seq):
    n = []
    for i in seq:
        if i not in n:
            n.append(i)
    return n


print(distinct([1, 1, 1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])