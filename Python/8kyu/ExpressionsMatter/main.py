def expression_matter(a, b, c):
    return max((a * (b + c)), (a * b * c), (a + b * c), ((a + b) * c), (a + b + c))


print(expression_matter(2, 1, 2), 6)
