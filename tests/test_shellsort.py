from algorithms.shellsort import shellsort_wrapper

def test_shellsort_basic():
    """
    The above code defines two test functions for a shell sort algorithm.
    """
    assert shellsort_wrapper([9, 7, 5, 3]) == [3, 5, 7, 9]

def test_shellsort_single_element():
    assert shellsort_wrapper([1]) == [1]