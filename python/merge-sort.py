# Merge sort

import random

random_array = []

for x in range(0, 100):
	random_array.append(random.randint(0,100))

def merge_arrays(array_A, array_B):
	merged_array = []
	i = 0
	j = 0
	while len(merged_array) < len(array_A) + len(array_B):
		if j == len(array_B) or (i != len(array_A) and array_A[i] <= array_B[j]):
			merged_array.append(array_A[i])
			i += 1
		else:
			merged_array.append(array_B[j])
			j += 1
	return merged_array

def merge_sort(input_array):
	length = len(input_array)
	if length == 1:
		return input_array
	else:
		return merge_arrays(merge_sort(input_array[length // 2:]), merge_sort(input_array[:length // 2]))

print(merge_sort(random_array))
