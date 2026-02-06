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

    set_huffman_codes(node.left, codes, current+b"0", chars)
    set_huffman_codes(node.right, codes, current+b"1", chars)

def huffman_codes_to_characters_connection(root):
    codes = {}
    chars = {}
    set_huffman_codes(root, codes, b"", chars)
    return codes, chars

def create_huffman_string(text: str, codes: dict):
    output = b""
    codelist = []
    for char in text:
        output+=codes[char]
        codelist.append(codes[char])
    return output, codelist

def codelist_to_text(codelist: list, chars: dict):
    output = ""
    for code in codelist:
        output+= chars[code]
    return output








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