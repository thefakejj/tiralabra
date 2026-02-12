from huffman import bfs, bytes_to_text, huffman_string_to_binary_file, get_bytes_from_binfile, create_huffman_string, create_freq_table, create_tree, huffman_codes_to_characters_connection

from lz import lz, text_from_tokens, init_decode

import os

def get_text_from_file(path):
    with open(path, encoding="ASCII") as f:
        return f.read()
    
def compare_file_size(og_path, bin_path):
    og_size = os.path.getsize(og_path)
    bin_size = os.path.getsize(bin_path)
    print(f"Original file size: {og_size}\nBinary file size: {bin_size}")

if __name__ in "__main__":
    og_path = "./src/sampletexts/aabcbad.txt"
    filetext = get_text_from_file(og_path)
    print(filetext)
    
    # funnytext = "ABRACADABRARABARABARA"
    # lz_table = lz(funnytext)
    # print(lz_table)
    # print(init_decode(lz_table))

    # # HUFFMAN
    freq_table = create_freq_table(filetext)
    print(freq_table)
    tree = create_tree(freq_table)
    bfs(tree)
    huffman_codes, chars = huffman_codes_to_characters_connection(tree)
    output_string, codelist = create_huffman_string(filetext, huffman_codes)
    print(huffman_codes)
    print(output_string)
   # codelist = create_huffman_string(filetext, huffman_codes)

    bin_path = "./binfile.bin"

    huffman_string_to_binary_file(output_string, bin_path)
    compare_file_size(og_path, bin_path)

    bindata = get_bytes_from_binfile(bin_path)

    og_text = bytes_to_text(bindata, chars)
    print(og_text)
