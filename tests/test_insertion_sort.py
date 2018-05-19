import unittest
from algorithms.insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    def test_empty_list(self):
        initial_list = []
        x = 0
        expected_list = [0]
        result = insertion_sort(initial_list, x)
        self.assertEqual(expected_list, result)

    def test_positive_integers_list(self):
        initial_list = [1, 2, 4]
        x = 3
        expected_list = [1, 2, 3, 4]
        result = insertion_sort(initial_list, x)
        self.assertEqual(expected_list, result)

    def test_negative_integers_list(self):
        initial_list = [-3, 2, 8]
        x = -1
        expected_list = [-3, -1, 2, 8]
        result = insertion_sort(initial_list, x)
        self.assertEqual(expected_list, result)

    def test_edge_case_end_of_list(self):
        initial_list = [1, 2, 3, 4, 5]
        x = 6
        expected_list = [1, 2, 3, 4, 5, 6]
        result = insertion_sort(initial_list, x)
        self.assertEqual(expected_list, result)

    def test_edge_case_beginning_of_list(self):
        initial_list = [1, 2, 3, 4, 5]
        x = 0
        expected_list = [0, 1, 2, 3, 4, 5]
        result = insertion_sort(initial_list, x)
        self.assertEqual(expected_list, result)

    def test_edge_case_number_exists_in_list(self):
        initial_list = [1, 2, 3, 4, 5]
        x = 4
        expected_list = [1, 2, 3, 4, 4, 5]
        result = insertion_sort(initial_list, x)
        self.assertEqual(expected_list, result)


if __name__ == '__main__':
    unittest.main()
