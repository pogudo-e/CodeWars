def solution(nums):
    return sorted(nums) if nums else []


print(solution([1, 2, 3, 10, 5]), [1, 2, 3, 5, 10])
print(solution([]), [])
