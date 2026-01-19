from huffman import create_freq_table

def get_text_from_file(path):
    with open(path) as f:
        return f.read()

if __name__ in "__main__":
    filetext = get_text_from_file("./src/sampletexts/johndoe.txt")
    print(create_freq_table(filetext))
