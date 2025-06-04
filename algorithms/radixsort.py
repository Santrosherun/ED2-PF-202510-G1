def counting_sort(arr, exp):
    """
    The function implements counting sort algorithm to sort an array based on a specific digit position
    defined by the 'exp' parameter.
    
    :param arr: The `arr` parameter in the `counting_sort` function is the input array that you want to
    sort using the counting sort algorithm. It contains the elements to be sorted
    :param exp: The `exp` parameter in the `counting_sort` function represents the exponent value used
    to extract the digit at a particular position from the elements in the input array `arr`. This
    exponent value is used to perform the counting sort based on the digit at the specified position in
    each element of the array
    :return: The `counting_sort` function is returning the sorted array `output` based on the specified
    exponent `exp`.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in reversed(range(n)):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    return output


def radix_sort(arr):
    """
    The `radix_sort` function implements the radix sort algorithm to sort a list of integers.
    
    :param arr: The `radix_sort` function you provided is an implementation of the radix sort algorithm
    in Python. It sorts a list of integers by processing individual digits. The function first finds the
    maximum number in the list to determine the number of digits in the largest number. It then performs
    counting sort on each digit
    :return: The `radix_sort` function is returning the sorted `arr` using the radix sort algorithm.
    """
    if not arr:
        return []

    max_num = max(arr)
    exp = 1
    output = arr.copy()

    while max_num // exp > 0:
        output = counting_sort(output, exp)
        exp *= 10

    return output


# Utilizar el ordenamiento sin importar los parámetros
def radixsort_wrapper(arr):
    return radix_sort(arr)