class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = ""
        for digit in digits:
            temp += str(digit)

        res = []
        temp = int(temp) + 1
        for i in str(temp):
            res.append(int(i))

        return res
