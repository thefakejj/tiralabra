import unittest
from lz import *
import os

def create_mock_trie():
    a = 0
    b = 1
    c = 2
    d = 3
    e = 4
    f = 5

    a.children["A"] = b
    a.children["B"] = e
    a.children["C"] = d

    b.children["B"] = c
    b.children["D"] = f
    return a

class TestHuffman(unittest.TestCase):
    def setUp(self):
        self.mock_trie = create_mock_trie()
        self.readbin_path = "./src/tests/test_bin/read_this.bin"
        self.abc_path = "./src/tests/test_bin/aabcbad.bin"
        self.savebin_path = "./src/tests/test_bin/save_this.bin"
        self.testbytes = bytearray()
        self.testbytes.append(255)
    

