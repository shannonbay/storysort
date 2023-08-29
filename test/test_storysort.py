from storysort.storysort import fib, generate_run_array, is_sorted, story_sort


def test_fib() -> None:
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(10) == 55


def test_story_sort() -> None:
    assert is_sorted(story_sort([4, 1, 7, 2, 9, 3]))
    assert not is_sorted([4, 1, 7, 2, 9, 3])


def test_generate_run_array() -> None:
    print(generate_run_array([4, 1, 7, 2, 9, 3]))
