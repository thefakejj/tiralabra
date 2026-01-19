#Huffman-koodaus

def create_freq_table(text: str):
    freq_table = {}
    for char in text:
        if not char in freq_table:
            freq_table[char] = 1
        else:
            freq_table[char] += 1
    return freq_table
