"""
You are given an integer array height of length n. There are n vertical lines 
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the 
container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104
"""


# brute force with two pointers O(n*n)
def maxAreaSlow(height: list[int]) -> int:
    max_area = 0
    for i in range(len(height)):
        j = len(height) - 1
        while i < j:
            length = j - i
            max_shared_height = min(height[i], height[j])
            area = length * max_shared_height
            if area > max_area:
                max_area = area
            j -= 1

    return max_area


# two pointer in O(n)
def maxArea(height: list[int]) -> int:
    max_area = 0
    i = 0
    j = len(height) - 1
    while i < j:
        max_shared_height = min(height[i], height[j])
        length = j - i
        area = max_shared_height * length
        if area > max_area:
            max_area = area
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))
