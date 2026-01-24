
def lz(text: str):
    existing_tokens = set()
    tokens = [None]
    indices = dict()

    current = ""
    #current = text[0]
    index = 1
    for char in text:
        current += char
        if current not in indices:
            indices[current] = index
            index += 1
            current = ""
            continue
        index_string = str(indices[current])
        current = index_string
    
    current+="EOF"
    indices[current] = index

    return indices
