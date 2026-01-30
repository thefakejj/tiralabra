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

# def bfs(root, ):
#     visited = set()
#     queue = [root]
#     while len(queue)>0:
#         current = queue[0]
#         if current not in visited and not None:
#             for child in current.children:
#                 if child != None:
#                     queue.append(child)
#             visited.add(current)
#             queue.remove(current)
#         #print(current.freq)
#         #trying huff code attribute for leaves
#         if current.children.keys() == None:
#             print(current.char, current.code, current.freq)   


# def lz(text: str):
#     existing_tokens = set()
#     tokens = [None]
#     codes = dict()

#     current = ""
#     codes[0] = ""
#     prev_index = 0
#     index = 1
#     pair = (0, "")
#     for char in text:
#         current += char
#         if len(current) == 1:
#             pair = (prev_index, current)
#         if current not in existing_tokens:
#             existing_tokens.add(current)
#             codes[current] = index
#             index += 1
#             current = ""
#             continue
#         index_string = str(codes[current])
#         current = index_string
    
#     current+="EOF"
#     codes[current] = index

#     return codes



# def lz(text: str):
#     existing_tokens = set()
#     tokens = [None]
#     indices = dict()

#     current = ""
#     index = 1
#     indices[""] = 0
#     prev_index = 0
#     for char in text:
#         current += char
#         if current not in indices:
#             indices[current] = index
#             index += 1
#             current = ""
#             continue
#         index_string = str(indices[current])
#         current = index_string
    
#     current+="EOF"
#     indices[current] = index

#     return indices