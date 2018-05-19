import unittest
from algorithms.insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    def test_empty_list(self):
        initial_array = []
        expected_array = [0]
        result = insertion_sort(initial_array, 0)
        self.assertTrue(expected_array, result)


if __name__ == '__main__':
    unittest.main()