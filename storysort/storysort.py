def fib(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def story_sort(arr):
    # Use Python's built-in sorted() function to sort the array
    sorted_arr = sorted(arr)
    return sorted_arr


def is_sorted(arr):
    # Check if each element is less than or equal to the next element
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
