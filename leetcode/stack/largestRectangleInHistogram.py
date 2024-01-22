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
    stack = []  # pair: [index, height]
    maxArea = 0

    for i in range(len(heights)):
        h = heights[i]
        start = i
        while stack and stack[-1][1] > h:
            popped_i, popped_h = stack.pop()
            maxArea = max(maxArea, (i - popped_i) * popped_h)
            start = popped_i
        stack.append([start, h])

    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))
    return maxArea


heights = [2, 1, 5, 6, 2, 3]
print(largestRectangleArea(heights))


heights = [2, 4]
print(largestRectangleArea(heights))
