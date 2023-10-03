from collections import deque

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        res = []
        for word in words:
            reverse = ""
            queue = deque(word)
            for i in range(len(word)):
                reverse += queue.pop()
            res.append(reverse)

        res = " ".join(res)

        return res