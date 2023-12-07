def remainder(a, b):
    return max([a, b]) % min(a, b) if a and b else None if max([a, b]) != 0 or a == b else 0


print(remainder(17, 5))
print(remainder(0, 5))
print(remainder(17, 0))
print(remainder(-1, 0))
print(remainder(0, 0))
