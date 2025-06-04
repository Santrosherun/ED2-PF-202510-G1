def merge_sort(arr):
    """
    The given Python code implements the merge sort algorithm to sort a given array in ascending order.
    
    :param arr: The `arr` parameter in the `merge_sort` function is the list that you want to sort using
    the merge sort algorithm. It represents the array that needs to be sorted
    :return: The `merge_sort` function sorts the input array `arr` using the merge sort algorithm and
    returns the sorted array. The `merge` function is used within the `merge_sort` function to merge two
    sorted arrays `left` and `right` into a single sorted array.
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Utilizar el ordenamiento sin importar los parámetros
def mergesort_wrapper(arr):
    return merge_sort(arr)