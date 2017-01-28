# Heap Sort

# In basic heap using list, left child is 2 * n, right child is 2 * n + 1
#
# [0, 1, 2, 3, 4, 5, 6]
#
#			     0
#		     /      \
#		   1           2
#        /  \          / \
#       3   4         5   6
#      /\   /\       /\   /\
#	  7 8  9  10   11 12 13 14

def max_heapify(input_list, index):
	"""
	Input: 
		input_list: heap that may not have max property (all children are <= parent)
		index: index at which we may need to swap
	
	Output: Heap with max property

	Note: middle boolean in first if so we always move the larger of the two up to keep max property
	"""
	if len(input_list) > index * 2 + 2 and input_list[index * 2 + 1] < input_list[index * 2 + 2] and input_list[index] < input_list[index * 2 + 2]:
		temp = input_list[index]
		input_list[index] = input_list[index * 2 + 2]
		input_list[index * 2 + 2] = temp
		return max_heapify(input_list, index * 2 + 2)
	elif len(input_list) > index * 2 + 1 and input_list[index] < input_list[index * 2 + 1]:
		temp = input_list[index]
		input_list[index] = input_list[index * 2 + 1]
		input_list[index * 2 + 1] = temp
		return max_heapify(input_list, index * 2 + 1)
	else: 
		return input_list

def build_max_heap(input_list):
	"""
	Input: Heap without max property
	Output: Heap with max property
	"""
	for i in range(len(input_list) // 2, -1, -1):
		input_list = max_heapify(input_list, i)
	return input_list


def heap_sort(input_list):
	"""
	Input: unsorted list
	Output: sorted list
	O(nlogn): swap is constant, max_heapify is log(n)
	"""
	heap = []
	heap.extend(build_max_heap(input_list))
	result_list = []
	for i in range(len(heap) - 1, -1, -1):
		temp = heap[i]
		heap[i] = heap[0]
		heap[0] = temp
		result_list.insert(0,heap.pop())
		heap = max_heapify(heap,0)
	return result_list
