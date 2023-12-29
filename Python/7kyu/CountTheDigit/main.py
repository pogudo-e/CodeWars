def nb_dig(n, d):
    count = 0
    for i in range(n + 1):
        count += str(i**2).count(str(d))
    return count


print(nb_dig(10, 1))
print(nb_dig(5750, 0))
print(nb_dig(25, 1))
