from huffman import create_freq_table, create_tree, huffman_codes_to_characters_connection

def get_text_from_file(path):
    with open(path) as f:
        return f.read()

if __name__ in "__main__":
    filetext = get_text_from_file("./src/sampletexts/johndoe.txt")
    freq_table = create_freq_table(filetext)
    #print(freq_table)
    tree = create_tree(freq_table)
    huffman_codes = huffman_codes_to_characters_connection(tree, freq_table)
    print(huffman_codes)