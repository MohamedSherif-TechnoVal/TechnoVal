# queue.py
# Implementation of a Queue (FIFO) in Python

class Queue:
    def __init__(self):
        self.items = []  # internal list to store queue elements

    def enqueue(self, item):
        """Add an item to the end of the queue"""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the front item of the queue"""
        if not self.is_empty():
            return self.items.pop(0)  # remove from front
        else:
            return "Queue is empty"

    def peek(self):
        """Return the front item without removing it"""
        if not self.is_empty():
            return self.items[0]
        else:
            return "Queue is empty"

    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue"""
        return len(self.items)


# Test the queue functionality
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Front item:", q.peek())      # 10
    print("Queue size:", q.size())      # 3
    print("Dequeued item:", q.dequeue())# 10
    print("Front item now:", q.peek())  # 20
    print("Queue is empty?", q.is_empty()) # False