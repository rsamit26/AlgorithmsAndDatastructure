"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9.
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5
below 1000.

"""

class Solution:

    def sumOfMultiple(self, n):
        multiple = []

        for i in range(3,n,3):
            if i%3 ==0 and i%5!=0:
                multiple.append(i)
        for i in range(5,n,5):
            if i%5==0 and i%3 != 0:
                multiple.append(i)
        for i in range(15,n,15):
            if i%5==0 and i%3 == 0:
                multiple.append(i)
        return sum(multiple)

s = Solution()
print(s.sumOfMultiple(1000))
