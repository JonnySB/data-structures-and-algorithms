"""
Given an array of integers nums which is sorted in ascending order, and an 
integer target, write a function to search target in nums. If target exists, 
then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:
    1 <= nums.length <= 104
    -104 < nums[i], target < 104
    All the integers in nums are unique.
    nums is sorted in ascending order.
"""


def search(nums: list[int], target: int) -> int:
    l = 0
    r = len(nums) + 1

    while l <= r:
        m = l + ((r - l) // 2)
        v = nums[m]
        if v == target:
            return m
        elif target < v:
            r = m - 1
        else:
            l = m + 1
    return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(search(nums, target))

nums = [-1, 0, 3, 5, 9, 12]
target = 2
print(search(nums, target))


#    l = 0
#    r = len(nums) - 1
#    while l <= r:
#        # calculated like this as opposed to ((r + l) // 2) to avoid int
#        # overflow. I.e. adding two int that are close to their max value.
#        m = l + ((r - l) // 2)
#        if nums[m] > target:
#            r = m - 1
#        elif nums[m] < target:
#            l = m + 1
#        else:
#            return m
#    return -1
