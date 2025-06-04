def quicksort(data, low, high):
    """
    The code implements the quicksort algorithm in Python with a wrapper function for ease of use.
    
    :param data: The `data` parameter in the `quicksort` function represents the list of elements that
    you want to sort using the quicksort algorithm. It is the input array that will be sorted in
    ascending order
    :param low: The `low` parameter in the `quicksort` function represents the lowest index of the
    subarray being sorted. It is used to keep track of the starting point of the subarray within the
    overall array being sorted
    :param high: The `high` parameter in the `quicksort` function represents the index of the last
    element in the sublist of the array being sorted. It indicates the upper bound of the sublist within
    which the sorting algorithm should operate
    """
    if low < high:
        i = low
        j = high
        p = data[(low + high) // 2]
        
        while i <= j:
            while data[i] < p:
                i += 1
            while data[j] > p:
                j -= 1
            if i <= j:
                swap(data, i, j)
                i += 1
                j -= 1

        quicksort(data, low, j)
        quicksort(data, i, high)

# Utilizar el ordenamiento sin importar los parámetros
def quicksort_wrapper(arr): 
    data = arr[:]  # Crea una copia para no modificar la lista original
    quicksort(data, 0, len(data) - 1)
    return data

def swap(data, i, j):
    """
    The `swap` function in Python swaps the elements at two specified indices in a given list.
    
    :param data: The `data` parameter is a list or array that contains the elements to be swapped
    :param i: The parameter `i` in the `swap` function represents the index of the first element that
    you want to swap in the `data` list
    :param j: The parameter `j` in the `swap` function represents the index of the element in the `data`
    list that you want to swap with the element at index `i`
    """
    data[i], data[j] = data[j], data[i]