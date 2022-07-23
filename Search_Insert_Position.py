'''Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Input: nums = [1,3,5,6], target = 5
Output: 2

Input: nums = [1,3,5,6], target = 2
Output: 1

Input: nums = [1,3,5,6], target = 7
Output: 4
'''
def searchInsert(nums, target):
    low, high = 0, len(nums)-1
    while low <= high:
        mid = (low+high)//2
            
        if nums[mid] == target:
            return mid
            
        elif nums[mid] > target:
            high = mid - 1
                
        else:
            low = mid + 1
                
    return low