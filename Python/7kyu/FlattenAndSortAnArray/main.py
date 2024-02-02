def flatten_and_sort(array):
    return sorted([v for i in array for v in i])


print(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
