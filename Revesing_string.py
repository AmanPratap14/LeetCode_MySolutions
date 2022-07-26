'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''


def ReversingString(s):
    l, r= 0, len(s)-1
#simply using two pointer on 0(index) and len(s)-1 Index
    while l<=r:
        #just swapping 
        s[l], s[r]= s[r], s[l]
        l+=1
        r-=1
    return s


a= ReversingString(["h","e","l","l","o"])
print(a)