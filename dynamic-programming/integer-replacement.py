class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        while n>1:
            if n==3:
                return count+2
            if n % 2==0:
                n=n//2
                count+=1
            else:
                if ((n-1)/2)%2==0:
                    n = n-1
                else:
                    n=n+1
                count += 1
            
        return count

