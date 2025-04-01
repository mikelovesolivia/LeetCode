class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)

        SUM = sum(cookies)
        subsum = [0] * k
        self.res = float('inf')
    
        def backtrack(i):
            if i == n:
                self.res = min(self.res, max(subsum))
                return
            for j in range(k):
                subsum[j] += cookies[i]
                backtrack(i+1)
                subsum[j] -= cookies[i]
                if subsum[j] == 0:
                    break
        backtrack(0) 
        return self.res