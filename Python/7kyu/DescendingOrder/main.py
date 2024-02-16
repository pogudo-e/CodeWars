def descending_order(num: int):
    b = []
    while num > 0:
        b.append(num % 10)
        num = num // 10
    number = 0
    b = sorted(b, reverse=True)
    for digit in b:
        number = number * 10 + digit
    return number


print(descending_order(123456))
print(descending_order(23542354234))
