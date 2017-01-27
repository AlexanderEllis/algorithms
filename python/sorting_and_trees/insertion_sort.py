# Insertion sort

def insertion_sort(input_list):
	"""
	Input: unsorted list
	Output: sorted list

	O(n^2) worst case
	"""
	length = len(input_list)
	for i in range(1, length):
		j = i
		while input_list[j - 1] > input_list[j] and j > 0:
			temp = input_list[j]
			input_list[j] = input_list[j - 1]
			input_list[j - 1] = temp
			j -= 1

	return input_list
