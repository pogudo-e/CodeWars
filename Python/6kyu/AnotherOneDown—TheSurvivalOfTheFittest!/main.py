def remove_smallest(n: int, arr: list) -> list:
    n_arr = arr.copy()
    if n <= 0:
        return arr
    elif len(arr) < n:
        return []
    for i in range(n):
        n_arr.remove(min(n_arr))
    return n_arr


print(remove_smallest(-10, [1, 2, 3, 4, 5]))
print(remove_smallest(3, [5, 3, 2, 1, 4]))
# 5 , 4
print(remove_smallest(2, [5, 3, 2, 1, 4]))
# 5 ,3,4
print(remove_smallest(2, [5, 2, 3, 2, 1, 4]))
