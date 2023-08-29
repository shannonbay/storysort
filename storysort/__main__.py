import sys

from storysort.storysort import fib, story_sort

if __name__ == "__main__":
    # Example usage
    input_array = [4, 1, 7, 2, 9, 3]
    sorted_array = story_sort(input_array)
    print(sorted_array)  # Output: [1, 2, 3, 4, 7, 9]

    n = int(sys.argv[1])
    print(fib(n))
