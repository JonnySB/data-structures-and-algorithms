class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current_index = len(self.heap) - 1
        
        while current_index > 0 and self.heap[current_index] < self.heap[self._parent(current_index)]:
            self._swap(current_index, self._parent(current_index))
            current_index = self._parent(current_index)
    
    def _sink_down(self, index):
        min_index = index
        while True:
            left_index = self._right_child(index)
            right_index = self._left_child(index)

            if left_index < len(self.heap) and self.heap[min_index] > self.heap[left_index]:
                min_index = left_index

            if right_index < len(self.heap) and self.heap[min_index] > self.heap[right_index]:
                min_index = right_index

            if index != min_index:
                self._swap(index, min_index)
                index = min_index
            else:
                return

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return min_value      
 
myheap = MinHeap()
myheap.insert(12)
myheap.insert(10)
myheap.insert(8)
myheap.insert(6)
myheap.insert(4)
myheap.insert(8)

print(myheap.heap)  # [6, 8, 10, 12]

myheap.remove()

Rrint(myheap.heap)  # [4, 6, 10, 12, 8]

"""
    EXPECTED OUTPUT:
    ----------------
    [6, 8, 10, 12]
    [4, 6, 10, 12, 8]
    [2, 6, 4, 12, 8, 10]

"""
