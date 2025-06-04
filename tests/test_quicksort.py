from algorithms.quicksort import quicksort_wrapper

def test_quicksort_basic():
    """
    The above code snippet contains test cases for a quicksort function.
    """
    assert quicksort_wrapper([3, 1, 2]) == [1, 2, 3]

def test_quicksort_empty():
    assert quicksort_wrapper([]) == []

def test_quicksort_sorted():
    assert quicksort_wrapper([1, 2, 3]) == [1, 2, 3]