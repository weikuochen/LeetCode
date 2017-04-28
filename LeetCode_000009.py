"""
Palindrome Number

Determine whether an integer is a palindrome. Do this without extra space.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, 
note the restriction of using extra space.

You could also try reversing an integer. 
However, if you have solved the problem "Reverse Integer", 
you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
"""
class Solution(object):
    def isPalindrome(self, x):
        result = False
        if x < 0:
            pass
        elif x >= 0 and x < 10:
            result = True
        else:
            for i in range(len(str(x)) / 2):
                if str(x)[i] != str(x)[-(i + 1)]:
                    break
            else:
                result = True
        return result
    
    x = int(input())
    print(isPalindrome(0, x))