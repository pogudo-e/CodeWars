import math


def is_square(n):
    return math.sqrt(n).is_integer() if n >= 0 else False


print(is_square(0), True)
