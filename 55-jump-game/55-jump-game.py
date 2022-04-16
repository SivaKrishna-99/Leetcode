class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end_pos = 0
        
        for i,num in enumerate(nums):
            if end_pos < i :
                return False
            end_pos = max(end_pos,i+num)
        return True
            
        