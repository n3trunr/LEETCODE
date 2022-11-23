'''

Given an array nums of integers, return how many of them contain an even number of digits.

Constraints:
1 <= nums.length <= 500
1 <= nums[i] <= 105

'''

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            if (len(str(abs(n)))%2==0):
                count += 1
        return count
