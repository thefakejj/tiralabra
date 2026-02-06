from huffman import bytes_to_text, huffman_string_to_binary_file, binary_to_text, get_codelist_from_file, save_codelist_to_file, codelist_to_text, create_huffman_string, create_freq_table, create_tree, huffman_codes_to_characters_connection

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
    og_path = "./src/sampletexts/johndoe.txt"
    filetext = get_text_from_file(og_path)
    #binaryfile = open("binfile.bin", "wb")
    
    # funnytext = "ABRACADABRARABARABARA"
    # lz_table = lz(funnytext)
    # print(lz_table)
    # print(init_decode(lz_table))

    # # HUFFMAN
    freq_table = create_freq_table(filetext)
    #print(freq_table)
    tree = create_tree(freq_table)
    huffman_codes, chars = huffman_codes_to_characters_connection(tree)
    #print(huffman_codes["T"])
    output_string, codelist = create_huffman_string(filetext, huffman_codes)
   # codelist = create_huffman_string(filetext, huffman_codes)

    # print(filetext)
    #print(output_string)
    #print(codelist)

    bin_path = "./binfile.bin"
    save_codelist_to_file(bin_path, codelist)
    bindata = get_codelist_from_file(bin_path)

    compare_file_size(og_path, bin_path)

    huffman_string_to_binary_file(output_string, bin_path)

    bindata = get_codelist_from_file(bin_path)
    og_text = bytes_to_text(bindata, chars)
    print(og_text)


    #original_text = codelist_to_text(codelist, chars)
    #print(original_text)

