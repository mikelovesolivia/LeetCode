class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        m = len(part)
        n = len(s)
        for i in range(n):
            stack.append(s[i])
            if len(stack) >= m:
                if "".join(stack[-m:]) == part:
                    stack = stack[:-m]
        return "".join(stack)