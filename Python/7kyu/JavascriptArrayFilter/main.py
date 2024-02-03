def filter_odd_num(in_num):
    if (in_num % 2) == 0:
        return True
    else:
        return False


def get_even_numbers(arr):
    return list(filter(filter_odd_num, arr))


print(get_even_numbers([1, 2, 3, 4, 5]), [2, 4], "Returned list is incorrect")

# def get_even_numbers(arr):
# return list(filter(lambda x: x % 2 == 0, arr))
