class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grp_anagrams = defaultdict(list)
        # grp_anagrams = {}
        
        for s in strs:
            freq = [0]*26
            for c in s:
                freq[ord(c)-ord("a")] += 1    
            grp_anagrams[tuple(freq)].append(s) 
            #here freq is a list but in python, lists can't be keys so we use tuples which are non-mutable 
        return grp_anagrams.values()
        
        