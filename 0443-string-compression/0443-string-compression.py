class Solution:
    def compress(self, chars: List[str]) -> int:
        cur = ""
        count = 0
        res = ""
        for idx, char in enumerate(chars):
            if cur != char:
                res += cur
                if count > 1:
                    res += str(count)
                cur = char
                count = 1
            else:
                count += 1

            if idx+1 == len(chars):
                res += cur
                if count > 1:
                    res += str(count)

        chars.clear()
        for c in res:
            chars.append(c)

        return len(chars)