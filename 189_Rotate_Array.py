'''Given an array, rotate the array to the right by k steps,
where k is non-negative.
 
Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

'''
'''def rotate(nums, k):
    k= k% len(nums)
    #if k= len(nums) we are basically rotating entire array as 0 time
    l, r= 0 ,len(nums)-1
    while l <r:
        nums[l], nums[r]= nums[r], nums[l]#swapping ele
        l, r= l+1, r-1

    # next thing we are doing reverseing first K ele
    #then reverse the remaining portion
    l, r= 0 ,k-1
    while l <r:
        nums[l], nums[r]= nums[r], nums[l]#swapping ele
        l, r= l+1, r-1
    
    # next thing we are doing reverseing remaining portion K ele
    l, r= k ,len(nums)-1
    while l <r:
        nums[l], nums[r]= nums[r], nums[l]#swapping ele
        l, r= l+1, r-1
    '''

def rotate(nums, k):
    def twopt(arr, i, j):
        while (i < j):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return arr
#if k= len(nums) we are basically rotating entire array as 0 time
    if k > len(nums):
        k %= len(nums)

    if (k > 0):
        twopt(nums, 0, len(nums) - 1)  # rotate entire array
        twopt(nums, 0, k - 1)          #  # next thing we are doing reverseing first K ele
    #then reverse the remaining portion
        twopt(nums, k, len(nums) - 1)  # rotate array from k to end of array
    

    
'''size = len(nums)
    tmp_nums = [None]*size
    k = k%size
    for indx in range(len(nums)):
        tmp_nums[(indx+k)%size] = nums[indx]
               
    for indx in range(len(nums)):
        nums[indx] = tmp_nums[indx]
        '''

a= rotate([1,2,3,4,5,6,7], 3)
print(a)
