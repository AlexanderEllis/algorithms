# Heap Sort

# In this basic heap using list, left child is 2 * n, right child is 2 * n + 1
#

def max_heapify(input_list, index):
	"""
	Input: 
		input_list: heap that may not have max property (all children are <= parent)
		index: index at which we may need to swap
	
	Output: Heap with max property

	Note: middle boolean in first if so we always move the larger of the two up to keep max property
	"""
	heap = []
	heap.extend(input_list)
	if len(heap) > index * 2 + 2 and heap[index * 2 + 1] < heap[index * 2 + 2] and heap[index] < heap[index * 2 + 2]:
		temp = heap[index]
		heap[index] = heap[index * 2 + 2]
		heap[index * 2 + 2] = temp
		return max_heapify(heap, index * 2 + 2)
	elif len(heap) > index * 2 + 1 and heap[index] < heap[index * 2 + 1]:
		temp = heap[index]
		heap[index] = heap[index * 2 + 1]
		heap[index * 2 + 1] = temp
		return max_heapify(heap, index * 2 + 1)
	else: 
		return heap

def build_max_heap(input_list):
	"""
	Input: Heap without max property
	Output: Heap with max property
	"""
	max_heap = []
	max_heap.extend(input_list)
	for i in range(len(max_heap) // 2, -1, -1):
		max_heap = max_heapify(max_heap, i)
	return max_heap


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
