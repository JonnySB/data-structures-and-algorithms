def longest_repeating(s: str, k: int) -> int:
    count = {}
    max_length = 0

    l = 0
    maxf = 0
    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        maxf = max(maxf, count[s[r]])

        while (r - l + 1) - maxf > k and l <= r:
            count[s[l]] -= 1
            l += 1

        max_length = max(max_length, (r - l + 1))

    return max_length


s = "ABAB"
k = 2
print(longest_repeating(s, k))

s = "AABABBA"
k = 1
print(longest_repeating(s, k))
