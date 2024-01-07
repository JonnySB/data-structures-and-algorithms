def minWindowOld(s: str, t: str) -> str:
    if len(t) > len(s):
        return ""

    count_t = {}
    window = {}
    for c in t:
        count_t[c] = count_t.get(c, 0) + 1

    have = 0
    need = len(count_t)

    res_coords = [-1, -1]
    res_len = float("infinity")
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)

        if c in count_t and window[c] == count_t[c]:
            have += 1

        while have == need:
            if (r - l + 1) < res_len:
                res_coords = [l, r]
                res_len = r - l + 1

            window[s[l]] -= 1
            if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                have -= 1
            l += 1
    l, r = res_coords
    return s[l : r + 1] if res_len != float("infinity") else ""


"""
Given two strings s and t of lengths m and n respectively, return the minimum 
window substring of s such that every character in t (including duplicates) is 
included in the window. If there is no such substring, return the empty string 
"".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' 
from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
    m == s.length
    n == t.length
    1 <= m, n <= 105
    s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""


def minWindowOld(s: str, t: str) -> str:
    if len(t) > len(s):
        return ""

    count_t = {}
    window = {}
    for c in t:
        count_t[c] = count_t.get(c, 0) + 1

    have = 0
    need = len(count_t)

    res_coords = [-1, -1]
    res_len = float("infinity")
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)

        if c in count_t and window[c] == count_t[c]:
            have += 1

        while have == need:
            if (r - l + 1) < res_len:
                res_coords = [l, r]
                res_len = r - l + 1

            window[s[l]] -= 1
            if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                have -= 1
            l += 1
    l, r = res_coords
    return s[l : r + 1] if res_len != float("infinity") else ""


def minWindow(s: str, t: str) -> str:
    if len(t) > len(s):
        return ""

    count_t = {}
    window = {}
    for c in t:
        count_t[c] = count_t.get(c, 0) + 1

    have = 0
    need = len(count_t)
    res_length = float("infinity")
    res_coords = [-1, -1]

    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = window.get(c, 0) + 1

        if c in count_t and count_t[c] == window[c]:
            have += 1

        while have == need:
            window_length = r - l + 1
            if window_length < res_length:
                res_coords = [l, r]
                res_length = window_length

            c = s[l]
            window[c] -= 1

            if c in count_t and window[c] < count_t[c]:
                have -= 1

            l += 1

    l, r = res_coords
    return s[l : r + 1] if res_length != float("infinity") else ""


s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))
