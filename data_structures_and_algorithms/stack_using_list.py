"""
Class creating stack from list
"""


class Stack:
    """Create stack from list"""

    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        lst = []
        for i in range(len(self.stack_list)-1, -1, -1):
            lst.append(self.stack_list[i])
        print(lst)

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

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]


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


# CODING CHALLENGE 42:*
""" 
Stack: Sort Stack ( ** Interview Question)
The sort_stack function takes a single argument, a Stack object.  The function should sort the elements in the stack in ascending order (the lowest value will be at the top of the stack) using only one additional stack. 

The function should use the pop, push, peek, and is_empty methods of the Stack object.

The function should perform the following tasks:
- Create a new instance of the Stack class called sorted_stack.
- While the input stack is not empty, perform the following:
    - Pop the top element from the input stack and store it in a variable temp.
    - While the sorted_stack is not empty and its top element is greater than temp, pop the top element from sorted_stack and push it back onto the input stack.
    - Push the temp variable onto the sorted_stack.
- Once the input stack is empty, transfer the elements back from sorted_stack to the input stack. To do this, while sorted_stack is not empty, pop the top element from sorted_stack and push it onto the input stack.

You can also click on "Hints" (above) to see the pseudo-code.

Overall, the function should have a time complexity of O(n^2), where n is the number of elements in the original stack, due to the nested loops used to compare the elements.  However, the function should only use one additional stack, which could be useful in situations where memory is limited.   
"""


def sort_stack(stack):
    additional_stack = Stack()

    while not stack.is_empty():
        temp = stack.pop()

        while not additional_stack.is_empty() and additional_stack.peek() > temp:
            stack.push(additional_stack.pop())

        additional_stack.push(temp)

    while not additional_stack.is_empty():
        stack.push(additional_stack.pop())


# TEST
my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

# print("Stack before sort_stack():")
# my_stack.print_stack()

# sort_stack(my_stack)

# print("\nStack after sort_stack:")
# my_stack.print_stack()
