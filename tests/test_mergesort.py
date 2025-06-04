from algorithms.mergesort import mergesort_wrapper

def test_mergesort_basic():
    """
    The above code snippet contains test cases for a mergesort function with various input scenarios.
    """
    assert mergesort_wrapper([9, 7, 5, 3]) == [3, 5, 7, 9]

def test_mergesort_single_element():
    assert mergesort_wrapper([1]) == [1]

def test_mergesort_empty():
    assert mergesort_wrapper([]) == []

def test_mergesort_duplicates():
    assert mergesort_wrapper([4, 5, 4, 3]) == [3, 4, 4, 5]

def test_mergesort_negative_numbers():
    assert mergesort_wrapper([-2, 3, -1, 0]) == [-2, -1, 0, 3]