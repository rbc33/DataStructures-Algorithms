# %%
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    current = llist_1.head
    while current.next:
        current = current.next
    current.next = llist_2.head
    return current
    

def intersection(llist_1, llist_2):
    # Your Solution Here
    intersection = []
    current1 = llist_1.head
    while current1:
        current2 = llist_2.head 
        while current2:
            if current1.value==current2.value:
                intersection.append(current1.value) 
            current2 = current2.next
        current1 = current1.next
    return intersection


## Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
print(intersection(linked_list_1, linked_list_2))

## Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
print(intersection(linked_list_3, linked_list_4))

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1

## Test Case 2

## Test Case 3

# %%
print("\n## Test Case 1: One empty list")
empty_list = LinkedList()
normal_list = LinkedList()

for i in [1, 2, 3, 4, 5]:
    normal_list.append(i)

print("Union with empty list:")
try:
    print(union(empty_list, normal_list))
except AttributeError:
    print("Error: Cannot perform union with empty list")

print("Intersection with empty list:")
result = intersection(empty_list, normal_list)
print(f"Result: {result}")
print(f"Length: {len(result)}")

# %%
## Test Case 2: Lists with duplicate values
print("\n## Test Case 2: Lists with duplicate values")
duplicate_list1 = LinkedList()
duplicate_list2 = LinkedList()

for i in [1, 1, 2, 2, 3, 3]:
    duplicate_list1.append(i)

for i in [2, 2, 3, 3, 4, 4]:
    duplicate_list2.append(i)

print("Intersection with duplicates:")
result = intersection(duplicate_list1, duplicate_list2)
print(f"Result: {result}")
print(f"Expected unique values: [2, 3]")
print(f"Actual count: 2's: {result.count(2)}, 3's: {result.count(3)}")

# %%
## Test Case 3: Very large lists
print("\n## Test Case 3: Very large lists")
large_list1 = LinkedList()
large_list2 = LinkedList()

# Create lists with 1000 elements each
for i in range(1000):
    large_list1.append(i)
    
for i in range(500, 1500):  # Overlap from 500-999
    large_list2.append(i)

# Test intersection performance
import time
start_time = time.time()
result = intersection(large_list1, large_list2)
end_time = time.time()

print(f"Intersection of large lists:")
print(f"Number of common elements: {len(result)}")
print(f"First few elements: {result[:5]}...")
print(f"Time taken: {end_time - start_time:.4f} seconds")


