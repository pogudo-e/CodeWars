def beeramid(bonus, price):
    if bonus < 0:
        return 0
    beer_price = bonus / price
    n = 0
    i = 0
    while beer_price >= n:
        n += i * i
        i += 1
    return i - 2


print(beeramid(9, 2))  # 1 -- 4,5
print(beeramid(21, 1.5))  # 3 -- 14
