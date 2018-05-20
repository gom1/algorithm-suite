"""
Functions to help explain how to sort a list with the insertion sort algorithm
@author: German Om

"""


def insertion(input_list, x):
    """
    Performs insertion sort and returns the new sorted array with x added to the list.
    :param input_list: sorted list of integers
    :param x: integer that will be added to the input_list
    :return sorted_list: sorted list with x properly sorted in it
    """
    sorted_list = input_list
    sorted_list.append(x)
    for i in reversed(xrange(1, len(input_list))):
        if sorted_list[i - 1] <= sorted_list[i]:
            # order is sorted, so we can exit the loop
            break
        else:
            # swapping values in-place
            sorted_list[i], sorted_list[i - 1] = sorted_list[i - 1], sorted_list [i]
    return sorted_list


def sort_with_insertion(input_list):
    """
    Performs full insertion sort of any integer list and returns a sorted list
    :param input_list: integer list (sorted or not)
    :return: sorted list
    """
    sorted_array = []
    for i in input_list:
        sorted_array = insertion(sorted_array, i)
    return sorted_array


def insertion_sort(input_list):
    """
    Takes in a list of unsorted integers and performs insertion sort (in-place sorting) to return a sorted list
    :param input_list:
    :return:
    """
    for i in xrange(1, len(input_list)):
        for j in xrange(i, 0, -1):
            if input_list[j - 1] < input_list[j]:
                # order is sorted, so we can exit the loop!
                break
            else:
                # swapping values in-place
                input_list[j], input_list[j - 1] = input_list[j - 1], input_list[j]
    return input_list
