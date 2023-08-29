import bisect


def fib(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def story_sort(arr):
    run_array, run_start_idx = generate_run_array(arr)

    result = []
    # merge runs - could be optimised by maintaining a min heap
    # 1. Get all the run_start_idx's and pop the one with the lowest value. append that values run_array value (unless 0?)
    # 2. Repeat step 1 until run_start_idx is empty?
    while run_start_idx:
        min_value = arr[run_start_idx[0]]
        min_idx = 0
        # Loop through the rest of the indexes in run_start_idx
        for i in range(1, len(run_start_idx)):
            # Get the current index
            index = run_start_idx[i]
            # Get the current element of arr at that index
            value = arr[index]
            # Compare it with the current min_value and update it if it is smaller
            if value < min_value:
                min_value = value
                min_idx = i
        # update the run_start_idx for the new min_value
        index = run_start_idx.pop(min_idx)
        if run_array[index] > -1:
            run_start_idx.append(run_array[index])

        # Return the min_value as the final answer
        result.append(min_value)

    return result


def key_function(x):
    return -x


def generate_run_array(input_array):
    run_array = [-1] * len(
        input_array
    )  # non-consecutive series of indexes over input_array - Initialize the run_array with 0
    run_maxes = [
        input_array[0]
    ]  # Keeps track of the current value for each run - maintained in order from lowest to highest
    run_mins = [input_array[0]]
    run_indexes = [0]  # Keeps track of the current index for each run
    run_start_idx = [0]

    # For each input value
    for i, value in enumerate(input_array[1:], start=1):
        found = False

        # For each established run
        j = bisect.bisect_left(run_maxes, key_function(value), key=key_function)

        if j != len(run_maxes):
            run_maxes[j] = value  # update the max for run j
            run_array[run_indexes[j]] = i  # run array for run j now points to i
            run_indexes[j] = i  # i is now the latest index in run j
            found = True

        if not found:
            j = bisect.bisect_left(run_mins, value)
            # For each established run
            if j != len(
                run_mins
            ):  # find the first run (j) that current value is greater than (or equal to)
                run_mins[j] = value  # update the min for run j
                run_array[i] = run_start_idx[j]  # point to the old start
                run_start_idx[j] = i  # this is the new start idx for the run
                found = True

        if not found:
            run_maxes.append(value)  # start a new run
            run_mins.append(value)
            run_indexes.append(i)  # i is now the latest index in run j
            run_start_idx.append(i)

    return run_array, run_start_idx


def is_sorted(arr):
    # Check if each element is less than or equal to the next element
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
