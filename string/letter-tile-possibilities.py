class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = collections.Counter(tiles)
        def backtrack():
            total = 0
            for char in count:
                if count[char] > 0:
                    count[char] -= 1
                    total += 1 + backtrack()
                    count[char] += 1
            return total
        return backtrack()
