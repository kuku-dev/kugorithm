class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        else:
            ret = 1
            while True:
                if x >= ret*ret:
                    ret += 1
                else:
                    return ret-1