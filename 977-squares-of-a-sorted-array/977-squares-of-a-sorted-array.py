class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # for i in range(len(nums)):
        #     nums[i] *= nums[i]
        # nums.sort()    
        # return nums
        
        res = [0] * len(nums)
        left, right = 0, len(nums)-1
        
        while left <= right:
            begin, end = abs(nums[left]), abs(nums[right])
            if begin > end:
                res [right-left] = begin*begin
                left += 1
            else:
                res[right-left] = end*end
                right -= 1
        return res
    
    
    
    