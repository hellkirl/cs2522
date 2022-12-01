def mergeSort(array):
    """
    MergeSort is much more effective than all the elementary algorithms.
    Still, it is not as wide-spread as QuickSort and HeapSort.
    Time complexity - O(n * Log n)

    >>> mergeSort([1, 5, 3, 7, 1, 8, 4, 8, 9, 1, 5])
    [1, 1, 1, 3, 4, 5, 5, 7, 8, 8, 9]
    """
    if len(array) == 1:
        return array
    middle_index = len(array)//2
    left_part = mergeSort(array[:middle_index])
    right_part = mergeSort(array[middle_index:])
    return merge_two_lists(left_part, right_part)


def merge_two_lists(left, right):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    if i < len(left):
        sorted_list += left[i:]
    if j < len(right):
        sorted_list += right[j:]

    return sorted_list
