class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        temp = ""
        for c in s.lower():
            if c.isalpha() or c.isdigit():
                temp += c
        
        pre = 0
        post = len(temp)-1

        while pre <= post:
            if temp[pre] == temp[post]:
                pre += 1
                post -= 1
            else:
                return False
        return True