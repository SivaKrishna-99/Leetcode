class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        b_Sum = float('-inf')
        c_Sum = 0
        for a in nums:
            c_Sum = max(a, c_Sum+a)
            b_Sum = max(b_Sum, c_Sum)
            
        return b_Sum