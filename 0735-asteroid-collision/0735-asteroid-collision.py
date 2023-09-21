class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        idx = 0 

        while idx < len(asteroids)-1:
            if asteroids[idx] > 0 and asteroids[idx+1] < 0:
                if abs(asteroids[idx]) == abs(asteroids[idx+1]):
                    asteroids.pop(idx)
                    asteroids.pop(idx)
                    idx = max(0, idx-1)
                else:
                    if abs(asteroids[idx]) < abs(asteroids[idx+1]):
                        asteroids.pop(idx)
                    else:
                        asteroids.pop(idx+1)

                    idx = max(0, idx-1)
            else:
                idx += 1

        return asteroids