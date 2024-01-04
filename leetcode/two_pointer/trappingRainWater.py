"""
Given n non-negative integers representing an elevation map where the width of 
each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array 
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) 
are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
 
Constraints:
    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105

"""


# for each index (excluding 0 and len - 1, as no L / R)
# find the max to the left and max to the right, the min of these minus the height
# of the element is the amount of water that can be stored in that 'column'
# time-complexity = O(4n) -> O(n)
# space-complexity = O(3n) -> O(n)
def trapIneff(height: list[int]) -> int:
    res = 0
    max_left = []
    max_right = []
    min_left_right = []

    # build max_left
    max = 0
    for i in range(len(height)):
        max_left.append(max)
        if height[i] > max:
            max = height[i]

    # build max_left (list reversed)
    max = 0
    for i in range(len(height) - 1, -1, -1):
        max_right.append(max)
        if height[i] > max:
            max = height[i]

    # build min list
    for i in range(len(height)):
        min_left_right.append(min(max_left[i], max_right[-(i + 1)]))

    # difference:
    for i in range(len(height)):
        difference = min_left_right[i] - height[i]
        if difference > 0:
            res += difference
    return res


# INTUITION:
# two pointer starting from either end.
# keep track of left_max and right_max
# concentrating on the smaller side of left_max vs right_max at a time,
# add left_max - current column height to res.
# note, this will always be positive due to incrementing l/ r first
def trap(height: list[int]) -> int:
    if not height:
        return 0

    l = 0
    r = len(height) - 1

    left_max = height[l]
    right_max = height[r]
    res = 0

    while l < r:
        if left_max < right_max:
            l += 1
            left_max = max(left_max, height[l])
            res += left_max - height[l]
        else:
            r -= 1
            right_max = max(right_max, height[r])
            res += right_max - height[r]
    return res


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))
