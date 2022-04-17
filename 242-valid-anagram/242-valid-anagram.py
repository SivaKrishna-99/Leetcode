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
        for c in t:
            if c in d2:
                d2[c] += 1
            else:
                d2[c] = 1
        for c in d1 :
            if( c not in d2):
                return False
            elif d1[c] == d2[c]:
                continue
            else:#count of char not same
                return False
          
        return True
        
        # s = sorted(s)
        # t = sorted(t)
        # return s == t