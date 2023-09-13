class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
      maxSum = sum(nums[0:k])
      curSum = maxSum

      for idx in range(1, len(nums)-k+1):
          curSum = curSum - nums[idx-1] + nums[idx+k-1]
          if maxSum <= curSum:
              maxSum = curSum
              
      return round(maxSum/k, 5)
