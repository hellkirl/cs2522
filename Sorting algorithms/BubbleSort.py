def bubbleSort(array):
    """
    >>> bubbleSort([1, 3, 1, 2, 3])
    [1, 1, 2, 3, 3]
    """
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
