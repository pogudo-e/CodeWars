def array_diff(a, b):
    if a:
        return [i for i in a if i not in a or i not in b]
    return a


print(array_diff([1, 2, 2], [2]))
print(array_diff([1, 2], [1]))
