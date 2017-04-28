"""
Longest Common Prefix


Write a function to find the longest common prefix string amongst an array of strings.
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        result = ""
        if len(strs) > 0:
            for i in range(len(strs[0])):
                temp = strs[0][0:i + 1]
                for j in range(1, len(strs)):
                    if len(strs[j]) >= i + 1 and temp == strs[j][0:i + 1]:
                        pass
                    else:
                        break
                else:
                    result = temp
        return result

    rawInput=input()
    arr=rawInput[1:len(rawInput)-1].split(',')
    data=[]
    for item in arr:
    	data.append(item)
    print(longestCommonPrefix(0,data))