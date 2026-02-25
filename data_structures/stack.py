# stack.py
# Implementation of a Stack (LIFO) in Python

class Stack:
    def __init__(self):
        self.items = []  # Internal list to store stack elements

    def push(self, item):
        """Add an item to the top of the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item of the stack"""
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        """Return the top item without removing it"""
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the stack"""
        return len(self.items)


# Test the stack functionality
if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)

    print("Top item:", s.peek())     # 30
    print("Stack size:", s.size())   # 3
    print("Popped item:", s.pop())   # 30
    print("Top item now:", s.peek()) # 20
    print("Stack is empty?", s.is_empty()) # False