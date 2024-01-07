def sort_by_length(arr):
    return sorted(arr, key=len)


print(sort_by_length(["i", "to", "beg", "life"]), ["beg", "life", "i", "to"])
