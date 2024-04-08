from abc import ABC, abstractmethod

class Container(ABC):
    @abstractmethod
    def get_items(self):
        pass

    def validate_items(self, items):
        # Check if all items are of the same type
        if not all(isinstance(item, type(items[0])) for item in items):
            raise ValueError("Items must be of the same type")

        # Return the items if validation passes
        return items

class Stack(Container):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()

    def get_items(self):
        return self.validate_items(self.items)

class Queue(Container):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.items:
            return self.items.pop(0)

    def get_items(self):
        return self.validate_items(self.items)

# Usage
stack = Stack()
stack.push("A")
stack.push("B")
print(stack.get_items())  # Outputs: ['A', 'B']

queue = Queue()
queue.enqueue("X")
queue.enqueue("Y")
print(queue.get_items())  # Outputs: ['X', 'Y']

# This will raise a ValueError
try:
    stack.push(1)
except ValueError as e:
    print(e)
