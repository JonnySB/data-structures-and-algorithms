"""
Given an array of integers heights representing the histogram's bar height 
where the width of each bar is 1, return the area of the largest rectangle in 
the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4

Constraints:
    1 <= heights.length <= 105
    0 <= heights[i] <= 104
"""


def largestRectangleArea(heights: list[int]) -> int:
    if len(heights) == 1:
        return heights[0]
    l = 0
    r = len(heights) - 1
    stack = []  # monotonic increasing stack
    while l <= r:
        l_value = heights[l]
        r_value = heights[r]
        curr_sum = min(l_value, r_value) * ((r - l) + 1)

        # check if curr_sum lower than previous stack values
        while stack and curr_sum <= stack[-1]:
            stack.pop()
        stack.append(curr_sum)

        if l_value <= r_value:
            l += 1
        else:
            r -= 1

    return stack[-1]


heights = [2, 1, 5, 6, 2, 3]
print(largestRectangleArea(heights))
