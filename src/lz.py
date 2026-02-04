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


# def text_from_tokens(table: list):
#     current = ""
#     for pair in table:
#         if pair != None:
#             current += pair[1]
#     return current

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
        if pair != None:
            result += text_from_tokens(table, pair)
    return result
