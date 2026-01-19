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
def set_huffman_codes(node, codes: list, current: str):

    if node is None:
        return
    
    if node.left is None and node.right is None:
        codes.append(current)
        node.add_huff_code(current)
        return

    set_huffman_codes(node.left, codes, current+"0")
    set_huffman_codes(node.right, codes, current+"1")

def huffman_codes_to_characters_connection(root, freq_table: dict):
    codes = []
    set_huffman_codes(root, codes, "")
    huff_codes = {}
    char_i = 0
    bfs(root)
    # for char in freq_table.keys():
    #     huff_codes[char] = codes[char_i]
    #     char_i += 1
    # print(huff_codes)
   # return huff_codes











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