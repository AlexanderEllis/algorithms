from merge_sort import *
from bubble_sort import *
from binary_search import *
from insertion_sort import *
from heap_sort import *
from bst_sort import *
from linked_list import *
import unittest
import random

# Usage: python tests.py -v

class SortingTest(unittest.TestCase):
	
	def test_merge_sort(self):
		self.assertEqual(merge_sort([2,4,5,1,2,4]), [1,2,2,4,4,5])
		self.assertEqual(merge_sort([5,4,3,2,1]), [1,2,3,4,5])

		random_array = []
		for x in range(0, 100):
				random_array.append(random.randint(0,100))

		self.assertEqual(merge_sort(random_array), sorted(random_array))
		
	def test_bubble_sort(self):
		self.assertEqual(bubble_sort([2,4,5,1,2,4]), [1,2,2,4,4,5])

		random_array = []
		for x in range(0, 100):
			random_array.append(random.randint(0, 100))

		self.assertEqual(bubble_sort(random_array), sorted(random_array))
	
	def test_insertion_sort(self):
		self.assertEqual(insertion_sort([2,4,5,1,2,4]), [1,2,2,4,4,5])

		random_array = []
		for x in range(0, 100):
			random_array.append(random.randint(0, 100))

		self.assertEqual(insertion_sort(random_array), sorted(random_array))
	
	def test_heap_sort(self):
		self.assertEqual(heap_sort([2,4,5,1,2,4]), [1,2,2,4,4,5])
		self.assertEqual(heap_sort([5,4,3,2,1]), [1,2,3,4,5])

		random_array = []
		for x in range(0, 100):
				random_array.append(random.randint(0,100))

		self.assertEqual(heap_sort(random_array), sorted(random_array))
		
	def test_bst_sort(self):
		self.assertEqual(bst_sort([2,4,5,1,2,4]), [1,2,2,4,4,5])
		self.assertEqual(bst_sort([5,4,3,2,1]), [1,2,3,4,5])

		random_array = []
		for x in range(0, 100):
				random_array.append(random.randint(0,100))

		self.assertEqual(bst_sort(random_array), sorted(random_array))
	
	def test_linked_list_sort(self):

		test_array = [2,5,3,1,2,4]

		test_list = Linked_List()
		for value in test_array:
			test_list.insert(value)
		test_list.sort()
		self.assertEqual(test_list.printer(), sorted(test_array))

		random_array = []
		for x in range(100):
			random_array.append(random.randint(0,100))

		test_list = Linked_List()
		for value in random_array:
			test_list.insert(value)
		test_list.sort()
		self.assertEqual(test_list.printer(), sorted(random_array))





	def test_binary_search(self):
		self.assertTrue(binary_search([1,2,3,4,5], 4))
		self.assertTrue(binary_search([1,4,5,8,9,11,15,23,44,51,52], 52))
		self.assertFalse(binary_search([1,4,5,6,11,24], 3))

if __name__ == '__main__':
	unittest.main()
