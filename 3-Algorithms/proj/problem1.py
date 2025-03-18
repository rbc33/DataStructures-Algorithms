def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0:
        return 0
# Initial search space
    lo = 1
    hi = number
    res = 1
    
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        
        # If square of mid is less than or equal to number 
        # update the result and search in upper half
        if mid * mid <= number:
            res = mid
            lo = mid + 1
            
        # If square of mid exceeds number, 
        # search in the lower half
        else:
            hi = mid - 1
    
    return res


print("Pass" if 3 == sqrt(9) else "Fail")
print("Pass" if 0 == sqrt(0) else "Fail")
print("Pass" if 4 == sqrt(16) else "Fail")
print("Pass" if 1 == sqrt(1) else "Fail")
print("Pass" if 5 == sqrt(27) else "Fail")