class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d1 ={}
        freq = [[] for _ in range(len(nums)+1)]
        #[ [ ] for _ in range(len(4) ) ] - gives [ [],[],[],[] ]
        
        res = []
        if k == len(nums):
            return nums
        
        for num in nums:
            if num in d1:
                d1[num] += 1
            else:
                d1[num] = 1
        #To get the count of values 
        #for num in nums:
        #     d1[num] = 1+ d1.get(num,0)
        # d1 = Counter(nums).items()
        #BucketSort- Where a num is appended to its count 
        for  num,count in d1.items():
            freq[count].append(num)
        #Traverse from the end of the freq array as we have to print numbers with higher count first
        for count in range(len(freq)-1,0,-1):
            for num in freq[count]:
                res.append(num)
                if len(res) == k:
                    return res
        
        # return heapq.nlargest(k,d1.keys(),key = d1.get)
            