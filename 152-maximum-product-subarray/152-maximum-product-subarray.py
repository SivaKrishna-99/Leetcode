class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        max_prod = nums[0]
        min_prod = nums[0]
        for i in range(1,len(nums)):
            prod = nums[i]*max_prod
            max_prod = max(nums[i]*max_prod,nums[i]*min_prod,nums[i])
            min_prod = min(nums[i]*min_prod,prod,nums[i])
            ans = max(ans,max_prod)
        return ans
                
        
        
        

                
            