class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Kadane's Algorithm
        maxSum = float('-inf')
        currSum = 0
        for num in nums:
            currSum = max(num, currSum+num)
            maxSum = max(maxSum, currSum) 
        return maxSum