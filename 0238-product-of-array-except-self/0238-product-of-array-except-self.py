class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)
        ret = [1] * len(nums)
        
        pre[0] = nums[0]
        for idx in range(1, len(nums)):
            pre[idx] = pre[idx-1] * nums[idx]

        post[len(nums)-1] = nums[len(nums)-1]
        for idx in range(len(nums)-2, -1, -1):
            post[idx] = post[idx+1] * nums[idx]

        for idx in range(len(nums)):
            if idx == 0:
                ret[idx] = post[idx+1]
            elif idx == len(nums)-1:
                ret[idx] = pre[idx-1]
            else:
                ret[idx] = pre[idx-1] * post[idx+1]
        return ret