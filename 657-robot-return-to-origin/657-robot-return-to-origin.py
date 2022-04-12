class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        # #no of L's and R's equal and U and D's 
        # l,r,u,d = 0,0,0,0
        # for i in range(len(moves)):
        #     if moves[i] == 'L':
        #         l += 1
        #     elif(moves[i] == 'R'):
        #         r += 1
        #     elif(moves[i] == 'U'):
        #         u += 1
        #         print(u)
        #     else:
        #         d += 1
        #         print(d)
        # if l == r and u ==d :
        #     return True
        # else:
        #     return False
        
        xSum = 0
        ySum = 0
        for i in range(len(moves)):
            if moves[i] == 'L':
                xSum -= 1
            elif(moves[i] == 'R'):
                xSum += 1
            elif(moves[i] == 'U'):
                ySum += 1
            else:
                ySum -= 1
        if xSum ==0 and ySum == 0:
            return True
        else:
            return False
        
        