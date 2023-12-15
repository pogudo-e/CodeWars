def invert(lst):
    return [abs(i) if i < 0 else -i for i in lst]


print(invert([1, 2, 3, 4, 5]))
