""" Set: Remove Duplicates ( ** Interview Question)
You have been given a list my_list with some duplicate values. Your task is to write a Python program that removes all the duplicates from the list using a set and then prints the updated list.

You need to implement a function remove_duplicates(my_list) that takes in the input list my_list as a parameter and returns a new list with no duplicates.

Your function should not modify the original list, instead, it should create a new list with unique values and return it. """


'authenticate/register_user.html',


def remove_duplicates(my_list):
    return list(set(my_list))


my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
new_list = remove_duplicates(my_list)
print(new_list)


"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    (Order may be different as sets are unordered)

"""
