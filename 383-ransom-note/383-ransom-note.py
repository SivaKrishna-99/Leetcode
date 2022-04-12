class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(ransomNote) > len(magazine):
            return False
        d1 = {}
        for c in magazine:
            if c in d1:
                d1[c] += 1
            else:
                d1[c] = 1
        for c in ransomNote:
            if c in d1 and d1[c] > 0:
                d1[c] -= 1                
            else:
                return False
        return True
        