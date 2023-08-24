class ArrayList:
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

    def print_array(self):
        if self.size == 0:
            return None
        print(self.data[0:self.size])

resizeable_array = ArrayList()
resizeable_array.append(0)
resizeable_array.append(1)
resizeable_array.append(2)
resizeable_array.append(3)
resizeable_array.append(4)
resizeable_array.append(5)
resizeable_array.append(6)
resizeable_array.append(7)
resizeable_array.append(8)
resizeable_array.append(9)
resizeable_array.append(10)
resizeable_array.append(11)
resizeable_array.append(12)
resizeable_array.append(13)

resizeable_array.print_array()
