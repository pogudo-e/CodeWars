def is_sorted_and_how(arr):
    return 'yes, ascending' if sorted(arr) == arr else 'yes, descending' if sorted(arr, reverse=True) == arr else 'no'


print(is_sorted_and_how([1, 2]), 'yes, ascending')
