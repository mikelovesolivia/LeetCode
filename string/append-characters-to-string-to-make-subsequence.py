class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = j = 0
        n, m = len(s), len(t)
        while j < m:
            if i >= n:
                return m - j
            if s[i] == t[j]:
                j += 1
            i += 1
        return 0