# %%
from collections import deque
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = {}  
        self.order = deque()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if self.capacity == 0:
            return -1  # Changed from None to -1 for consistency
        if key in self.cache:
            # Update access order
            self.order.remove(key)
            self.order.appendleft(key)
            return self.cache[key]
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.capacity == 0:
            return
            
        if key in self.cache:
            # Update existing key
            self.cache[key] = value
            self.order.remove(key)
            self.order.appendleft(key)
        else:
            # Add new key
            if len(self.cache) >= self.capacity:
                # Remove least recently used item
                old_key = self.order.pop()
                del self.cache[old_key]
            
            # Add new item
            self.cache[key] = value
            self.order.appendleft(key)

# %%
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print("Should return: 1 -> ", our_cache.get(1))       # returns 1
print("Should return: 2 -> ", our_cache.get(2))       # returns 2
print("Should return: -1 -> ", our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print("Should return: -1 -> ", our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# %%
def test_function(test_case):
    cache = test_case[0]
    operations = test_case[1]
    expected = test_case[2]
    
    results = []
    
    for op in operations:
        if op[0] == "get":
            results.append(cache.get(op[1]))
        elif op[0] == "set":
            cache.set(op[1], op[2])
    
    if results == expected:
        print("Pass")
    else:
        print("Fail")

# %%
cache1 = LRU_Cache(5)
operations1 = [
    ["set", 1, 1],
    ["set", 2, 2],
    ["get", 1],
    ["get", 2],
    ["get", 3]
]
expected1 = [1, 2, -1]
test_case1 = [cache1, operations1, expected1]
test_function(test_case1)

# %%
cache2 = LRU_Cache(2)
operations2 = [
    ["set", 1, 1],
    ["set", 2, 2],
    ["set", 3, 3],
    ["get", 1],
    ["get", 2],
    ["get", 3]
]
expected2 = [-1, 2, 3]
test_case2 = [cache2, operations2, expected2]
test_function(test_case2)

# %%
# For a cache with capacity 0, we should handle the empty list case
cache3 = LRU_Cache(0)
operations3 = [
    ["set", 1, 1],
    ["get", 1],
    ["set", 2, 2],
    ["get", 2]
]
expected3 = [-1, -1]  # All get operations should return -1 since nothing can be stored
test_case3 = [cache3, operations3, expected3]
test_function(test_case3)


