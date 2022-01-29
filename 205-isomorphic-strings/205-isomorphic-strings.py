class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict = {}
        for i in range(len(s)):
            c1 = s[i]
            t1 = t[i]
            if c1 not in dict:
                
                if t1 in dict.values() :
                    return False
                dict[c1] = t1
            elif dict[c1] != t1 :
                return False
            
        return True
        