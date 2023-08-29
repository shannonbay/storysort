from storysort.storysort import generate_run_array, story_sort

if __name__ == "__main__":
    # Example usage
    input_array = [4, 1, 7, 2, 9, 3]
    print("Starting story sort.  Unsorted:\n", input_array)
    sorted_array = story_sort(input_array)
    print(sorted_array)  # Output: [1, 2, 3, 4, 7, 9]
    print("Finished story sort")

    n = [7, 8, 9, 3, 4, 10, 6]
    print(n)
    print(generate_run_array(n))
