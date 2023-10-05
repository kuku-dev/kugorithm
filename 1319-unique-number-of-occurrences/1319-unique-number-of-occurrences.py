class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        res = []
        d = Counter(arr)

        for _, cnt in d.items():
            if cnt in res:
                return False
            else:
                res.append(cnt)
                
        return True
    