# LRU Cache Implementation

This implementation of a Least Recently Used (LRU) cache efficiently manages a fixed-size cache by removing the least recently accessed items when the cache reaches capacity.

The solution uses a combination of:

- A dictionary ( self.cache ) for O(1) key-value lookups
- A double-ended queue ( collections.deque ) for tracking access order
  When an item is accessed or updated, it's moved to the front of the queue, marking it as most recently used. When the cache reaches capacity and a new item needs to be added, the least recently used item (at the end of the queue) is removed.

The time complexity for both get and set operations is O(1), with space complexity of O(n) where n is the cache capacity. Using Python's built-in deque provides efficient operations at both ends of the queue without the need to implement a custom doubly linked list.

This implementation handles edge cases such as zero capacity caches and maintains proper LRU ordering when items are accessed or updated.
