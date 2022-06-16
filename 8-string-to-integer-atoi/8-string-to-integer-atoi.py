class Solution:
    def myAtoi(self, s: str) -> int:
        index = 0 
        n = len(s)
        sign = 1
        ans = 0
        #check for leading white spaces 
        while index < n and s[index] == ' ':
            index += 1
        #check for sign
        if index < n and s[index] == '+':
            sign = 1
            index += 1
        elif(index < n and s[index] == '-'):
            sign = -1
            index += 1
        
        #check for the digits
        
        while index < n and s[index].isdigit():
            
            digit = int(s[index])
            
            # final result validation
            if ( (ans > (pow(2,31)-1)//10) or (ans == (pow(2,31)-1)//10) and digit > ((pow(2,31)-1) % 10) ):
                if sign == 1:
                    return pow(2,31)-1
                else:
                    return -pow(2,31)
            ans = ans*10 +digit
            index += 1
        
        return sign*ans
        
        