def binary_array_to_number(arr: list) -> int:
    return int(''.join(map(str, arr)), 2)


print(binary_array_to_number([0, 0, 0, 1]))
print(binary_array_to_number([1, 1, 1, 1]), 15)
