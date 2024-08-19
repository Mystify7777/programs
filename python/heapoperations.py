class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return max_val

    def heapify_down(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        largest = i

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.heapify_down(largest)

    def search(self, value):
        return value in self.heap

# Example usage:
heap = MaxHeap()
heap.insert(5)
heap.insert(7)
heap.insert(3)
heap.insert(9)
heap.insert(2)

print("Heap after insertion:", heap.heap)

print("Extracted max element:", heap.extract_max())
print("Heap after extraction:", heap.heap)

print("Search for 7:", heap.search(7))
print("Search for 10:", heap.search(10))
