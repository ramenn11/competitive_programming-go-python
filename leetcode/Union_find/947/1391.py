# 1391. Check if There is a Valid Path in a Grid
from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        dirs = {
            1: [(0,-1),(0,1)], # LEFT-RIGHT
            2: [(-1,0),(1,0)], # UP-DOWN
            3: [(0,-1),(1,0)], # LEFT-DOWN
            4: [(0,1),(1,0)],  # RIGHT-DOWN
            5: [(0,-1),(-1,0)],# LEFT-TOP
            6: [(0,1),(-1,0)] # RIGHT-TOP
        }

        rev = {
            (0,-1):(0,1), (0,1):(0,-1),
            (-1,0):(1,0), (1,0):(-1,0)
        }

        from collections import deque
        q = deque([(0, 0)])
        seen = {(0,0)}

        while q:
            x, y = q.popleft()
            if (x, y) == (m-1, n-1):
                return True
            
            for dx, dy in dirs[grid[x][y]]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < 0:
                    if rev[(dx, dy)] in dirs[grid[nx][ny]] and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        q.append((nx, ny))

        return False