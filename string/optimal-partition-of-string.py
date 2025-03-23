class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        cur_s = []
        for c in s:
            if c in cur_s:
                cur_s = [c]
                count += 1
            else:
                cur_s.append(c)
        return count