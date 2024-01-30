import math


def find_next_square(sq):
    if int(math.sqrt(sq) * 100) % 100 == 0: return int(math.sqrt(sq) + 1) ** 2
    return -1


print(find_next_square(121), 144, "Wrong output for 121")
print(find_next_square(532), -1, "Wrong output for 121")
