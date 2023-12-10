def sum_two_smallest_numbers(numbers: list) -> int:
    return sum(sorted(numbers)[:2])


# from heapq import nsmallest


# def sum_two_smallest_numbers(numbers):
#     return sum(nsmallest(2, numbers))


print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))
print(sum_two_smallest_numbers([25, 42, 12, 18, 22]))
