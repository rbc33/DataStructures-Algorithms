# %%
import sys
from collections import deque
class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        
    def __repr__(self):
        return f"Node(char={self.char}, freq={self.freq})"

class Tree:
    def __init__(self, root=None):
        self.root = root
        
    def get_root(self):
        return self.root
        
    def __repr__(self):
        return f"Tree(root={self.root})"

# %%
def dic_of_frequency(data):
    freq = {}
    for i in data:
        if i in freq.keys():
            freq[i] += i
        else:
            freq[i] = i 
    return freq

# %%
def generate_codes(node, current_code, codes):
    if node is None:
        return
        
    # If this is a leaf node (has a character)
    if node.char is not None:
        codes[node.char] = current_code if current_code else "0"
        return
    
    # Traverse left (add 0)
    generate_codes(node.left, current_code + "0", codes)
    
    # Traverse right (add 1)
    generate_codes(node.right, current_code + "1", codes)

# %%
def create_tree(nodes):
    while len(nodes) > 1:
        # Find two nodes with lowest frequencies
        min_node1 = min(nodes, key=lambda x: x.freq)
        nodes.remove(min_node1)
        
        min_node2 = min(nodes, key=lambda x: x.freq)
        nodes.remove(min_node2)
        
        # Create new internal node with these two as children
        node_sum = Node(None, min_node1.freq + min_node2.freq)
        node_sum.left = min_node1
        node_sum.right = min_node2
        
        # Add the new node back to the queue
        nodes.append(node_sum)
    
    # Create and return a Tree with the root node
    return Tree(nodes[0]) if nodes else Tree()


def huffman_encoding(data):
    if not data:
        return "", None
        
    # Get frequency of each character
    freq = dic_of_frequency(data)
    
    # Create nodes for each character
    nodes = deque()
    for char, frequency in freq.items():
        nodes.append(Node(char, frequency))
    
    # Build the Huffman tree
    tree = create_tree(nodes)
    
    # Generate codes for each character
    codes = {}
    generate_codes(tree.get_root(), "", codes)
    
    # Encode the data
    encoded_data = ""
    for char in data:
        encoded_data += codes[char]
    
    return encoded_data, tree

    
            

def huffman_decoding(data,tree):
    if not data or tree.get_root() is None:
        return ""
    
    root = tree.get_root()
    
    # Special case for tree with only one character
    if root.left is None and root.right is None:
        return root.char * len(data)
    
    decoded_data = ""
    current_node = root
    
    # Traverse the Huffman tree based on the encoded data
    for bit in data:
        if bit == '0':
            current_node = current_node.left
        else:  # bit == '1'
            current_node = current_node.right
            
        # If we reach a leaf node (character node)
        if current_node.left is None and current_node.right is None:
            decoded_data += current_node.char
            current_node = root  # Reset to the root for next character
    
    return decoded_data

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print(f"The size of the data is: {sys.getsizeof(a_great_sentence)}")
    print(f"The content of the data is: {a_great_sentence}")

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print(f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2))}")
    print(f"The content of the encoded data is: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, tree)

    print(f"The size of the decoded data is: {sys.getsizeof(decoded_data)}")
    print(f"The content of the encoded data is: {decoded_data}")



# %%
huffman_encoding("ht")

# %%
test_string = "AAAABBBCCD"
print("Test Case 1: String with different frequency characters")
print(f"Original string: {test_string}")
encoded_data, tree = huffman_encoding(test_string)
print(f"Encoded data: {encoded_data}")
decoded_data = huffman_decoding(encoded_data, tree)
print(f"Decoded data: {decoded_data}")
print(f"Original size: {sys.getsizeof(test_string)} bytes")
print(f"Encoded size: {sys.getsizeof(int(encoded_data, base=2))} bytes")
print(f"Compression ratio: {sys.getsizeof(test_string)/sys.getsizeof(int(encoded_data, base=2)):.2f}\n")


# %%
test_string = ""
print("Test Case 2: Empty string")
encoded_data, tree = huffman_encoding(test_string)
print(f"Original string: '{test_string}'")
print(f"Encoded data: '{encoded_data}'")
decoded_data = huffman_decoding(encoded_data, tree)
print(f"Decoded data: '{decoded_data}'\n")

# %%
test_string = "AAAAAAAAAA"
print("Test Case 3: String with a single repeated character")
print(f"Original string: {test_string}")
encoded_data, tree = huffman_encoding(test_string)
print(f"Encoded data: {encoded_data}")
decoded_data = huffman_decoding(encoded_data, tree)
print(f"Decoded data: {decoded_data}")
print(f"Original size: {sys.getsizeof(test_string)} bytes")
print(f"Encoded size: {sys.getsizeof(int(encoded_data, base=2) if encoded_data else 0)} bytes")


