from huffman import decode_huffman, encode_huffman

from lz import decode_lz, encode_lz

import os

def get_text_from_file(path):
    with open(path, encoding="ASCII") as f:
        return f.read()[:-1]
    
def compare_file_size(og_path, bin_path):
    og_size = os.path.getsize(og_path)
    bin_size = os.path.getsize(bin_path)
    print(f"Original file size: {og_size}\nBinary file size: {bin_size}\nCompression ratio: {(bin_size/og_size)*100:.2f}%")

if __name__ in "__main__":

    og_path = "./src/sampletexts/hamlet.txt"
    filetext = get_text_from_file(og_path)
    bin_path = "./binfile.bin"

    # LZ78

    encode_lz(filetext, bin_path)
    compare_file_size(og_path, bin_path)
    lz_output = decode_lz(bin_path)
    print(f"text matches: {filetext==lz_output}")

    # HUFFMAN

    encode_huffman(filetext, bin_path)
    compare_file_size(og_path, bin_path)
    huffman_output = decode_huffman(bin_path)
    print(f"text matches: {filetext==huffman_output}")