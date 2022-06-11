class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [0]*k
        self.cursize = 0
        self.head = 0
        
    def enQueue(self, value: int) -> bool:
        if self.cursize < self.k:
            self.queue[(self.head+self.cursize) % self.k] = value
            self.cursize += 1
            return True
        else:
            return False
        

    def deQueue(self) -> bool:
        
        if self.cursize > 0:
            self.head = (self.head+1)% self.k
            self.cursize -= 1
            return True
        else:
            return False
        

    def Front(self) -> int:
        if self.cursize > 0:
            return self.queue[self.head]
        else:
            return -1
        

    def Rear(self) -> int:
        if self.cursize == 0:
            return -1
        return self.queue[(self.head+self.cursize-1) % self.k]
        
    def isEmpty(self) -> bool:
        if self.cursize == 0:
            return True
        else:
            return False
            
    def isFull(self) -> bool:
        if self.cursize == self.k:
            return True
        else:
            return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()