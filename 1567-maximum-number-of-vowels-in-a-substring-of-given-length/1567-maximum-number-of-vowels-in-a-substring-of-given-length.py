class Solution:
    def maxVowels(self, s: str, k: int) -> int:
      vowels = ['a', 'e', 'i', 'o', 'u']
      subString = s[0:k]
      maxCnt = 0

      for c in subString:
          if c in vowels:
              maxCnt += 1
      curCnt = maxCnt

      for idx in range(1, len(s)-k+1):
          if s[idx-1] in vowels:
              curCnt -= 1

          if s[idx+k-1] in vowels:
              curCnt += 1

          if maxCnt < curCnt:
              maxCnt = curCnt

      return maxCnt