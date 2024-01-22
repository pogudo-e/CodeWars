def round_to_next5(n):
    return n if n % 5 == 0 else 5*(n//5+1)


print(round_to_next5(5), 5)
print(round_to_next5(7), 10)
print(round_to_next5(3), 5)
print(round_to_next5(20), 20)
print(round_to_next5(39), 40)
print(round_to_next5(-2), 0)
print(round_to_next5(-5), -5)

