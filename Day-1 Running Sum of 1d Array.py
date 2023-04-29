'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

'''

#one method (runtime 23ms)
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num= 0
        lst = []
        for i in nums:
            ii = i+ num
            lst.append(ii)
            num +=i
        return lst
    
# second Method (runtime 18ms )

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lst = [i+ sum(nums[:idx])for idx, i in enumerate(nums)]
        return lst
    
#Third Method 
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = list(map(lambda x: sum(nums[:x+1]), range(len(nums))))
        return result

