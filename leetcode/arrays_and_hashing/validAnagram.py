"""
Given two strings s and t, return true if t is an anagram of s, and false 
otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt 
your solution to such a case?
"""


# using hash table
def isAnagram(s: str, t: str) -> bool:
    letters = {}
    for letter in s:
        letters[letter] = letters.get(letter, 0) + 1

    for letter in t:
        if letters.get(letter) is None:
            return False

        if letters.get(letter) == 1:
            del letters[letter]
            continue

        letters[letter] -= 1

    return not bool(letters)


# using char map
def isAnagramMap(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    char_map = [0] * 26

    for i in range(len(s)):
        char_map[ord(s[i]) - ord("a")] += 1
        char_map[ord(t[i]) - ord("a")] -= 1

    return all(count == 0 for count in char_map)
