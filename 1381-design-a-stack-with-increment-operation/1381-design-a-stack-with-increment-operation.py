class CustomStack:
    

    def __init__(self, maxSize: int):
        self.stack = []
        self.mSize = maxSize
        self.curSize = 0
        

    def push(self, x: int) -> None:
        if len(self.stack) < self.mSize:
            self.stack.append(x)
            

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return -1
        

    def increment(self, k: int, val: int) -> None:
        
        
    
        for i in range(min(len(self.stack),k)):
            self.stack[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)