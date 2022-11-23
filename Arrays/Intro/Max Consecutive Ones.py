'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.
Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

'''

def max_consecutive_ones(nums):
    consecutive_ones = 0
    max = 0
    for n in nums:
        if (n == 1):
            consecutive_ones+=1
        else:
            consecutive_ones = 0
        if(consecutive_ones>max):
            max = consecutive_ones
    return max


INPUTS = [
    [1,1,0,1,1,1],
    [1,0,1,1,0,1]
]

for i in INPUTS:
    print(i)
    print("max_consecutive_ones(): ")
    print(max_consecutive_ones(i))