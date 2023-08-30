from storysort.storysort import fib, generate_run_array, is_sorted, story_sort


def test_fib() -> None:
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(10) == 55


def test_is_sorted() -> None:
    assert not is_sorted([4, 1, 7, 2, 9, 3])
    assert is_sorted([1, 2, 2, 3, 4, 7, 7, 9])


def test_story_sort() -> None:
    res = story_sort([1, 2, 9, 2, 3, 1])
    assert res == [1, 1, 2, 2, 3, 9]
    assert is_sorted(res)

    res = story_sort([4, 1, 7, 2, 9, 3, 5, 2, 3])
    assert is_sorted(res)

    res = story_sort([1, 2, 9, 2, 3, 1])
    assert is_sorted(res)


def test_generate_run_array() -> None:
    run_array, run_start_idx = generate_run_array([4, 1, 7, 2, 9, 3, 5, 2, 3])
    assert run_array == [2, 0, 4, 5, -1, 6, -1, 3, -1]
    assert run_start_idx == [1, 7, 8]

    run_array, run_start_idx = generate_run_array([1, 2, 9, 2, 3, 1])
    assert run_array == [1, 2, -1, 4, -1, 0]
    assert run_start_idx == [5, 3]
