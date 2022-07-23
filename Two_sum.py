'''Given an array of integers nums of size n and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.

ex-2 Input : 
   4
   2 7 11 15
   9
Output : 
    0 1
Explaination : nums[0] + nums[1] == 9, return 0, 1

ex-1 Input : 
    3
    3 2 4
    6
Output : 
     1 2
'''

from collections import deque

def solve(n, nums, target):
    # CODE HERE
    dict_seen= {}

    for i, el in enumerate(nums):
        if target- el in dict_seen:
            return [dict_seen[target-el], i]
        dict_seen[el]= i

if __name__ == '__main__':
	n = int(input())
	nums = list(map(int, input().split()))
	target = int(input())
	out = solve(n, nums, target)
	print(*out)