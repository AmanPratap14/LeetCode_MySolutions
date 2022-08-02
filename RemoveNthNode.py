'''Given the head of a linked list, remove the nth node from the end of the 
list and return its head.
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
'''
from collections import deque
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


def convertToLL(arr, n):
	head = None
	tail = None
	for i in arr:
		node = Node(int(i))
		if not head:
			head = node
		if tail:
			tail.next = node
		tail = node
	return head


def printLL(head):
	while head:
		print(head.data, end = ' ')
		head = head.next
	print()

#main  code
def solve(head, n):
    # CODE HERE
    s= head
    while(n>0):
        s= s.next
        n -= 1
    #using two pointer s, t first s increment k-1 time
    if s == None:
        return head.next
        
    t= head
#after that while s on k-1 index t start increment as follow one 
    while(s.next):
        t= t.next
        s= s.next

    t.next= t.next.next
    return head


if __name__ == '__main__':
	raw_array = list(map(int, input().split()))
	head = convertToLL(raw_array, len(raw_array))
	n = int(input())
	res = solve(head, n)
	printLL(res)

