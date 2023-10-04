from collections import deque
from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gidx = 0
        sidx = 0
        count = 0
        while gidx < len(g) and sidx < len(s):
            if g[gidx] <= s[sidx]:
                count += 1
                gidx += 1
                sidx += 1
            else:
                sidx += 1

        return count