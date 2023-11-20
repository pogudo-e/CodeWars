def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return 'INVALID'
    if n == m or n > m:
        return 0
    if m % n == 0.0:
        count = m // n - 1
    else:
        count = m // n
    res = 0
    ret = 0
    for i in range(count):
        res += n
        ret += res
    return ret


# def sum_mul(n, m):
#     if m>0 and n>0:
#         return sum(range(n, m, n))
#     else:
#         return 'INVALID'

print(sum_mul(3, 13))
print(sum_mul(2, 9))
print(sum_mul(2, 10))
