class QueueUsingStacks:    #Class to implement a queue using two stacks
    def __init__(self):       #Constructor to initialize two stacks
        self.stack1 = []
        self.stack2 = []
   
    def enqueue(self, x):      #Funtion to add an element to the queue
        self.stack1.append(x)

    def dequeue(self):        #Function to remove an element from the queue
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