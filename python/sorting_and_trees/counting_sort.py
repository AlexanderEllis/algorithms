"""
This is a version of a simple counting sort.  It's going to loop through the list to find the
maximum value.  It will then create a list of that size, initialized to zero.  It will then
loop through the original list, incrementing the value in the resulting list for each value as
index.  It will then work backwards through the list to create the mapping of position to value,
and finally it will fill in the values in a final resulting array.

"""

def counting_sort(input_list):
	"""
	This function assumes that the input list is a list of positive integers.  It will
	be a stable sort, so we will be able to use it as a sub-routine when we (we?) implement
	radix sort. It outputs a sorted list of integers.
	"""
	max_value = None
	for integer in input_list:
		if max_value is None:
			max_value = integer
		elif integer > max_value:
			max_value = integer
	counting_list = [0] * (max_value + 1)

	for integer in input_list:
		counting_list[integer] += 1

	for index in range(len(counting_list) - 1): # To ensure it's stable
		counting_list[index + 1] += counting_list[index]

	resulting_list = [0] * (len(input_list))

	for index in range(len(input_list) - 1, -1, -1):
		resulting_list[counting_list[input_list[index]] - 1] = input_list[index]
		counting_list[input_list[index]] -= 1

	return resulting_list
