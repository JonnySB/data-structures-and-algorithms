def check_unique(mystring: str) -> bool:
    mydict = dict()
    for letter in mystring:
        if mydict.get(letter) is not None:
            return False
        mydict[letter] = letter
    return True


print(check_unique('unique'))
print(check_unique('abcdefghijk'))
