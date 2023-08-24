'''
In some programming languages, creating a new string from a list of words would need to create a new string every time a word is added, hence leading to a time complexity of O(n squared). How could you do this with a time complexity of O(1)
'''

class StringBuilder:
    ''' resizable array class to hold string as array before converting as string '''
    def __init__(self, initial_size=10):
        self.data = [None] * initial_size
        self.capacity = initial_size
        self.size = 0

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def append(self, value):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.data[self.size] = value
        self.size += 1


def join_string(words):
    string_builder = StringBuilder() 
    for word in words:
        string_builder.append(word)
    return ' '.join([word for word in string_builder.data if word is not None])


string = 'This is a list of words that is longer than the minimum of 10 words long'
words = string.split(' ')

print(join_string(words))
