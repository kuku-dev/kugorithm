class Solution:
    def reverseWords(self, s: str) -> str:
        split_words = s.split()
        ret = []
        for i in range(len(split_words), 0, -1):
            ret.append(split_words[i-1])

        return " ".join(ret)