# 1. Name:
#      Connor Sanderson
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      This is designed to sort through a list using two sub lists. It will go through 
#      the list until it finds a number that is not in order and then sort the two sublists 
#      before begining the process again
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

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
            i_begin2 += 1
    
    return destination

def read(array):
    pass


def main():
    print('hello world')

main()