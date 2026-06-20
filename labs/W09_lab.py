# 1. Name:
#      Connor Sanderson
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      This is designed to sort through a list using two sub lists. It will go through 
#      the list until it finds a number that is not in order and then sort the two sublists 
#      before begining the process again
# 4. What was the hardest part? Be as specific as possible.
#      I would say over all this assignment went well. It just took me a little bit to 
#      get the driver working becuase I accidentily forgot to unindent something.
# 5. How long did it take for you to complete the assignment?
#      1hr 30min

def sort_array(array):
    """sort the array"""
    size = len(array)

    if size <= 1:
        return array
    
    source = array
    destination = [0] * size
    num = 2

    while num > 1:
        num = 0
        begin1 = 0

        while begin1 < size:
            end1 = begin1 + 1

            while (end1 < size) and (source[end1 - 1] <= source[end1]):
                end1 += 1
            
            begin2 = end1
            if begin2 < size:
                end2 = begin2 + 1
            else:
                end2 = begin2
            
            while (end2 < size) and (source[end2 - 1] <= source[end2]):
                end2 += 1
            
            num += 1
            combine_lists(source, destination, begin1, begin2, end2)
            begin1 = end2
        
        source, destination = destination, source

    return source

def combine_lists(source, destination, begin1, begin2, end2):
    """Combine the two lists"""
    end1 = begin2

    i_begin1 = begin1
    i_begin2 = begin2

    for i in range(begin1, end2):
        if (i_begin1 < end1) and (i_begin2 == end2 or source[i_begin1] <= source[i_begin2]):
            destination[i] = source[i_begin1]
            i_begin1 += 1
        else:
            destination[i] = source[i_begin2]
            i_begin2 += 1
    
    return destination


def test_sort():
    # --- Test Cases Inputs ---
    tc1_input = []
    tc2_input = [42]
    tc3_input = [10, 20, 30, 40, 50]
    tc4_input = [5, 4, 3, 2, 1]
    tc5_input = [3, 7, 2, 8, 5, 9, 1, 4]
    tc6_input = [4, 2, 4, 3, 2, 1]
    tc7_input = [3, -1, 0, -5, 2]

    # --- Test Cases Outputs ---
    tc1_output = []
    tc2_output = [42]
    tc3_output = [10, 20, 30, 40, 50]
    tc4_output = [1, 2, 3, 4, 5]
    tc5_output = [1, 2, 3, 4, 5, 7, 8, 9]
    tc6_output = [1, 2, 2, 3, 4, 4]
    tc7_output = [-5, -1, 0, 2, 3]

    # nputs and expected outputs
    inputs = [
        tc1_input, tc2_input, tc3_input, tc4_input, 
        tc5_input, tc6_input, tc7_input
    ]
    
    expected_outputs = [
        tc1_output, tc2_output, tc3_output, tc4_output, 
        tc5_output, tc6_output, tc7_output
    ]

    passed_count = 0
    total_tests = len(inputs)

    # --- tests ---
    print("==========================================")
    print("testing the sorting...")
    print("==========================================")

    for i in range(total_tests):
        current_input = inputs[i]
        current_expected = expected_outputs[i]

        # Execute the function under test
        actual_output = sort_array(current_input)

        print(f"Test Case: {i + 1}")
        print(f"Input:    {current_input}")
        print(f"Expected: {current_expected}")
        print(f"Actual:   {actual_output}")

        # Evaluate correctness
        if actual_output == current_expected:
            print("Status: Passed")
            passed_count += 1
        else:  # [cite: 191]
            print("Status: Failed")
        
        print()

    print("==========================================")
    print(f"Testing summary: {passed_count} / {total_tests} Tests Passed")
    

def main():
    test_sort()

main()