import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    # Define comparison operators for the priority queue
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    # Create a priority queue (min-heap)
    heap = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        # Extract the two nodes with the smallest frequencies
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # Create a new internal node with these two nodes as children
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        # Add the new node to the heap
        heapq.heappush(heap, merged)
    
    # The remaining node is the root of the Huffman tree
    return heap[0]

def generate_huffman_codes(root):
    codes = {}
    
    def _generate_codes(node, current_code):
        if node is None:
            return
        
        # If this is a leaf node, add the code to the dictionary
        if node.char is not None:
            codes[node.char] = current_code
            return
        
        # Traverse the left subtree
        _generate_codes(node.left, current_code + "0")
        
        # Traverse the right subtree
        _generate_codes(node.right, current_code + "1")
    
    _generate_codes(root, "")
    return codes

def huffman_encoding(data):
    if not data:
        return "", None
    
    # Count the frequency of each character in the data
    frequencies = Counter(data)
    
    # Build the Huffman tree
    root = build_huffman_tree(frequencies)
    
    # Generate Huffman codes
    codes = generate_huffman_codes(root)
    
    # Encode the data
    encoded_data = "".join(codes[char] for char in data)
    return encoded_data, root

def huffman_decoding(encoded_data, root):
    if not encoded_data or root is None:
        return ""
    
    decoded_data = []
    current_node = root
    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        # If we reach a leaf node, append the character to the result
        if current_node.char is not None:
            decoded_data.append(current_node.char)
            current_node = root
    
    return "".join(decoded_data)

# Example usage:
data = "this is an example for huffman encoding"
encoded_data, tree = huffman_encoding(data)
print(f"Encoded data: {encoded_data}")

decoded_data = huffman_decoding(encoded_data, tree)
print(f"Decoded data: {decoded_data}")
