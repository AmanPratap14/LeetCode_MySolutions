'''
Given a string s, reverse the order of characters in each word within a 
sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
 
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
'''


def reverseWords(s):
    w= s.split()# builtin function to spilt string
    for i in range(len(w)):
        w[i]= w[i][::-1] #reversing string just before any space

    return ' '.join(w)


a= reverseWords("Let's take LeetCode contest")

print(a)