class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        dict = {}
        
        for task in tasks:
            if task not in dict:
                dict[task] = 1
            else:
                dict[task] += 1
        #Getting only the values from the dictionary
        # dict = [value for key, value in dict.items()]#
        # dict.items() returns both the (k-v) pairs
        # dict.keys() returns the keys of the dictinary
        dict = list(dict.values())
        
        # highest num of times a character occured.
        max_count = max(dict)
        # Characters which occured with max count
        task_max_count = dict.count(max_count)
        
        return max(len(tasks), (max_count-1)*(n+1) + task_max_count )
        