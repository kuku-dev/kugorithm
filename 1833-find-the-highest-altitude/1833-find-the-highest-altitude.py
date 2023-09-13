class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        highest = 0
        for l in gain:
            altitude += l

            if highest < altitude:
                highest = altitude

        return highest