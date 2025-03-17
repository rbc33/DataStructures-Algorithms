# Active Directory Group Membership Algorithm

This implementation provides a recursive solution for checking if a user is a member of a group in an Active Directory-like structure, where groups can contain both users and other groups.

The solution uses:

- A `Group` class that maintains lists of users and subgroups
- A recursive traversal algorithm to check membership at any level of nesting

The algorithm works by:

1. Checking if the user is directly in the current group's user list
2. If not found, recursively checking each subgroup
3. Returning True as soon as the user is found in any group or subgroup
4. Returning False only after exhausting all possible paths

The time complexity is O(n) where n is the total number of users and groups in the system, with space complexity of O(d) where d is the maximum depth of group nesting due to the recursive call stack.

This implementation handles edge cases such as empty groups and deeply nested group structures, providing an efficient way to determine user membership in complex organizational hierarchies.
