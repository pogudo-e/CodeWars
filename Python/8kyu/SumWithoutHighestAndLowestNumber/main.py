def sum_array(arr):
    if arr and len(arr) > 2:
        arr.remove(max(arr))
        arr.remove(min(arr))
        return sum(arr)
    return 0


print(sum_array([6, 2, 1, 8, 10]))
# 16
