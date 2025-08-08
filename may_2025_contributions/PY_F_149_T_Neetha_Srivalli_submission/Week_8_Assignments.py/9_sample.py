class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return "Queue is empty"
        return self.stack2.pop()

# Example usage
q = QueueUsingStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())

#Output: 
# 1