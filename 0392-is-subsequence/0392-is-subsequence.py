class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)
        true_num = 0
        start_idx = 0
        if s == "":
            return True

        for s_sub in s:
            for idx in range(start_idx, len(t)):
                if s_sub == t[idx]:
                    true_num += 1
                    start_idx = idx+1
                    break
                
                if idx+1 == len(t):
                    return False
                
            if s_len == true_num:
                return True