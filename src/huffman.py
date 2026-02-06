import heapq

#Huffman-koodaus

class Node:
    def __init__(self, freq: int, char=None):
        self.freq = freq
        self.char = char
        self.code = None
        self.left = None
        self.right = None

    def add_huff_code(self, code: str):
        self.code = code

    # less-than operaaito, jotta heap osaa järjestellä nodet
    def __lt__(self, other):
        return self.freq < other.freq

def create_freq_table(text: str):
    freq_table = {}
    for char in text:
        if not char in freq_table:
            freq_table[char] = 1
        else:
            freq_table[char] += 1
    return freq_table

def create_tree(freq_table: dict):
    prio_queue = []

    for char in freq_table:
        freq = freq_table[char]
        node = Node(freq, char)
        heapq.heappush(prio_queue, node)

    while len(prio_queue) >= 2:
        left = heapq.heappop(prio_queue)
        right = heapq.heappop(prio_queue)

        new_node = Node(left.freq+right.freq)
        new_node.left = left
        new_node.right = right
        heapq.heappush(prio_queue, new_node)

    root = heapq.heappop(prio_queue)
    return root

# rekursiivinen funktio jolla muodostetaan puun lehdille huffman-koodit
def set_huffman_codes(node, codes: dict, current, chars: dict):

    if node is None:
        return
    
    if node.left is None and node.right is None:
        #codes.append(current)
        #node.add_huff_code(current)
        codes[node.char] = current
        chars[current] = node.char
        return

    set_huffman_codes(node.left, codes, current+"0", chars)
    set_huffman_codes(node.right, codes, current+"1", chars)

def huffman_codes_to_characters_connection(root):
    codes = {}
    chars = {}
    set_huffman_codes(root, codes, "", chars)
    return codes, chars

def create_huffman_string(text: str, codes: dict):
    output = ""
    codelist = []
    for char in text:
        output+=codes[char]
        codelist.append(codes[char])
    return output, codelist

def save_codelist_to_file(filepath: str, codes: list):
    return
    with open(filepath, "wb") as binfile:
        for code in codes:
            binfile.write(code)

def get_codelist_from_file(filepath: str):
    with open(filepath, "rb") as binfile:
        binary = binfile.read()
    return binary

def codelist_to_text(codelist: list, chars: dict):
    output = ""
    for code in codelist:
        output+= chars[code]
    return output

def binary_to_text(binary, chars: dict):
    output = ""
    current = b""
    start_index = 0
    for i in range(1, len(binary)+1):
        current = binary[start_index:i]
        character = chars.get(current, None)
        if character == None:
            continue
        output += character
        start_index = i
        current = b""
    return output

def bytes_to_text(bytes, chars: dict):
    huffman_string = ""
    for byte in bytes:
        huffman_string += format(byte, "b")
    length = len(huffman_string)
    # huffman_string = huffman_string[0:length]
    print(huffman_string)
    output = ""
    current = ""
    start_index = 0
    for i in range(1, len(huffman_string)+1):
        current = huffman_string[start_index:i]
        character = chars.get(current, None)
        if character == None:
            continue
        output += character
        start_index = i
        current = ""
    return output
    return current

def huffman_string_to_binary_file(huffman_string: str, filepath):
    missing_bits = 8 - len(huffman_string) % 8
    padding = "0"*missing_bits
    huffman_string += padding

    bytes = bytearray()
    for i in range(0, len(huffman_string), 8):
        byte = huffman_string[i:i+8]
        bytes.append(int(byte, 2))

    with open(filepath, "wb") as binfile:
        binfile.write(bytes)


def bfs(root):
    visited = set()
    queue = [root]
    while len(queue)>0:
        current = queue[0]
        if current not in visited and not None:
            for child in [current.left, current.right]:
                if child != None:
                    queue.append(child)
            visited.add(current)
            queue.remove(current)
        #print(current.freq)
        #trying huff code attribute for leaves
        if current.left is None and current.right is None:
            print(current.char, current.code, current.freq)