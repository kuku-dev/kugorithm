class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for idx in range(len(flowerbed)):
            if flowerbed[idx] == 0 and (idx == 0 or flowerbed[idx-1] == 0) and (idx == len(flowerbed)-1 or flowerbed[idx+1] == 0):
                flowerbed[idx] = 1
                n -= 1
                if n == 0:
                    return True
        return False