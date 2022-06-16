class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #Easy usnig hash set
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
        for i in range(1,len(nums)+2):
            if i not in seen:
                return i
                
        