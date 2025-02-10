class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        x_max = round(n**(1/x))
        weights = [i**x for i in range(1, x_max+1)]
        m = len(weights)
        dp = [0] * (n + 1)
        dp[0] = 1
        MOD = 1e9 + 7
        for i in range(m):
            for j in range(n, weights[i]-1, -1):
                dp[j] += dp[j-weights[i]] % MOD
        return int(dp[-1] % MOD)