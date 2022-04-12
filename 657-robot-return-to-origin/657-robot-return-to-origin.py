class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        #no of L's and R's equal and U and D's 
        l,r,u,d = 0,0,0,0
        print("Hello")
        for i in range(len(moves)):
            print("is it entering the loop")
            if moves[i] == 'L':
                l += 1
            elif(moves[i] == 'R'):
                r += 1
            elif(moves[i] == 'U'):
                u += 1
                print(u)
            else:
                d += 1
                print(d)
        if u == d and l == 0 and r == 0:
                return True
        if l == r and u == 0 and d == 0:
                return True
        if l == r and u ==d :
                return True
        else:
            return False
        