"""
Class creating stack from list
"""


class Stack:
    """Create stack from list"""

    def __init__(self):
        self.stack_list = []

    def size(self):
        return len(self.stack_list)
    
    def is_empty(self):
        return len(self.stack_list) == 0

    def push(self, value):
        """Appends item to end of list"""
        self.stack_list.append(value)

    def pop(self):
        """Removes item from the end of the list"""
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()
        
def is_balanced_parentheses(test_string: str) -> bool:
    """takes in string list and returns whether balanced"""
    stack = Stack()
    for item in test_string:
        if item == "(":
            stack.push(item)
        elif item == ')':
            if stack.is_empty() or stack.pop() != '(':
                return False
    return stack.size() == 0

def reverse_string(target_string: str) -> str:
    """Takes a string and uses a stack to reverse it"""
    stack = Stack()
    reversed_string = str()

    for letter in target_string:
        stack.push(letter)

    while not stack.is_empty():
            reversed_string += stack.pop()

    return reversed_string


print(reverse_string('abcde'))

