class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i-1] :
#                 return True
            
        # return False
#         return len(set(nums)) < len(nums)
        d ={}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                return True
        return False
        