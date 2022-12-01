def selectionSort(array):
    """
    SelectionSort is one of the easiest to implement sorting algorithms.
    However, it is not an as affective as more complex algortihms.
    A minimum element in an array is found and put into en empty list while
    the initial array is emptied, using while-loop.
    This algorithm is effective for sorting a small array of numbers.
    Time complexity - O(n^2)

    >>> selectionSort([1, 5, 2, 67, 83, 55, 9235, 235,96996, 1, 5, 5])
    [1, 1, 2, 5, 5, 5, 55, 67, 83, 235, 9235, 96996]
    >>> selectionSort([1, 2, 5, 6, 7])
    [1, 2, 5, 6, 7]
    >>> selectionSort([0, 13523, 35, 134, 153, 5, 235, 5, 5, 2, 53, 52, 5,135])
    [0, 2, 5, 5, 5, 5, 35, 52, 53, 134, 135, 153, 235, 13523]
    """
    sorted_list = []
    while len(array) != 0:
        sorted_list.append(min(array))
        array.remove(min(array))
    return sorted_list
