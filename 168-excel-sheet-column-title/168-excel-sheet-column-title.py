class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        ans = ''
        while columnNumber > 0:
            y = (columnNumber-1) % 26
            columnNumber = (columnNumber-1) // 26
            s = chr(y+ord('A') )
            ans = ''.join((s, ans))

        return ans
            