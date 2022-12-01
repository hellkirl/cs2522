def bubbleSort(array):
    """
    BubbleSort is a popular but ineffective sorting algorithm.
    The biggest element of a list pops like a bubble at the end of a list.
    This algorithm is effective for sorting a small array of numbers.
    Time complexity - O(n^2)

    >>> bubbleSort([1, 3, 1, 2, 3])
    [1, 1, 2, 3, 3]
    """
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
