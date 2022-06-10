class Solution:
    def fizzBuzz(self,n:int)->List[str]:
        answer = []
        fb_D = {3:'Fizz',5:'Buzz'}#constant space
        for i in range(1,n+1):
            sub_ans = ''
            #this for loop takes constant time as it only has two keys.
            for key in fb_D.keys():
                if i%key == 0:
                    sub_ans += fb_D[key]
            if not sub_ans:
                sub_ans = str(i)
            answer.append(sub_ans)
        return answer