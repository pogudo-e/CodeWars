def pillars(num_pill, dist, width):
    x = (dist * 100) * (num_pill - 1) + (width * (num_pill - 2))
    return x if x > 0 else 0


print(pillars(11, 15, 30), 15270)
print(pillars(2, 20, 25), 2000)
print(pillars(1, 10, 10), 0)
