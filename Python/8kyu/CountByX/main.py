def count_by(x, n):
    return [x * i + x for i in range(n)]


print(count_by(3, 5) == [3, 6, 9, 12, 15])
