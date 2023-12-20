def twoSum(nums, target):
    n = len(nums)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# Testing code

print(twoSum([3, 3], 6))
print(twoSum([1, 3, 9, 3, 10, 2, 7], 19))
