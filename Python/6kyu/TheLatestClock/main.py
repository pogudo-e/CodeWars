import time
import itertools
from datetime import datetime


def late_clock(a, b, c, d):
    ll = [a, b, c, d]
    res = list(itertools.permutations(ll))
    result = []
    for i in res:
        try:
            result.append(time.mktime(time.strptime(f"{i[0]}{i[1]}:{i[2]}{i[3]}", "%H:%M")))
        except ValueError:
            continue
    return datetime.fromtimestamp(max(result)).strftime("%H:%M")


print(late_clock(1, 9, 8, 3))  # 19:38
print(late_clock(9, 1, 2, 5))  # 21:59
print(late_clock(1, 2, 8, 9))  # 19: 28
