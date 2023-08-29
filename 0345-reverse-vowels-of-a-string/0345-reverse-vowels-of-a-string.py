class Solution:
    def reverseVowels(self, s: str) -> str:
        gather = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        temp = []
        ret = ""
        for char in s:
            if char in gather:
                temp.append(char)

        idx = 0
        for char in s:
            if char in gather:
                ret += str(temp.pop())
            else:
                ret += char

        return ret
