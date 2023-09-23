class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I":1,"V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        res = 0
        idx = 0

        while idx < len(s):
            if idx == len(s)-1:
                res += roman_dict[s[idx]]
                break
            
            if s[idx] == "I":
                if s[idx+1] == "V":
                    res += 4
                    idx += 2
                elif s[idx+1] == "X":
                    res += 9
                    idx += 2
                else:
                    res += 1
                    idx += 1
            elif s[idx] == "V":
                res += 5
                idx += 1
            elif s[idx] == "X":
                if s[idx+1] == "L":
                    res += 40
                    idx += 2
                elif s[idx+1] == "C":
                    res += 90
                    idx += 2
                else:
                    res += 10
                    idx += 1
            elif s[idx] == "L":
                res += 50
                idx += 1
            elif s[idx] == "C":
                if s[idx+1] == "D":
                    res += 400
                    idx += 2
                elif s[idx+1] == "M":
                    res += 900
                    idx += 2
                else:
                    res += 100
                    idx += 1
            elif s[idx] == "D":
                res += 500
                idx += 1
            elif s[idx] == "M":
                res += 1000
                idx += 1

        return res