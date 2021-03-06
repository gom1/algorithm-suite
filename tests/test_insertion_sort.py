import unittest
import algorithms.insertion_sort as ais


class TestInsertionSort(unittest.TestCase):
    def test_empty_list(self):
        initial_list = []
        x = 0
        expected_list = [0]
        result = ais.insertion_sort(initial_list, x)
        self.assertEqual(expected_list, result)

    def test_positive_integers_list(self):
        initial_list = [1, 2, 4]
        x = 3
        expected_list = [1, 2, 3, 4]
        result = ais.insertion_sort(initial_list, x)
        self.assertEqual(expected_list, result)

    def test_negative_integers_list(self):
        initial_list = [-3, 2, 8]
        x = -1
        expected_list = [-3, -1, 2, 8]
        result = ais.insertion_sort(initial_list, x)
        self.assertEqual(expected_list, result)

    def test_edge_case_end_of_list(self):
        initial_list = [1, 2, 3, 4, 5]
        x = 6
        expected_list = [1, 2, 3, 4, 5, 6]
        result = ais.insertion_sort(initial_list, x)
        self.assertEqual(expected_list, result)

    def test_edge_case_beginning_of_list(self):
        initial_list = [1, 2, 3, 4, 5]
        x = 0
        expected_list = [0, 1, 2, 3, 4, 5]
        result = ais.insertion_sort(initial_list, x)
        self.assertEqual(expected_list, result)

    def test_edge_case_number_exists_in_list(self):
        initial_list = [1, 2, 3, 4, 5]
        x = 4
        expected_list = [1, 2, 3, 4, 4, 5]
        result = ais.insertion_sort(initial_list, x)
        self.assertEqual(expected_list, result)


class TestSortWithInsertionSort(unittest.TestCase):
    def test_empty_list(self):
        initial_list = []
        expected_list = []
        result = ais.sort_with_insertion_sort(initial_list)
        self.assertEqual(expected_list, result)

    def test_already_sorted_list(self):
        initial_list = [1, 2, 3]
        expected_list = [1, 2, 3]
        result = ais.sort_with_insertion_sort(initial_list)
        self.assertEqual(expected_list, result)

    def test_mixed_integers_list(self):
        initial_list = [1, 5, 2]
        expected_list = [1, 2, 5]
        result = ais.sort_with_insertion_sort(initial_list)
        self.assertEqual(expected_list, result)

    def test_edge_case_sort_whole_list(self):
        initial_list = [4, 3, 2, 1]
        expected_list = [1, 2, 3, 4]
        result = ais.sort_with_insertion_sort(initial_list)
        self.assertEqual(expected_list, result)

    def test_edge_case_duplicate_integers_in_list(self):
        initial_list = [8, 2, 5, 3, 4, 5]
        expected_list = [2, 3, 4, 5, 5, 8]
        result = ais.sort_with_insertion_sort(initial_list)
        self.assertEqual(expected_list, result)


class TestSortWithInsertionSortInPlace(unittest.TestCase):
    def test_empty_list(self):
        initial_list = []
        expected_list = []
        result = ais.sort_with_insertion_sort_in_place(initial_list)
        self.assertEqual(expected_list, result)

    def test_already_sorted_list(self):
        initial_list = [1, 2, 3]
        expected_list = [1, 2, 3]
        result = ais.sort_with_insertion_sort_in_place(initial_list)
        self.assertEqual(expected_list, result)

    def test_mixed_integers_list(self):
        initial_list = [1, 5, 2]
        expected_list = [1, 2, 5]
        result = ais.sort_with_insertion_sort_in_place(initial_list)
        self.assertEqual(expected_list, result)

    def test_edge_case_sort_whole_list(self):
        initial_list = [4, 3, 2, 1]
        expected_list = [1, 2, 3, 4]
        result = ais.sort_with_insertion_sort_in_place(initial_list)
        self.assertEqual(expected_list, result)

    def test_edge_case_duplicate_integers_in_list(self):
        initial_list = [8, 2, 5, 3, 4, 5]
        expected_list = [2, 3, 4, 5, 5, 8]
        result = ais.sort_with_insertion_sort_in_place(initial_list)
        self.assertEqual(expected_list, result)

if __name__ == '__main__':
    unittest.main()
