# class CustomStack:
    

#     def __init__(self, maxSize: int):
#         self.stack = []
#         self.mSize = maxSize

#     def push(self, x: int) -> None:
#         if len(self.stack) < self.mSize:
#             self.stack.append(x)
            
#     def pop(self) -> int:
#         if self.stack:
#             return self.stack.pop()
#         else:
#             return -1
        
#     def increment(self, k: int, val: int) -> None:
#         for i in range(min(len(self.stack),k)):
#             self.stack[i] += val

class CustomStack:
    
    def __init__(self,maxSize:int):
        self.mSize = maxSize
        self.stack = [[0,0]]*self.mSize
        self.curSize = 0
        
    def push(self,x:int)->None:
        if self.curSize < self.mSize:
            self.stack[self.curSize] = [x,0]
            self.curSize += 1
         
    def pop(self)->int:
        if self.curSize <= 0:
            return -1
        
        val,inc = self.stack[self.curSize-1]
        self.curSize -= 1
        
        if self.curSize > 0:
            self.stack[self.curSize-1][1] += inc 
            
        return (val + inc) 
        
    def increment(self,k:int,val:int)->None:
        self.stack[min(self.curSize-1,k-1)][1] += val
            
# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)