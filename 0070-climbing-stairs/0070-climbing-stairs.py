class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        ret = [0] * (n+1)
        ret[0] = 1
        ret[1] = 1
        for i in range(2, n+1):
            ret[i] = ret[i-1] + ret[i-2]
        return ret[n]