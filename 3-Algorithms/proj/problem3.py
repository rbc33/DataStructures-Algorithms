def heapify(arr, n, i):
    """
    :param: arr - array to heapify
    n -- number of elements in the array
    i -- index of the current node
    TODO: Converts an array (in place) into a maxheap, a complete binary tree with the largest values at the top
    """
    largest_index = i
    left_node = 2 * i + 1
    right_node = 2 * i + 2

    if left_node < n and arr[i] < arr[left_node]:
        largest_index = left_node

    if right_node < n and arr[largest_index] < arr[right_node]:
        largest_index = right_node

    if largest_index != i:
        arr[i], arr[largest_index] = arr[largest_index], arr[i]
    
        heapify(arr, n, largest_index)
    
def heapsort(arr):
    n = len(arr)
    heapify(arr, n, 0)

    for i in range(n, -1, -1):
        heapify(arr, n ,i)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i ,0)


def rearrange_digits(input_list):
    """
    Rearranges the elements of the given array to form two numbers such that their sum is maximized.
    The numbers formed have a number of digits differing by no more than one.
    
    Args:
        input_list (List[int]): A list of integers

    Returns:
        Tuple[int, int]: A tuple containing two integers
    """
    heapsort(input_list)
    print(input_list)
    list1 = input_list[::2]
    list2 = input_list[1::2]
    print(list1)
    print(list2)
    res = [0,0]
    for i,v in enumerate(list1):
        res[0] += v * 10**i 
    for i,v in enumerate(list2):
        res[1] += v * 10**i 
    print(res)
    return res

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]