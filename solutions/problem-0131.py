# Daily Coding Problem: Problem #131 [Medium]
# This question was asked by Snapchat.

# Given the head to a singly linked list, where each node also has a “random” pointer
# that points to anywhere in the linked list, deep clone the list.
class ListNode:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.random = None

def deepClone(root):
	if root==None:
		return None

	node = root
	# clone list
	while node!=None:
		n = ListNode(node.data)
		n.next = node.next
		node.next = n
		node = n.next

	# set random pointer
	node = root
	while node!=None:
		if node.random != None:
			node.next.random = node.random.next
		node = node.next.next

	# separation
	dupl = root.next;
	node = root
	while node!=None:
		node.next = node.next.next
		node = node.next

	return dupl


if __name__ == '__main__':
	n1 = ListNode(1)
	n2 = ListNode(2)
	n3 = ListNode(3)
	n4 = ListNode(4)
	n5 = ListNode(5)

	n1.random = n3
	n2.random = n1
	n3.random = n5
	n4.random = None
	n5.random = n5

	deepClone(n1)