# %%
import hashlib
import datetime


# %%
class Block:

    def __init__(self, data, previous_hash):
      self.timestamp = datetime.datetime.now()
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.next = None

    def calc_hash(self):
      sha = hashlib.sha256()

      hash_str = "We are going to encode this string of data!".encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

## Add your own test cases: include at least three test cases
## and two of them must include edge cases, such as null, empty or very large values

## Test Case 1

## Test Case 2

## Test Case 3

# %%
class Blockchain:
    def __init__(self):
        self.head = None
        self.previous_hash = None
        self.next = None
    def push(self, data):
        if not self.head:
            self.head = Block(data, self.previous_hash)
            self.previous_hash = self.head.previous_hash
        else:
            new_head = Block(data, self.head.previous_hash)
            new_head.next = self.head
            self.head = new_head




# %%
my_block = Blockchain()
my_block.push(3)
my_block.push(4)

# %%
# Test Case 1: Normal blockchain operation
blockchain = Blockchain()
blockchain.push("First Block Data")
blockchain.push("Second Block Data")
blockchain.push("Third Block Data")

print("Test Case 1: Normal blockchain operation")
current = blockchain.head
block_number = 1
while current:
    print(f"Block {block_number}:")
    print(f"Data: {current.data}")
    print(f"Previous Hash: {current.previous_hash}")
    print("-" * 30)
    current = current.next
    block_number += 1

# %%
# Test Case 2: Edge case - Empty blockchain
empty_blockchain = Blockchain()
print("\nTest Case 2: Empty blockchain")
if empty_blockchain.head is None:
    print("Blockchain is empty")
else:
    print("Blockchain is not empty")

# %%
# Test Case 3: Edge case - Large data input
import random
import string

# Generate a large random string
large_data = ''.join(random.choices(string.ascii_letters + string.digits, k=10000))

large_blockchain = Blockchain()
large_blockchain.push(large_data)

print("\nTest Case 3: Large data input")
print(f"Block hash length: {len(large_blockchain.head.hash)}")
print(f"First 50 chars of data: {large_blockchain.head.data[:50]}...")
print(f"Data size: {len(large_blockchain.head.data)} characters")


