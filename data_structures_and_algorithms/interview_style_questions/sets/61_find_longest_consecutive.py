"""
Set: Longest Consecutive Sequence ( ** Interview Question)
Given an unsorted array of integers, write a function that finds the length of the  longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater than the previous element).

Use sets to optimize the runtime of your solution.

Input: An unsorted array of integers, nums.

Output: An integer representing the length of the longest consecutive sequence in nums.
"""

def longest_consecutive_sequence(arr):
    my_set = set(arr)
    longest_sequence = 0
    for num in arr:
        if (num - 1) not in my_set:
            current_sequence = 1
            while (num + current_sequence) in my_set:
                current_sequence += 1
            if current_sequence > longest_sequence:
                longest_sequence = current_sequence
    return longest_sequence
                

( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )

"""
    EXPECTED OUTPUT:
        ----------------
    4

"""
