import heapq

# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Comparator for heap
    def __lt__(self, other):
        return self.freq < other.freq


# Function to generate Huffman Codes
def generate_codes(root, current_code, huffman_codes):
    if root is None:
        return
    
    # If leaf node
    if root.char is not None:
        huffman_codes[root.char] = current_code
        return
    
    generate_codes(root.left, current_code + "0", huffman_codes)
    generate_codes(root.right, current_code + "1", huffman_codes)


# Function to build Huffman Tree
def build_huffman_tree(chars, freqs):
    heap = []
    
    # Create initial nodes
    for i in range(len(chars)):
        heapq.heappush(heap, Node(chars[i], freqs[i]))
    
    # Edge case: only one character
    if len(heap) == 1:
        root = heapq.heappop(heap)
        new_root = Node(None, root.freq)
        new_root.left = root
        return new_root
    
    # Build tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        heapq.heappush(heap, merged)
    
    return heap[0]


# Main function
def huffman_coding():
    print("=== Huffman Coding using Greedy Approach ===")
    
    try:
        n = int(input("Enter number of characters: "))
        
        # Constraints check
        if n <= 0:
            print("Error: Number of characters must be > 0")
            return
        
        chars = []
        freqs = []
        
        print("Enter characters:")
        for i in range(n):
            ch = input(f"Character {i+1}: ")
            if len(ch) != 1:
                print("Error: Enter only single character")
                return
            chars.append(ch)
        
        print("Enter frequencies:")
        for i in range(n):
            f = int(input(f"Frequency of '{chars[i]}': "))
            if f <= 0:
                print("Error: Frequency must be > 0")
                return
            freqs.append(f)
        
        # Build tree
        root = build_huffman_tree(chars, freqs)
        
        # Generate codes
        huffman_codes = {}
        generate_codes(root, "", huffman_codes)
        
        # Output
        print("\n--- Huffman Codes ---")
        print("{:<10} {:<10} {:<10}".format("Character", "Frequency", "Code"))
        print("-" * 30)
        
        for i in range(n):
            print("{:<10} {:<10} {:<10}".format(chars[i], freqs[i], huffman_codes[chars[i]]))
    
    except ValueError:
        print("Error: Invalid input. Please enter integers where required.")


# Run program
if __name__ == "__main__":
    huffman_coding()