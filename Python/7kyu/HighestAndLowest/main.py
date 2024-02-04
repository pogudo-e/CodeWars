def high_and_low(numbers):
    num = list(int(i) for i in numbers.split(' '))
    return f'{max(num)} {min(num)}'


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"), "42 -9")
