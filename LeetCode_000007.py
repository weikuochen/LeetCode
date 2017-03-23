"""
Reverse Integer   


Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. 
Your function should return 0 when the reversed integer overflows.
"""
class Solution(object):
    def reverse(self, x):
        m = -1 if x < 0 else 1
        result=''
        for w in str(x):
        	if w!='-':
        		result=w+result
        r=int(result)
        if r > 0x7FFFFFFF:
            return 0
        return m*r

    rawInput=input()
    print(reverse(0,int(rawInput)))


