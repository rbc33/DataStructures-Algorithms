# Huffman Coding Implementation

This implementation provides a complete solution for Huffman coding, a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies.

The solution uses a combination of:

- A `Node` class to represent elements in the Huffman tree, storing character data, frequency, and references to child nodes
- A `Tree` class to encapsulate the Huffman tree structure with a root node
- A frequency dictionary to count character occurrences in the input data
- A priority mechanism to build the tree by repeatedly combining the least frequent nodes

The algorithm works in several steps:

1. Count the frequency of each character in the input data
2. Create leaf nodes for each character with its frequency
3. Build the Huffman tree by repeatedly combining the two nodes with lowest frequencies
4. Generate unique binary codes for each character by traversing the tree
5. Encode the original data using these codes
6. Provide a decoding mechanism to recover the original data

The time complexity is O(n log n) where n is the number of unique characters, with space complexity of O(n) for storing the tree and codes. The implementation handles edge cases such as empty strings and inputs with a single character.

This approach provides efficient compression for text data where character frequencies vary significantly, with more frequent characters receiving shorter codes.
