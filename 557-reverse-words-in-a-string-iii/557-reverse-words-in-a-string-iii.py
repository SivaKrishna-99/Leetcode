class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()
        ans = []
        for word in s:
            l = 0
            r = len(word)-1
            while(l < r):
                word = list(word)
                word[l], word[r] = word[r],word[l]
                l += 1
                r -= 1
            ans1 = (''.join(word))
            ans.append(ans1)
        return(' '.join(ans))
                
    
     

    
        