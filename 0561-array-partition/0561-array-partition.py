class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        res = 0
        for idx in range(1, len(nums),2):
            res += min(nums[idx-1], nums[idx])
        return res