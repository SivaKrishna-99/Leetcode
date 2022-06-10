class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        
        for i in range(1,n+1):
            #This will be able to deal even if the FizzBuzz string size varies.s
            sub_ans = ''
            if (i%3 == 0) :
                sub_ans = 'Fizz'
            if( i%5 == 0):
                sub_ans += 'Buzz'
            if not sub_ans:
                sub_ans = str(i)
            answer.append(sub_ans)
        
        return answer
        

        