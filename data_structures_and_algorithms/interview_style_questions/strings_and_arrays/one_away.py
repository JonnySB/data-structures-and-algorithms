'''
One away:
There are three types of edits that can be performed on strings: insert a character, remove a character, or relpace a character. Given two strings write a function to check if they are one edit (or zero edits) away.
Example:
    pale, ple -> True
    pales, pale -> True
    pale, bale -> True
    pale, bake -> False
'''

def one_away(string, string_2):
    letter_hash = dict()
    for letter in string:
        if letter_hash.get(letter) is None:
            letter_hash[letter] = 1
        else:
            letter_hash[letter] += 1
    for letter in string_2:
        if letter_hash.get(letter) is None:
            letter_hash[letter] = -1
        else:
            letter_hash[letter] -= 1
            if letter_hash[letter] == 0:
                del letter_hash[letter]
    if len(letter_hash) <= 2 and abs(sum(letter_hash.values())) <= 2:
        return True
    return False

def one_edit_away(string_1, string_2): # book solution
    if len(string_1) == len(string_2):
        return one_edit_replace(string_1, string_2)
    if len(string_1) + 1 == len(string_2):
        return one_edit_insert(string_1, string_2)
    if len(string_1) - 1 == len(string_2):
        return one_edit_insert(string_2, string_1)
    return False

def one_edit_replace(string_1, string_2):
    found_difference = False
    for i in range(len(string_1)):
        if string_1[i] != string_2[i]:
            if found_difference:
                return False
            found_difference = True
    return True

def one_edit_insert(string_1, string_2):
    index1 = 0
    index2 = 0
    while index1 < len(string_1) and index2 < len(string_2):
        if string_1[index1] != string_2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1 
    return True

print(one_edit_away('pale', 'ple'))
print(one_edit_away('pales', 'pale'))
print(one_edit_away('pale', 'bale'))
print(one_edit_away('pale', 'bake'))
