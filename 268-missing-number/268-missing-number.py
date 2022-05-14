class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        n  = len(nums)
        for i in range(len(nums)):
            sum += nums[i]
        nSum = (n*(n+1))//2
        return nSum-sum