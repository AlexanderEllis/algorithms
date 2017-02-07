# Binary Search

def binary_search(array, value):
	"""
	Given sorted list and value, returns boolean on whether or not the value exists in the list
	"""
	length = len(array)
	if length == 1 and array[0] == value:
		return True
	elif length == 1:
		return False
	elif array[length // 2] > value:
		return binary_search(array[: length // 2], value)
	else:
		return binary_search(array[length // 2 :], value)
