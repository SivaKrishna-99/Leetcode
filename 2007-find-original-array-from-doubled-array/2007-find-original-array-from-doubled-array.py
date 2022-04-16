class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2 is not 0:
            return []
        original = []
        changed.sort()
        d1 = {}
        for num in changed:
            if num in d1:
                d1[num] += 1
            else:
                d1[num] = 1
        
        for num in changed:
            if d1[num] >= 1:
                idx = num*2
                d1[num] -= 1
                if idx in d1 and d1[idx] >= 1:
                    original.append(num)
                    d1[idx] -= 1
                print(num)
                    
        if len(changed)//2 == len(original):
            return original
        else:
            return []
        
        
        
        
        
        
        
        

        
            
            
        