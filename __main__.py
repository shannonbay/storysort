import time

import numpy as np

from storysort.storysort import generate_run_array, is_sorted, story_sort

if __name__ == "__main__":
    # Example usage
    # input_array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    input_array = [4, 1, 7, 2, 9, 3]
    print("Starting story sort.  Unsorted:\n", input_array)
    run_array = generate_run_array(input_array)
    print("Run array:", run_array)
    sorted_array = story_sort(input_array)
    print(sorted_array)  # Output: [1, 2, 3, 4, 7, 9]
    print("Finished story sort")

    random_array = np.random.randint(low=1, high=100000, size=100000)
    print(random_array[1:50])

    pre_sorted_array = sorted(random_array)
    reverse_sorted_array = sorted(random_array, reverse=True)

    print("Finished generating data - starting story_sort")
    for array in [random_array]:  # , pre_sorted_array, reverse_sorted_array]:
        start_time = time.time()
        array_sorted = story_sort(array)
        elapsed_time = time.time() - start_time
        print("StorySort time: {:.2f} seconds".format(elapsed_time))
        assert is_sorted(array_sorted)
        print(array_sorted[1:50])

    for array in [random_array]:  # , pre_sorted_array, reverse_sorted_array]:
        start_time = time.time()
        array_sorted = sorted(array)
        elapsed_time = time.time() - start_time
        print("TimSort (Python sorted) Time for: {:.2f} seconds".format(elapsed_time))

    n = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(n)
    print(generate_run_array(n))
