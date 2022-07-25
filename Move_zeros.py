"""
Given an integer array nums, move all 0's to the end of it while maintaining the 
relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

def MoveZeros(nums):
    position= 0

    for i in range(len(nums)):
        #checking if element is not 0
        if nums[i]!=0:
            #swaping elements
            nums[i], nums[position] =nums[position], nums[i]
            #increment postion pointer/indexs
            position +=1
            
    return nums

a= MoveZeros([0,1,0,3,12])
print(a)