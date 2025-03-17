# Blockchain Implementation

This implementation provides a linked list-based solution for a blockchain data structure, where each block contains data, a timestamp, and cryptographic hashes to ensure integrity.

The solution uses:

- A `Block` class that stores data, timestamps, and hash information
- A `Blockchain` class that manages the chain of blocks using a linked list structure

The algorithm works by:

1. Creating blocks with unique timestamps and data
2. Calculating a cryptographic hash for each block based on its contents
3. Linking each new block to the previous one by storing the previous block's hash
4. Maintaining the integrity of the chain through this hash-based linking

The time complexity for adding a new block is O(1), with space complexity of O(n) where n is the number of blocks in the chain.

This implementation handles edge cases such as empty blockchains and blocks with large data inputs, providing a secure and efficient way to store immutable, chronologically-ordered data records.
