import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

target_path = os.path.join(current_dir, '..', 'python', 'soal2')

sys.path.append(os.path.abspath(target_path))

from soal2 import sum_two_smallest_numbers

class TestMaxTriSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(sum_two_smallest_numbers([19, 5, 42, 2, 77]), 7)
    def test_examples1(self):
        self.assertEqual(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]), 3453455)
    def test_examples2(self):
        self.assertEqual(sum_two_smallest_numbers([4, 1, 7, 3]), 4)

    def test_edge_cases(self):
        self.assertEqual(sum_two_smallest_numbers([5, 8, 12, 19, 22]), 13)
    def test_edge_cases1(self):
        self.assertEqual(sum_two_smallest_numbers([15, 28, 4, 2, 43]), 6)
    def test_edge_cases2(self):
        self.assertEqual(sum_two_smallest_numbers([3, 87, 45, 12, 7]), 10)

if __name__ == '__main__':
    unittest.main()