"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, 
or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
    1 <= s1.length, s2.length <= 104
    s1 and s2 consist of lowercase English letters.
"""


def checkInclusionOld(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    l = 0
    r = len(s1) - 1
    while r < len(s2):
        hash_map = [0] * 26
        sub_string = s2[l : r + 1]

        for i in range(len(s1)):
            hash_map[ord(s1[i]) - ord("a")] += 1
            hash_map[ord(sub_string[i]) - ord("a")] -= 1

        if all([count == 0 for count in hash_map]):
            return True

        l += 1
        r += 1

    return False


def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    # initialise maps and add one for the intial window length
    s1Count = [0] * 26
    s2Count = [0] * 26
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord("a")] += 1
        s2Count[ord(s2[i]) - ord("a")] += 1

    # calculate initial number of matches. I.e.
    matches = 0
    for i in range(26):
        matches += 1 if s1Count[i] == s2Count[i] else 0

    l = 0
    # loop starts with r looking at next available letter
    for r in range(len(s1), len(s2)):
        # matches equals 26 if both sub arrays are the same
        if matches == 26:
            return True

        # increase window size and add 1 to array index of letter
        index = ord(s2[r]) - ord("a")
        s2Count[index] += 1
        # inc/ dec matches depending if in s1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1

        # decrease window size and remove 1 from array index of letter
        index = ord(s2[l]) - ord("a")
        s2Count[index] -= 1
        # inc/ dec matches depending if in s1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1
        l += 1

    # return needs own check due to not running the loop again
    return matches == 26


s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))
