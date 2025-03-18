The implementation uses binary search to efficiently find the square root of a number.

Time Complexity: O(log n) - The binary search algorithm divides the search space in half with each iteration, resulting in logarithmic time complexity.

Space Complexity: O(1) - The algorithm uses a constant amount of extra space regardless of the input size, as it only needs a few variables (lo, hi, mid, res) to track the search space and result.

This is much more efficient than a linear approach (which would be O(√n)) because binary search allows you to quickly narrow down the possible values for the square root.
