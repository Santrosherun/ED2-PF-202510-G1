def generate_3smooth_gaps(n):
    """
    The function generates and returns the 5 largest 3-smooth numbers less than a given input number.
    
    :param n: The function `generate_3smooth_gaps(n)` generates a set of numbers that are powers of 3 up
    to a certain limit `n`, and then returns the largest 5 numbers from that set in descending order
    :return: The function `generate_3smooth_gaps(n)` returns a list of the 5 largest gaps that are
    multiples of powers of 2 and 3, up to the input value `n`.
    """
    gaps = set()
    p = 1
    while p < n:
        q = p
        while q < n:
            gaps.add(q)
            q *= 3
        p *= 2
    return sorted(gaps, reverse=True)[:5]

def shellsort(arr):
    n = len(arr)
    gaps = generate_3smooth_gaps(n)
    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
    return arr

def shellsort_wrapper(arr):
    return shellsort(arr[:]) 