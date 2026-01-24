# n^2 solution since n <= 1000, n = number of stones

from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        visited = [False] * n

        def dfs(i):
            for j in range(n):
                if not visited[j]:
                    if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:  # same row or column
                        visited[j] = True
                        dfs(j)

        comp_cnt = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                comp_cnt += 1

        return n - comp_cnt