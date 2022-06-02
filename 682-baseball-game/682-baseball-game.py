class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        
        for val in ops:
            
            if val == 'C':
                stack.pop()
                
            elif val == 'D':
                stack.append(stack[-1]*2)
                    
            elif val == '+':
                stack.append(stack[-1]+stack[-2])
            
            else:
                stack.append(int(val))           
        result = 0
        for i in range(len(stack)):                      
            result += stack[i]
        return result
    #return sum(stack)