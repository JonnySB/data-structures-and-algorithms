''' Create a method checking if one string is a palindrome of the other '''

class String:
    def __init__(self, string):
        self.string = string

    def is_palindrome(self, other_string):
        dic = dict()
        for letter in self.string:
            if dic.get(letter) is not None:
                dic[letter] += 1
            else:
                dic[letter] = 1
        for letter in other_string:
            if dic.get(letter) is None:
                return False
            dic[letter] -= 1
            if dic[letter] == 0:
                del dic[letter]
        if len(dic) == 0:
            return True
        return False


my_string = String('abcde')
print(my_string.is_palindrome('edcba'))
print(my_string.is_palindrome('dcba'))
print(my_string.is_palindrome('eddcba'))

