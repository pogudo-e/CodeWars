def two_sum(numbers: list, target):
    for i in numbers:
        jj = 0
        for j in numbers:
            if i + j == target and numbers.index(i) != jj:
                return (numbers.index(i), jj)
            jj += 1
    return


print(two_sum((2, 2, 3), 4))
