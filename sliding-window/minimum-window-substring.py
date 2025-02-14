class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        left = 0
        right = 0
        window = []
        ans = ""
        len_ans = float('inf')
        counter = collections.Counter(t)
        while right<n:
            window.append(s[right])
            if s[right] in counter:
                counter[s[right]] -= 1
                if counter[s[right]] == 0:
                    counter.pop(s[right])
                if not counter:
                    if len_ans > len(window):
                        len_ans = len(window)
                        ans = "".join(window)
                    left_letter = window.pop(0)
                    left += 1
                    while left_letter not in t:
                        left += 1
                        left_letter = window.pop(0)
                    counter[left_letter] += 1
            right += 1
        return ans
                