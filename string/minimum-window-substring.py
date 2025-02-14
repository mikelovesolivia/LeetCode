class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        left = 0
        right = 0
        window_counts = {}
        len_ans = float('inf')
        counter = collections.Counter(t)
        required = len(counter)
        formed = 0
        min_window = ""
        while right<n:
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            if char in counter and window_counts[char] == counter[char]:
                formed += 1
            while left<=right and formed == required:
                if right-left+1 < len_ans:
                    len_ans = right - left + 1
                    min_window = s[left:right+1]
                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in counter:
                    formed -= 1
                left += 1
            right += 1
        return min_window