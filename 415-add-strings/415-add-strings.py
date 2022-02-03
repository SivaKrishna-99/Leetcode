class Solution:
    def addStrings(self, num1: str, num2: str) -> str: 
        x = len(num1)-1
        y = len(num2)-1
        carry = 0
        res = ""
        while (x >=0 or y >= 0):
            sum = carry
            if x >= 0:
                sum += ord(num1[x])-ord('0')
                x -= 1
            if y >= 0:
                sum += ord(num2[y])-ord('0')
                y -= 1
                
            res += str(sum%10)
            carry = sum//10
            
        if carry!= 0 :
            res += str(carry)
        return res[::-1]
        
        
                