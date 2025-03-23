class Solution:
    def numberOfWays(self, s: str) -> int:
        n0 = n1 = n01 = n10 = n101 = n010 = 0
        for c in s:
            if c == '0':
                n0 += 1
                n010 += n01  # 形成 '010'
            else:  # c == '1'
                n1 += 1
                n101 += n10  # 形成 '101'

            if c == '0':
                n10 += n1  # 形成 '10'
            else:
                n01 += n0  # 形成 '01'
        return n101 + n010
        # n = len(s)
        # if n < 3:
        #     return 0
        # n0 = [0] * n
        # n1 = [0] * n
        # n01 = [0] * n
        # n10 = [0] * n
        # n101 = [0] * n
        # n010 = [0] * n
        # n0[0] = 1 if s[0] == '0' else 0
        # n1[0] = 1 if s[0] == '1' else 0
        # for i in range(1, n):
        #     n0[i] = n0[i-1] + 1 if s[i] == '0' else n0[i-1]
        #     n1[i] = n1[i-1] + 1 if s[i] == '1' else n1[i-1]
        #     n01[i] = n01[i-1] if s[i] == '0' else n01[i-1] + n0[i-1]
        #     n10[i] = n10[i-1] if s[i] == '1' else n10[i-1] + n1[i-1]
        #     n101[i] = n101[i-1] if s[i] == '0' else n101[i-1] + n10[i-1]
        #     n010[i] = n010[i-1] if s[i] == '1' else n010[i-1] + n01[i-1]
        # return n101[-1] + n010[-1]