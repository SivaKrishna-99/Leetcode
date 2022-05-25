class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pool = [0]*1001
        for trip in trips:
            numPass,start,end = trip
            pool[start] += numPass
            pool[end] -= numPass
        curPass = 0
        for i in range(1001):
            curPass += pool[i]
            if curPass > capacity:
                return False
        return True
        