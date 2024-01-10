"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and 
']', determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Constraints
    1 ≤ s.length ≤ 104
    s consists of parentheses only '()[]{}'.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5i:
Input: s = "{[]}"
Output: true
"""


class Stack:
    def __init__(self):
        self.stack = []
        self.length = 0

    def peek(self):
        if self.length > 0:
            return self.stack[self.length - 1]
        return None

    def push(self, value):
        self.stack.append(value)
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        else:
            self.length -= 1
            return self.stack.pop()


def validParenthesesClass(s: str) -> bool:
    stack = Stack()
    for i in range(len(s)):
        if f"{stack.peek()}{s[i]}" == "[]":
            stack.pop()
        elif f"{stack.peek()}{s[i]}" == "()":
            stack.pop()
        elif f"{stack.peek()}{s[i]}" == "{}":
            stack.pop()
        else:
            stack.push(s[i])

    return True if stack.length == 0 else False


def validParentheses(s: str) -> bool:
    par_map = {"]": "[", ")": "(", "}": "{"}
    stack = []
    for c in s:
        # add opening para
        if c not in par_map:
            stack.append(c)
            continue
        # for closing paras, if stack empty or top item not matching
        if not stack or stack[-1] != par_map[c]:
            return False
        stack.pop()
    # if empty return true
    return not stack


s = "()"
print(validParentheses(s))

s = "()[]{}"
print(validParentheses(s))

s = "(]"
print(validParentheses(s))

s = "([)]"
print(validParentheses(s))

s = "{[]}"
print(validParentheses(s))
