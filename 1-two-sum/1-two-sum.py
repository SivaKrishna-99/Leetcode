class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i,req1 in enumerate(nums):
            req2 = target-req1
            if req2 in dict:
                return [dict[req2],i]
            else:
                dict[req1] = i
        