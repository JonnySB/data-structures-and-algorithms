"""
Given an integer array nums and an integer k, return the k most frequent 
elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), 
where n is the array's size.
"""


# time-complexity = O(nlogn) - sorting dictionary takes nlogn
def topKFrequent(nums: list[int], k: int) -> list[int]:
    num_map = {}
    for num in nums:
        num_map[num] = num_map.get(num, 0) + 1
    sorted_dict = dict(sorted(num_map.items(), key=lambda x: x[1], reverse=True))
    return sorted_dict[k:]


# bucket sort
# time / space-complexity = O(n) / O(n)
def topKFrequentBucketSort(nums: list[int], k: int) -> list[int]:
    num_map = {}
    frequency_array = [[] for _ in range(len(nums) + 1)]

    for num in nums:
        num_map[num] = num_map.get(num, 0) + 1
    for num, frequency in num_map.items():
        frequency_array[frequency].append(num)

    res = []
    for i in range(len(frequency_array) - 1, 0, -1):
        for n in frequency_array[i]:
            res.append(n)
            if len(res) == k:
                return res
    return []


print(topKFrequentBucketSort([1, 1, 1, 1, 3, 3, 9, 7, 5, 5, 5], 2))
