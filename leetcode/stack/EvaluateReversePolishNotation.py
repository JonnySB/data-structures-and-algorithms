"""
console.log(evaluate the expression. Return an integer that represents the 
value of the expression).

Note that:

    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish 
    notation.
    The answer and all the intermediate calculations can be represented in a 
    32-bit integer.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

Constraints:
    1 <= tokens.length <= 104
    tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in 
    the range [-200, 200].
"""


def calcOpperation(opp, a, b):
    if opp == "+":
        return int(a) + int(b)
    if opp == "-":
        return int(a) - int(b)
    if opp == "*":
        return int(a) * int(b)
    if opp == "/":
        return int(int(a) / int(b))


def evalRPNOld(tokens: list[str]) -> int:
    opps = ("-", "+", "*", "/")
    stack = []
    for token in tokens:
        if token in opps:
            b = stack.pop()
            a = stack.pop()
            res = calcOpperation(token, a, b)
            stack.append(res)
        else:
            stack.append(token)
    return stack[0]


def evalRPN(tokens: list[str]) -> int:
    stack = []
    for c in tokens:
        if c == "+":
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif c == "*":
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        else:
            stack.append(int(c))
    return stack[0]


tokens = ["2", "1", "+", "3", "*"]
print(evalRPN(tokens))

tokens = ["4", "13", "5", "/", "+"]
print(evalRPN(tokens))

tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(evalRPN(tokens))
