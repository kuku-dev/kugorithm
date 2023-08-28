class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        x1 = 0
        x2 = len(height)-1

        while x1 < x2:
            area = max(area, (x2-x1) * min(height[x1], height[x2]))
            if height[x1] < height[x2]:
                x1 += 1
            else:
                x2 -= 1

        return area