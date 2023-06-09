'''
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
'''
# first Method
nums = [1,7,3,6,5,6]

def h(nums):
    for idx, i in enumerate(nums):
        

        lefft = sum(nums[:idx])
        rigght = sum(nums[idx+1:])
       # print("----", lefft, "   ", rigght)
        if lefft == rigght:
            return idx
            
    return -1
h(nums)

# second method
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = list(filter(lambda x:  sum(nums[:x]) == sum(nums[x+1:]),  range(len(nums))))

            
        return idx[0] if idx else -1