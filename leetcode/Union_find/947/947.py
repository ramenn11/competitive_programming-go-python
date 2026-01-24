# 947. Most Stones Removed with Same Row or Column

from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px

        OFFSET = 100_001

        for x,y in stones:
            if not x in stones:
                parent[x] = x
            if not y + OFFSET in parent:
                parent[y + OFFSET] = y + OFFSET

            union(x, y + OFFSET)

        comps = set()   # connected components
        for x, y in stones:
            comps.add(find(x))

        return len(stones) - len(comps) # atleast one node must stay in the connected components