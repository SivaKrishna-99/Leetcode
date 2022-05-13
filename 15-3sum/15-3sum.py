class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        tripletList = []
        
        for i in range(len(nums)-1):
            if i >0 and nums[i] == nums[i-1]:
                continue
            j,k = i+1,len(nums)-1
            while j < k:
                sum = nums[j]+nums[k]
                if sum == -nums[i]:
                    tripletList.append([nums[i],nums[j],nums[k]])
                    
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                    
                elif(sum > -nums[i]):
                    k -= 1
                else:
                    j += 1
            
        return tripletList
                
        
        