"""
You are given an array of integers nums, there is a sliding window of size k 
which is moving from the very left of the array to the very right. You can 
only see the k numbers in the window. Each time the sliding window moves right 
by one position.

Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    1 <= k <= nums.length
"""


# O(k(n-k)) i.e. slow
def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    res = []

    l = 0
    for r in range(k - 1, len(nums)):
        res.append(getMax(nums[l : r + 1]))
        l += 1
    return res


def getMax(nums):
    max = -float("infinity")
    for num in nums:
        if num > max:
            max = num
    return max


# O(n)


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(maxSlidingWindow(nums, k))
