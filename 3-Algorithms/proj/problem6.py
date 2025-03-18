def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    
    Args:
       ints(list): list of integers containing one or more integers
    """
    min_num = ints[0]
    max_num = ints[0]
    i = 1
    while i <= len(ints)-1:
        if ints[i]< min_num:
            min_num = ints[i]
        if ints[i] > max_num:
            max_num = ints[i]
        i += 1
    return min_num, max_num

### Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")