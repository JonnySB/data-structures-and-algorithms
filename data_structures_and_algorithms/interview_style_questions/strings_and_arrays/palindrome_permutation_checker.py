'''
Palindrome Permutation:
Given a string, write a function to check if it's a permutation of a palindrome. A palindrome is the same forwards as it is backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. You can ignore casing and non-letter characters.
E.g. input 'Tact coa'
Output: True 'taco cat', 'atco cta' etc.
'''

def palindrome_permutation(string):
    string = format_string(string)
    if len(string) < 4:
        return False
    letter_hash = dict()
    for letter in string:
        if letter_hash.get(letter) is None:
            letter_hash[letter] = 1
        else:
            del letter_hash[letter]
    if len(letter_hash) <= 1:
        return True
    return False

def format_string(string):
    new_string = ''
    for char in string.lower():
        if char in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
            new_string += char
    return new_string


print(palindrome_permutation('Tact coa'))
print(palindrome_permutation('Abba'))
print(palindrome_permutation('Aba'))
print(palindrome_permutation('fig  gif'))
print(palindrome_permutation('fantaf'))
