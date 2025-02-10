class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        queue = [0]
        visited = set()

        while queue:
            start = queue.pop(0)
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if end not in visited and s[start:end] in words:
                    queue.append(end)
                    visited.add(end)
        return False