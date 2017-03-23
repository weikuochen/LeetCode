"""
Median of Two Sorted Arrays


There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. 
The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""

#LeetCode used python 2.7
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        fullList = nums1 + nums2
        result = 0
        median = len(fullList) // 2 #python3
        #median = len(fullList) / 2 #python2
        fullList = sorted(fullList)
        if len(fullList) % 2 == 0:
        	result = (fullList[median] + fullList[median - 1]) / 2 #python3
        	#result = (fullList[median] + fullList[median - 1]) / 2.0 #python2
        else:
        	result = fullList[median]
        return result

    rawInput = input()
    arr = rawInput[1:len(rawInput)-1].split(',')
    nums1 = []
    for item in arr:
        nums1.append(int(item))

    rawInput = input()
    arr = rawInput[1:len(rawInput)-1].split(',')
    nums2 = []
    for item in arr:
        nums2.append(int(item))

    print(findMedianSortedArrays(0,nums1,nums2))