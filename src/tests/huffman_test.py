import unittest
from huffman import Node
from huffman import *

class TestHuffman(unittest.TestCase):
    def setUp(self):
        pass

    def test_frequency_table(self):
        freq_table = create_freq_table("AABCBAD")
        self.assertEqual(freq_table["A"], 3)
        self.assertEqual(freq_table["B"], 2)
        self.assertEqual(freq_table["C"], 1)
        self.assertEqual(freq_table["D"], 1)
