"""
Valid Parentheses


Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order, 
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""
class Solution(object):
    def isValid(self, s):
        result = False
        stack = []
        charMap = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if len(stack) == 0:
                    result = False
                    break
                else:
                    temp = stack.pop()
                if temp == charMap[i]:
                    result = True
                else:
                    result = False
                    break
        if len(stack) > 0:
            result = False
        return result

    s = input()
    print(isValid(0, s))