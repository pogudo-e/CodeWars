def square_digits(num: int):
    return int(''.join([str(int(x) ** 2) for x in str(num)]))


print(square_digits(9119))  # 811181
