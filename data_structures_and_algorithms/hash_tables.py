class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            # ord gets the ASCii number of each letter
            # modulo of length gives address of 0-6
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


my_hash_table = HashTable()
my_hash_table.print_table()
my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("washers", 50)
my_hash_table.print_table()

print(my_hash_table.get_item("bolts"))
print(my_hash_table.get_item("washers"))
print(my_hash_table.get_item("lumber"))

print(my_hash_table.keys())


# Using the above structure, compare two lists to see if they have any common elements::

arr1 = [2,7,4]
arr2 = [9,5,2]
arr3 = [10,6,3]

def commonValues(arr1, arr2):
    hash_table = HashTable()
    for num in arr1:
        hash_table.set_item(str(num), True)
    for num in arr2:
        if hash_table.get_item(str(num)) is not None:
            return True
    return False 

print(commonValues(arr1, arr2))
print(commonValues(arr1, arr3))