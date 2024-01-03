"""
A phrase is a palindrome if, after converting all uppercase letters into 
lowercase letters and removing all non-alphanumeric characters, it reads the 
same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters.
"""


def isPalindromeFirst(s: str) -> bool:
    clean_str = ""
    for char in s:
        if char.isalnum():
            clean_str += char.lower()
    for i in range(len(clean_str) // 2):
        if clean_str[i] != clean_str[-(i + 1)]:
            return False
    return True


def isPalindrome(s: str) -> bool:
    i = 0
    j = len(s) - 1
    while i < j:
        while not isAlphaNumeric(s[i]) and i < j:
            i += 1
        while not isAlphaNumeric(s[j]) and j > i:
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


def isAlphaNumeric(c: str) -> bool:
    return (
        ord("A") <= ord(c) <= ord("Z")
        or ord("a") <= ord(c) <= ord("z")
        or ord("0") <= ord(c) <= ord("9")
    )


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))

s = "race a car"
print(isPalindrome(s))
