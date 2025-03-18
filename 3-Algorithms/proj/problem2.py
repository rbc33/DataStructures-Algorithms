def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """        
    start = 0
    end = len(input_list) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        # Si encontramos el elemento
        if input_list[mid] == number:
            return mid
            
        # Si la mitad izquierda está ordenada
        if input_list[start] <= input_list[mid]:
            # Si el elemento está en la mitad izquierda ordenada
            if input_list[start] <= number < input_list[mid]:
                end = mid - 1
            else:
                start = mid + 1
        # Si la mitad derecha está ordenada
        else:
            # Si el elemento está en la mitad derecha ordenada
            if input_list[mid] < number <= input_list[end]:
                start = mid + 1
            else:
                end = mid - 1
                
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1
    
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")
        
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
