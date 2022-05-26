class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        #North, West, South, East - Anti clockwise direction
        dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        x,y = 0,0
        facing = 0
        for inst in instructions:
            if inst == "L":
                facing = (facing+1)%4
                
            elif(inst == "R"):
                facing = (facing-1)%4
                
            else:
                x += dir[facing][0]
                y += dir[facing][1]
                
        if facing != 0 or (x,y) == (0,0):
            return True
        else:
            return False
