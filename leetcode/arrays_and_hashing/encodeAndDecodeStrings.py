"""
Design an algorithm to encode a list of strings to a string. The encoded string 
is then sent over the network and is decoded back to the original list of 
strings.

Please implement encode and decode

Example1
Input: ["lint","code","love","you"]
Output: ["lint","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"

Example2
Input: ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
Explanation:
One possible encode method is: "we:;say:;:::;yes"
"""


def encode(strs: list[str]) -> str:
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res


def decode(s: str) -> list[str]:
    res = []
    i = 0
    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        start = j + 1
        end = start + length
        res.append(s[start:end])
        i = end
    return res


encoded_string = encode(["lint", "code", "love", "you"])
print(encoded_string)

decoded_string = decode(encoded_string)
print(decoded_string)
