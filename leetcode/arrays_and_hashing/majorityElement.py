"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You 
may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109
 
Follow-up: Could you solve the problem in linear time and in O(1) space?
"""


def majorityElement(nums: list[int]) -> int:
    maj_target = len(nums) / 2

    frequency_map = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

        if frequency_map[num] > maj_target:
            return num

    return 0


nums = [3, 2, 3]
print(majorityElement(nums))

nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))
