def find_uniq(arr):
    n = set(arr)
    return list(n)[list(map(arr.count, n)).index(1)]


print(find_uniq([0, 0, 0.55, 0, 0]), 0.55)
