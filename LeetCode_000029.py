"""
Divide Two Integers  


Divide two integers without using multiplication, division and mod operator.
If it is overflow, return MAX_INT.
"""

class Solution(object):
    def divide(self, dividend, divisor):
        positive = (dividend < 0) and (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

    dividend=input()
    divisor=input()
    print(divide(0,int(dividend),int(divisor)))
