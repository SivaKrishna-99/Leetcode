class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            temp = abs(num)
            if nums[temp] > 0:
                nums[temp] = - nums[temp]
            else:
                duplicate = temp
                break
        for i in range(len(nums)):
            if nums[i] < 0 :
                nums[i] = -nums[i]

        return duplicate
                
        