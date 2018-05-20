import unittest
from algorithms.insertion_sort import insertion_sort as ais


class TestInsertionSort(unittest.TestCase):
    def test_empty_list(self):
        initial_list = []
        expected_list = []
        result = ais.insertion_sort(initial_list)
        self.assertEqual(expected_list, result)

    def test_already_sorted_list(self):
        initial_list = [1, 2, 3]
        expected_list = [1, 2, 3]
        result = ais.insertion_sort(initial_list)
        self.assertEqual(expected_list, result)

    def test_mixed_integers_list(self):
        initial_list = [1, 5, 2]
        expected_list = [1, 2, 5]
        result = ais.insertion_sort(initial_list)
        self.assertEqual(expected_list, result)

    def test_edge_case_sort_whole_list(self):
        initial_list = [4, 3, 2, 1]
        expected_list = [1, 2, 3, 4]
        result = ais.insertion_sort(initial_list)
        self.assertEqual(expected_list, result)

    def test_edge_case_duplicate_integers_in_list(self):
        initial_list = [8, 2, 5, 3, 4, 5]
        expected_list = [2, 3, 4, 5, 5, 8]
        result = ais.insertion_sort(initial_list)
        self.assertEqual(expected_list, result)


if __name__ == '__main__':
    unittest.main()
