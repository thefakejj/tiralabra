class Node:
    def __init__(self, index: int):
        self.index = index
        self.children = dict()
    
    def search(self, root, key: list):
        x = root
        for char in key:
            if x.children.get(char) == None:
                return None
            x = x.children[char]
        return x
    
    def insert(self, x, key: list, value: int):
        for char in key:
            if x.children.get(char) == None:
                new_node = Node(value)
                x.children[char] = new_node
                return
            x = x.children[char]
            

# Trie-Insert(x, key, value)
#     for 0 ≤ i < key.length do
#         if x.Children[key[i]] = nil then
#             x.Children[key[i]] := Create-New-Node()
#         end if
#         x := x.Children[key[i]]
#     repeat
#     x.Value := value


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


def lz2(text: str):
    codes = dict()
    codes[0] = ""
    index = 1
    prev_index = 0
    current = ""
    for char in text:
        current += char
        if current not in codes:
            codes[index] = ()
            
    
    
    return indices


# def lz(text: str):
    


def lz(text: str):
    existing_tokens = set()
    tokens = [None]
    codes = dict()

    current = ""
    codes[0] = ""
    prev_index = 0
    index = 1
    pair = (0, "")
    for char in text:
        current += char
        if len(current) == 1:
            pair = (prev_index, current)
        if current not in existing_tokens:
            existing_tokens.add(current)
            codes[current] = index
            index += 1
            current = ""
            continue
        index_string = str(codes[current])
        current = index_string
    
    current+="EOF"
    codes[current] = index

    return codes
