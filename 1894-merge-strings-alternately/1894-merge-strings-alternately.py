class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len = len(word1)
        word2_len = len(word2)
        remain = ""
        ret = ""
        if word1_len > word2_len:
            remain = word1[word2_len:]
        elif word1_len < word2_len:
            remain = word2[word1_len:]
        
        for w1, w2 in zip(word1, word2):
            ret += w1 + w2
        return ret + remain