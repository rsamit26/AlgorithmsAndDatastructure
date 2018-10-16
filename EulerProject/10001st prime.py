"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""

class Solution:

    def isPrime(self, n):
        if n == 1:
            return False
        elif n < 4:
            return True
        elif n%2 == 0:
            return False
        elif n<9:
            return True
        elif n%3 == 0:
            return False
        else:
            import math
            r = math.floor(math.sqrt(n))
            f = 5
            while f <=r:
                if n%f==0:
                    return False
                if n% (f+2) == 0:
                    return False
                f+=6
        return True

    def genratePrime(self, n):
        if n==1:
            return 2            
        idx, nth_prime = 1,1
        while idx < n:
            nth_prime+= 2
            if self.isPrime(nth_prime):
                idx+= 1
        return nth_prime





s = Solution()
print(s.genratePrime(1))
