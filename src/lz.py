class Node:
    def __init__(self, index: int):
        self.index = index
        self.children = dict()

    def search(self, root, key: str):
        x = root
        prev_index = 0
        for i in range(len(key)):
            if x.children.get(key[i]) == None:
                return (None, prev_index)
            x = x.children[key[i]]
            prev_index = x.index
        return (x.index, prev_index)

    def insert(self, x, key: str, index: int):
        for char in key:
            if x.children.get(char) == None:
                new_node = Node(index)
                x.children[char] = new_node
                return
            x = x.children[char]

def lz(text: str):
    # table is a list of (index, character), where index refers to intex of correct coding in this table and character is a new character
    # starts with empty node
    table = [None]
    trie_root = Node(0)

    current = ""
    cur_index = 1
    for char in text:
        current += char
        result = trie_root.search(trie_root, current)
        if result[0] == None:
            trie_root.insert(trie_root, current, cur_index)
            prev_index = result[1]
            pair = (prev_index, char)
            table.append(pair)
            cur_index += 1
            current = ""
    return table

def lz_to_binary_string(table: list):
    # first is empty
    # we're going to create a string with all the bits
    output = ""
    # without the first None "pair"
    for pair in table[1:]:
        reference = pair[0]
        if reference >= 4096:
            raise ValueError("More than 4096 entries. This LZ78 is limited to 4096 entries.")
            
        ref_twelve = format(reference, "b")
        ref_twelve = left_pad_byte(ref_twelve, 12)

        char = pair[1]
        char_ascii = ord(char)
        char_ascii = format(char_ascii, "b")
        char_ascii = left_pad_byte(char_ascii, 8)
        # UNRELATED TO PROJECT https://www.youtube.com/watch?v=rPIt52BwTak 

        entry = ref_twelve+char_ascii
        output += entry
    return output
    
def lz_binary_to_file(binary_string: str, filepath: str):
    # could create a file saving function since this is almost same as huffman_string_to_binary_file
    missing_bits = (8 - len(binary_string)) % 8
    padding = "0"*missing_bits
    binary_string += padding

    bytes = bytearray()
    bytes.append(missing_bits)
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        bytes.append(int(byte, 2))

    with open(filepath, "wb") as binfile:
        binfile.write(bytes)

def lz_binary_to_bytes(filepath: str):
    with open(filepath, "rb") as binfile:
        bytes = binfile.read()
    return bytes

def bytes_to_bits(bytes: list):
    bits = ""
    detected_padding = bytes[0]
    for i in range(1, len(bytes)):
        byte = bytes[i]
        byte = format(byte, "b")
        byte = left_pad_byte(byte, 8)
        bits += byte
    end_index = len(bits) - detected_padding
    bits = bits[0:end_index] # string bits should include all binary starting from tree
    return bits

def lz_bits_to_table(bits: str):
    table = [None]
    # we want to first read 12 bits, which gives us a reference
    # then we want to read 8 bits, which gives the character's acsii code
    # True if currently reading reference
    for i in range(0, len(bits), 20):
        start = i
        end = i+20

        reference = bits[start:start+12]
        reference = int(reference)
    
        char = bits[start+12:end]
        char = int(char, 2)
        char = chr(char)

        pair = (reference, char)
        table.append(pair)
    return table


# def text_from_tokens(table: list):
#     current = ""
#     for pair in table:
#         if pair != None:
#             current += pair[1]
#     return current

# forgive the repetition this once
def left_pad_byte(byte: str, target_len: int):
        missing_bits = (target_len - len(byte)) % target_len
        padding = "0"*missing_bits
        byte = padding+byte
        return byte

def text_from_tokens(table: list, pair, current = ""):
    if pair[0] != 0:
        current += text_from_tokens(table, table[pair[0]], current)
    current += pair[1]
    return current


    # for pair in table:

    #     if pair != None:
    #         prev_index = pair[0]
            
    #         if prev_index != 0:
    #             text_from_tokens(table, prev_index)
    #         current += pair[1]

    # return current

def init_decode(table: list):
    result = ""
    for pair in table:
        if pair == None:
            continue
        if pair[0] != 0:
            iter = pair
            stack = []
            while iter[0] != 0:
                stack.append(iter[1])
                iter = table[iter[0]]
            stack.append(pair[1])
            while len(stack) > 0:
                result += stack.pop()
            continue
        result += pair[1]
    return result



# def init_decode(table: list):
#     result = ""
#     for pair in table:
#         if pair == None:
#             continue

#         if pair[0] != 0:
#             iter = pair
#             stack = []
#             while iter[0] != 0:
#                 print("moi")
#                 stack.append(iter[1])
#                 iter = table[iter[0]]
#                 print(stack)
#             print(iter)
#             for _ in stack:
#                 print("hei")
#                 result += stack.pop()
#         else:
#             result += pair[1]
#     return result
