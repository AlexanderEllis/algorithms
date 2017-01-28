# BST Search

# First we have to make the structure of a BST

class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.value = val

def insert_into_tree(root, node):
	"""
	Recursively find root to append node to
	"""
	if root is None:
		root = node
	else:
		if root.value > node.value:
			if not root.left:
				root.left = node
			else:
				insert_into_tree(root.left, node)
		else:
			if not root.right:
				root.right = node
			else:
				insert_into_tree(root.right, node)

def insert_in_order(root, input_list):
	"""
	Input: root of bst, list to append to
	"""
	if not root:
		return
	insert_in_order(root.left, input_list)
	input_list.append(root.value)
	insert_in_order(root.right, input_list)

def bst_sort(input_list):
	"""
	Input: unsorted list
	Output: sorted list
	"""
	bst_values = []
	bst_values.extend(input_list)
	bst_root = Node(bst_values[0])
	for i in range(1, len(bst_values)):
		insert_into_tree(bst_root, Node(bst_values[i]))
	
	result_list = []
	insert_in_order(bst_root, result_list)

	return result_list
