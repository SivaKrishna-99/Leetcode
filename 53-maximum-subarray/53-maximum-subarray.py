class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadane's Algorithm
        b = float('-inf')
        c = 0
        for num in nums:
            c = max(num, c+num)
            b = max(b, c) 
        return b