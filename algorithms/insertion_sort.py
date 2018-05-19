"""
Script that shows how to sort a list with insertion sort
@author: German Om


INSERTION SORT
Suppose that we have a sorted array, A, and a single element outside of it, x. The natural question is, how can we place
this element into our array while still keeping it sorted?

This operation is known as an insertion, and there are multiple ways to do it.

-   Place x at the end of A.
-   Compare x to the element on its left. There are three possibilities.
    -   If there is no element to the left, then we are done, since x will be the smallest element and it is already at the
        start of the array.
    -   If x is greater than or equal to it, then we are done; x is ahead of all smaller elements and behind all larger
        elements, so the array is once again sorted.
    -   If x is smaller, then it should be before the other element. Switch the two to put x on front.
-   Repeat step two until finished.

With each repetition of step two, we will either finish inserting, or reduce the number of elements ahead of x by one.
Since we are also finished when no more elements remain in front of x, repeating step two is guaranteed to successfully
make an insertion.

"""


def insertion_sort(input_list, x):
    """

    :param input_array:
    :param x:
    :return:
    """
    sorted_list = input_list
    sorted_list.append(x)
    return sorted_list


if __name__ == '__main__':
    pass