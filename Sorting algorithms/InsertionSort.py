def insertionSort(array):
    """
    InsertionSort is the simplest sorting algorithm. Like BubbleSort and SelectionSort,
    its use is very limited in real-life problems. This algorithm is effective for
    sorting a small array of numbers.
    Time complexity - O(n^2)

    >>> insertionSort([1, 5, 2, 7, 10, 6, 2])
    [1, 2, 2, 5, 6, 7, 10]
    """
    for i in range(1, len(array)):
        while array[i - 1] > array[i] and i > 0:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1
    return array
