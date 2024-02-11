def no_odds(values):
    result = []
    for i in values:
        if i % 2 == 0:
            result.append(i)
    return result


print(no_odds([0, 2, 4, 6, 8, 10]), [0, 2, 4, 6, 8, 10], 'Evens through ten')
print(no_odds([-1, -3, -5, -7, -9]), [], 'Negative odds')
