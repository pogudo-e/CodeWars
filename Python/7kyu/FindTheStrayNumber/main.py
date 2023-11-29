from collections import Counter


def stray(arr: list) -> int:
    return {v: k for (k, v) in Counter(arr).items() if v == 1}[1]


print(stray([1, 1, 1, 1, 1, 1, 2]))
print(stray([2, 3, 2, 2, 2]))

# def stray(arr):
#     for x in arr:
#         if arr.count(x) == 1:
#             return x
