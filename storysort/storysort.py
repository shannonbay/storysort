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
        if run_array[index] > 0:
            run_start_idx.append(run_array[index])

        # Return the min_value as the final answer
        result.append(min_value)

    return result


def generate_run_array(input_array):
    run_array = [0] * len(
        input_array
    )  # indexes over input_array - Initialize the run_array with 0
    run_maxes = [
        input_array[0]
    ]  # Keeps track of the current value for each run - maintained in order from highest to lowest
    run_indexes = [0]  # Keeps track of the current index for each run
    run_start_idx = [0]

    # For each input value
    for i, value in enumerate(input_array[1:], start=1):
        found = False

        # For each established run
        for j in range(
            len(run_maxes)
        ):  # this loop can be replaced with a binary search since run_maxes is ordered
            if (
                value >= run_maxes[j]
            ):  # find the first run (j) that current value is greater than (or equal to)
                run_maxes[j] = value  # update the max for run j
                run_array[run_indexes[j]] = i  # run array for run j now points to i
                run_indexes[j] = i  # i is now the latest index in run j
                found = True
                break

        if not found:
            # handle case where value is less than existing run maxes
            run_maxes.append(value)  # start a new run
            run_indexes.append(i)  # i is now the latest index in run j
            run_start_idx.append(i)

    print("Number of runs: ", len(run_indexes))
    return run_array, run_start_idx


def is_sorted(arr):
    # Check if each element is less than or equal to the next element
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
