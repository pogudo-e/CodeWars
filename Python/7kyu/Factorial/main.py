def factorial(n):
    if n < 0 or n > 12:
        raise ValueError
    return n * factorial(n - 1) if n > 1 else 1


print(factorial(3), 6, "factorial for 3 is 6")
print(factorial(1), 6, "factorial for 3 is 6")
print(factorial(0), 6, "factorial for 3 is 6")
print(factorial(2), 6, "factorial for 3 is 6")
# print(factorial(14), 6, "factorial for 3 is 6")
print(factorial(-6), 6, "factorial for 3 is 6")
