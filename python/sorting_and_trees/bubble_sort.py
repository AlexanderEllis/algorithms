# Bubble Sort

def bubble_sort(input_list):
	"""
	Input unsorted list, output sorted list
	"""
	list_sorted = False
	while not list_sorted:
		changed = False
		length = len(input_list)
		for i in range(0, length):
			if i != length - 1 and input_list[i] > input_list[i + 1]:
				temp = input_list[i]
				input_list[i] = input_list[i + 1]
				input_list[i + 1] = temp
				changed = True
		if not changed:
			list_sorted = True
	return input_list

