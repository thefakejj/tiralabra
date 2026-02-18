from huffman import binary_string_to_tree, tree_to_binary_string, bfs, bytes_to_text, huffman_string_to_binary_file, get_bytes_from_binfile, create_huffman_string, create_freq_table, create_tree, huffman_codes_to_characters_connection

from lz import lz_decode, lz_binary_to_bytes, bytes_to_bits, lz_bits_to_table, lz_binary_to_file, lz_to_binary_string, lz

import os

def get_text_from_file(path):
    with open(path, encoding="ASCII") as f:
        return f.read()[:-1]
    
def compare_file_size(og_path, bin_path):
    og_size = os.path.getsize(og_path)
    bin_size = os.path.getsize(bin_path)
    print(f"Original file size: {og_size}\nBinary file size: {bin_size}")

if __name__ in "__main__":

    og_path = "./src/sampletexts/hamlet.txt"
    filetext = get_text_from_file(og_path)

    # # # funnytext = "ABRACADABRARABARABARA"
    # # # lz_table = lz(funnytext)
    # # # print(lz_table)

    lz_table = lz(filetext)
    #print(lz_table)

    bin_path = "./binfile.bin"
    
    lz_binary = lz_to_binary_string(lz_table)

    lz_binary_to_file(lz_binary, bin_path)

    compare_file_size(og_path, bin_path)
    # print(init_decode(lz_table))

    lz_bytes = lz_binary_to_bytes(bin_path)

    lz_bits = bytes_to_bits(lz_bytes)

    new_lz_table = lz_bits_to_table(lz_bits)
    #print(new_lz_table)
    print("tables same:", lz_table==new_lz_table)
    
    lz_decoded = lz_decode(new_lz_table)
    #print(lz_decoded)
    print(f"text matches: {filetext==lz_decoded}")

    print()
    filetext = get_text_from_file(og_path)

    # # HUFFMAN
    freq_table = create_freq_table(filetext)
    tree = create_tree(freq_table)
    huffman_codes = huffman_codes_to_characters_connection(tree) [0]
    output_string = create_huffman_string(filetext, huffman_codes)

    tree_in_bits = tree_to_binary_string(tree)

    bin_path = "./binfile.bin"

    huffman_string_to_binary_file(tree_in_bits, output_string, bin_path)
    compare_file_size(og_path, bin_path)

    bindata = get_bytes_from_binfile(bin_path)

    og_text = bytes_to_text(bindata)
    print(f"text matches: {filetext==og_text}")
    # print(og_text)
