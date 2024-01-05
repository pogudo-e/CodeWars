def fake_bin(x):
    return ''.join(map(str, [0 if int(x[i]) < 5 else 1 for i in range(len(x))]))


print(fake_bin('17482'))
