def find_smallest(numbers: list, to_return: str) -> int:
    return min(numbers) if to_return == "value" else numbers.index(min(numbers))


print(find_smallest([5,4,3,2,1], 'index'))


print(find_smallest([ 8, 0, 9], 'value'))
