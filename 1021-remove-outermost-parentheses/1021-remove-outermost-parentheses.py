class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        paranOpen = 0
        ans = []
        for c in s:
            if c == ')':
                paranOpen -= 1
            if paranOpen > 0:
                ans.append(c)
            # this if condition should be last as the first '(' should not be appended.
            if c == '(':
                paranOpen += 1
        return ''.join(ans)
        
        
        