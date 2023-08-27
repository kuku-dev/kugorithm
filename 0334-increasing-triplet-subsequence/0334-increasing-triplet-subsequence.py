class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        minimum = nums[0]
        maximum = sys.maxsize

        for curr in nums[1:]:
            if curr > maximum:
                return True
            if curr > minimum:
                maximum = curr
            if curr < minimum:
                minimum = curr
            
        return False