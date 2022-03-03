class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Two methods - Sorting(O(NlogN)) and Using HAshmap(O(N))
        if len(s) != len(t):
            return False
        d1 = {}
        d2 = {}
        
        for c in s:
            if c in d1:
                d1[c] += 1
            else:
                d1[c] = 1
        for d in t:
            if d in d2:
                d2[d] += 1
            else:
                d2[d] = 1
        for a in d1 :
            
            if( a not in d2):
                return False
            elif d1[a] == d2[a]:
                continue
            else:
                return False
        return True
        