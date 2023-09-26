class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        minLen = 200
        for str in strs:
            if len(str) < minLen:
                minLen = len(str)


        for idx in range(0, minLen):
            comp = strs[0][idx]
            for str in strs:
                if comp != str[idx]:
                    return res
            res += comp

        return res