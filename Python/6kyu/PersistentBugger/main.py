import math


def persistence(n: int, count: int = 0) -> int:
    while True:
        num = list(map(int, str(n)))
        if len(num) > 1:
            n = math.prod(num)
            count += 1
        else:
            return count


print(persistence(39))
print(persistence(4))
print(persistence(25))
