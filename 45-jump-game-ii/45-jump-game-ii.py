class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        count = 0
        right = 0
        jump = 0
        for i in range(len(nums)):
            right = max(right,i+nums[i])
            if i == jump:
                jump = right
                count += 1
                
            if jump >= len(nums)-1:
                break
        return count
        