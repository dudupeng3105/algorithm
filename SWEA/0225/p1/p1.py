class CircularQueue:
    def __init__(self, qsize):
        self.qsize = qsize
        self.front = 0
        self.rear = 0
        self.items = [None] * qsize

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % self.qsize

    def clear(self):
        self.front = self.rear

    def __len__(self):
        return (self.rear-self.front + self.qsize) % self.qsize

    def enQueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.qsize
            self.items[self.rear] = item

    def deQueue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.qsize
            return self.items[self.front]

    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1) % self.qsize]


cq = CircularQueue(10)
cq.enQueue(1)
cq.enQueue(2)
cq.enQueue(3)
print(cq.deQueue())
print(cq.deQueue())
print(cq.deQueue())