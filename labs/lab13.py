def segregation_sort(array, low_index, high_index):
    """ Use Recursion to sort an array """

    if low_index < high_index:
        pivot_index = split_array(array, low_index, high_index)

        segregation_sort(array, low_index, pivot_index)

        segregation_sort(array, pivot_index + 1, high_index)


def split_array(array, low_index, high_index):
    """ Using division, split the array so that new pointers can 
        be assinged to be used in the segregation sort """
    
    middle_index = (low_index + high_index) // 2
    pivot = array[middle_index]
    
    left_pointer = low_index
    right_pointer = high_index

    while True:
        while array[left_pointer] < pivot:
            left_pointer += 1

        while array[right_pointer] > pivot:
            right_pointer -= 1

        if left_pointer >= right_pointer:
            return right_pointer

        array[left_pointer], array[right_pointer] = array[right_pointer], array[left_pointer]

        left_pointer += 1
        right_pointer -= 1

def test_segergation_test_cases():
    """ This function is an automation driver to test the test cases 
        for my segergation sort. It requires no input and will run through 
        each test case to ensure the proper outcome. """

    test_inputs = [
        [8, 3, 1, 7, 0, 10, 2],  # Standard Set
        [1, 2, 3, 4, 5],         # Already Sorted
        [9, 7, 5, 3, 1],         # Reverse Order
        [4, 2, 4, 2, 4],         # Duplicates
        [],                      # Empty Array
        [5]                      # Single Element
    ]
    
    # Expected outputs
    expected_outputs = [
        [0, 1, 2, 3, 7, 8, 10],
        [1, 2, 3, 4, 5],
        [1, 3, 5, 7, 9],
        [2, 2, 4, 4, 4],
        [],
        [5]
    ]
    
    # Test names
    test_names = [
        "Standard Set",
        "Already Sorted",
        "Reverse Order",
        "Duplicates",
        "Empty Array",
        "Single Element"
    ]
    
    # Testing loop
    for index in range(len(test_inputs)):
        current_array = test_inputs[index].copy()
        expected_array = expected_outputs[index]
        current_test_name = test_names[index]
        
        # if statement to avoid index error
        if len(current_array) > 0:
            high_index = len(current_array) - 1
            segregation_sort(current_array, 0, high_index)
            
        # Results evaluation and output
        if current_array == expected_array:
            print(f"Test: {current_test_name:<16} | Status: PASS")
        else:
            print(f"Test: {current_test_name:<16} | Status: FAIL")
            print(f"    Expected: {expected_array}")
            print(f"    Actual:   {current_array}")

if __name__ == "__main__":
    test_segergation_test_cases()