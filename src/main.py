from huffman import binary_to_text, get_codelist_from_file, save_codelist_to_file, codelist_to_text, create_huffman_string, create_freq_table, create_tree, huffman_codes_to_characters_connection

from lz import lz, text_from_tokens, init_decode

def get_text_from_file(path):
    with open(path, encoding="ASCII") as f:
        return f.read()

if __name__ in "__main__":
    filetext = get_text_from_file("./src/sampletexts/johndoe.txt")
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
    # output_string, codelist = create_huffman_string(filetext, huffman_codes)
    codelist = create_huffman_string(filetext, huffman_codes)

    # print(filetext)
    #print(output_string)
    #print(codelist)

    binfilepath = "./binfile.bin"
    save_codelist_to_file(binfilepath, codelist)
    bindata = get_codelist_from_file(binfilepath)

    og_text = binary_to_text(bindata, chars)
    print(og_text)

    #original_text = codelist_to_text(codelist, chars)
    #print(original_text)

