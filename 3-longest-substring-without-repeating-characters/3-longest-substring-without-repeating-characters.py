class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == ' ':
            return 1
        if s == "":
            return 0
        start = 0
        d1 = {}
        curr_len = 0
        max_len = 0
        
        for i in range(len(s)):
            
            if s[i] in d1:
                start = max(start,d1[s[i]]+1)
                d1[s[i]] = i
                curr_len = i-start+1
                max_len = max(curr_len,max_len)
            else:
                d1[s[i]] = i
                curr_len = i-start+1
                max_len = max(curr_len,max_len)
                
        return max_len