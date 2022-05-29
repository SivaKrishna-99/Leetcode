class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        out = []
        hMap = {
            "2": "abc",
            "3":"def",
            "4": "ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        def combinations(i,curStr):
            if len(curStr) == len(digits):
                out.append(curStr)
                return
            for char in hMap[digits[i]]:
                combinations(i+1,curStr+char)
        if digits:
            combinations(0,"")
        return out