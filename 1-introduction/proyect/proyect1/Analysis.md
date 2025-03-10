## Task0

**Description**: The task involves accessing first and last elements from texts and calls lists using direct index access.

**Approach**: Using direct index notation with [0] and [-1] to access the required elements.

**Complexity Analysis**:
- **Algorithm**: Single operation using direct array indexing.
- **Big O Notation**: $O(1)$
- **Justification**: Array index access operations are constant time regardless of input size.

## Task1

**Description**: Finding unique telephone numbers by checking and appending to a list.

**Approach**: Using list operations with 'not in' checks before appending new numbers.

**Complexity Analysis**:
- **Algorithm**: Nested operations with list searching and appending.
- **Big O Notation**: $O(n²)$
- **Justification**: For each number, we perform a linear search through the list before appending.

## Task2

**Description**: Tracking call durations using dictionary and finding the maximum.

**Approach**: Using dictionary to accumulate call times and iterating to find maximum.

**Complexity Analysis**:
- **Algorithm**: Single pass through calls with dictionary operations.
- **Big O Notation**: $O(n)$
- **Justification**: Each call is processed once with constant time dictionary operations.

## Task3

**Description**: Processing Bangalore calls using list operations and regex matching.

**Approach**: Using list operations with 'not in' checks and regex pattern matching.

**Complexity Analysis**:
- **Algorithm**: Multiple passes through data with list searches and final sorting.
- **Big O Notation**: $O(n²)$
- **Justification**: List membership testing is linear time, performed for each element, plus sorting.

## Task4

**Description**: Identifying telemarketers using multiple list comparisons.

**Approach**: Using multiple lists with membership testing and appending operations.

**Complexity Analysis**:
- **Algorithm**: Multiple iterations with list membership testing.
- **Big O Notation**: $O(n²)$
- **Justification**: Each 'not in' operation requires a linear search through the list, performed for each element.
