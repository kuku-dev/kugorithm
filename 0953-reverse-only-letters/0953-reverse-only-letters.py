class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        temp = []
        res = []
        for c in s:
            if str(c).isalpha():
                temp.append(c)
            
        for idx in range(len(s)):
            if str(s[idx]).isalpha():
                res.append(temp.pop())
            else:
                res.append(s[idx])
            
        return "".join(res)