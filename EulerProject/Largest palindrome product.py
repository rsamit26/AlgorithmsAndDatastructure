"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

class Solution:

    def largestPallindrome(self, k):
        n = 10**k-1
        l = []
        for i in range(n,10**(k-1), -1):
            for j in range(n, i-1,-1):
                if str(i*j) == str(i*j)[::-1]:
                    l.append(i*j)
                    break
        return max(l)

    def method_02(self, k):
        a = 10**k - 1
        largest_palindrome = 0
        while a > 10**(k-1):
            if a%11==0:
                b = 10**k - 1
                db = 1
            else:
                b = 10**k + 1 -11
                db = 11
            while b>=a:
                if a*b <= largest_palindrome:
                    break
                if str(a*b) == str(a*b)[::-1]:
                    largest_palindrome = a*b
                b = b-db
            a -= 1
        return largest_palindrome

s = Solution()
print(s.largestPallindrome(3))
print(s.method_02(3))
