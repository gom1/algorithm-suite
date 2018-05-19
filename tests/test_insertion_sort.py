import unittest
from algorithms.insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    def test_empty_list(self):
        initial_list = []
        expected_list = [0]
        result = insertion_sort(initial_list, 0)
        self.assertEqual(expected_list, result)


if __name__ == '__main__':
    unittest.main()
