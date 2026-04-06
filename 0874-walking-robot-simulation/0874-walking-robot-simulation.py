class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = set(map(tuple, obstacles))
        
        # Directions: North, East, South, West
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        dir = 0  # start facing North
        
        x = y = 0
        max_dist = 0
        
        for cmd in commands:
            if cmd == -1:  # turn right
                dir = (dir + 1) % 4
            elif cmd == -2:  # turn left
                dir = (dir - 1) % 4
            else:
                dx, dy = directions[dir]
                for _ in range(cmd):
                    if (x + dx, y + dy) not in obstacle_set:
                        x += dx
                        y += dy
                        max_dist = max(max_dist, x*x + y*y)
                    else:
                        break
        
        return max_dist
        