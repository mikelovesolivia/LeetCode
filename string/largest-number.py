class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num_str = [str(num) for num in nums]
        num_str.sort(key=functools.cmp_to_key(lambda a, b: 1 if a+b>b+a else -1), reverse=True)
        res = "".join(num_str)
        return "0" if res[0]=="0" else res