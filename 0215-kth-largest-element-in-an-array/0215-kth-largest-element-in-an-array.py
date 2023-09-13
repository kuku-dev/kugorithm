class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        temp = []
        for num in nums:
            heapq.heappush(temp, -num)

        ret = 0
        for i in range(0, k):
            ret = heapq.heappop(temp) * -1

        return ret