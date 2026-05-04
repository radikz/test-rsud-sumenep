import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

target_path = os.path.join(current_dir, '..', 'python', 'soal4')

sys.path.append(os.path.abspath(target_path))

from soal4 import maskify

class TestMaxTriSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(maskify("4556364607935616"), "############5616")
    def test_examples1(self):
        self.assertEqual(maskify("64607935616"), "#######5616")
    def test_examples2(self):
        self.assertEqual(maskify("1"), "1")

    def test_edge_cases(self):
        self.assertEqual(maskify(""), "")
    def test_edge_cases1(self):
        self.assertEqual(maskify("Skippy"), "##ippy")
    def test_edge_cases2(self):
        self.assertEqual(maskify("Nananananananananananananananana Batman!"), 
                         "####################################man!")
    def test_edge_cases6(self):
        self.assertEqual(maskify("1234567890"), "######7890")
    def test_edge_cases3(self):
        self.assertEqual(maskify("abcd"), "abcd")
    def test_edge_cases4(self):
        self.assertEqual(maskify("a"), "a")
    def test_edge_cases5(self):
        self.assertEqual(maskify("123"), "123")

if __name__ == '__main__':
    unittest.main()