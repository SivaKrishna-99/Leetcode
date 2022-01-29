class Solution:
    def romanToInt(self, s: str) -> int:
        romNum = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
        
        ans = 0
        
        for i in range(len(s)-1):
            if romNum[s[i]] < romNum[s[i+1]]:
                ans -= romNum[s[i]]
            else:
                ans += romNum[s[i]]
        return ans+romNum[s[-1]]
        
        