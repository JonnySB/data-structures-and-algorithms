'''
URLify
Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the 'true' length of the string.
'''

def URLify(string):
    string_arr = []
    space_counter = 0
    length = 0
    for letter in string:
        string_arr.append(letter)
        length += 1
        if letter == ' ':
            space_counter += 1
    string_arr.extend([None]*(2*space_counter))
    for i in range(length-1,0,-1):
        if space_counter == 0:
            return ''.join(string_arr)
        if string_arr[i] == ' ':
            string_arr[i + (2 * space_counter) - 2] = '%'
            string_arr[i + (2 * space_counter) - 1] = '2'
            string_arr[i + (2 * space_counter)] = '0'
            space_counter -= 1
        else:
            string_arr[i + (2 * space_counter)] = string_arr[i]


print(URLify('Mr John Smith'))
print(URLify('This is a test sentence to see if it works on something a bit longer'))
