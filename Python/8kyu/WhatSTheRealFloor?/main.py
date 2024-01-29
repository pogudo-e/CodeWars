def get_real_floor(n):
    if 0 < n < 13:
        return n - 1
    if n > 13:
        return n - 2
    return n


print(get_real_floor(5), 4)
