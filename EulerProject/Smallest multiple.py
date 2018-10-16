"""
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by
all of the numbers from 1 to 20?
"""

class Solution:

    def smallestMultiple(self, n):
        # LCM of number till note N
        x = 1
        while n > 1:
            x=  self.lcm(n, x)
            n-=1
        return x

    def gcd(self, a, b):
        if not a:
            return b
        else:
            return self.gcd(b%a,a)
    def lcm(self, a, b):
        return abs(a*b)//self.gcd(a,b)

    def genratePrime(self, n):
        prime = [True]*(n+1)
        p,i = [],2
        import math
        while (i*i < n):
            if prime[i] == True:
                for j in range(i*2, n+1, i):
                    prime[j] = False
            i+=1
        for i in range(2, n):
            if prime[i]:
                p.append(i)
        return p





s = Solution()
print(s.smallestMultiple(2))
