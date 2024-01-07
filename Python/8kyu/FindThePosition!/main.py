def position(alphabet):
    return ''.join([f'Position of alphabet: {key + 1}' for key, value in enumerate(list(map(chr, range(97, 123)))) if
                    value == alphabet])


print(position('a'))
print(position('c'))
