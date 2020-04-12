# Stack
class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def push(self, item):
        self.stack.append(item)

    def peek(self):
        return self.stack[-1]

    def sizeStack(self):
        return len(self.stack)

# Queue
class Queue:

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        return self.queue[0]

    def sizeQueue(self):
        return len(self.queue)
