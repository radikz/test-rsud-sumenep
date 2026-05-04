import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

target_path = os.path.join(current_dir, '..', 'python', 'soal3')

sys.path.append(os.path.abspath(target_path))

from soal3 import generate_snake_pattern

class TestSnakePattern(unittest.TestCase):
    def test_n_3(self):
        expected = [[7, 8, 9], [6, 5, 4], [1, 2, 3]]
        self.assertEqual(generate_snake_pattern(3), expected)

    def test_n_2(self):
        expected = [[4, 3], [1, 2]]
        self.assertEqual(generate_snake_pattern(2), expected)

if __name__ == '__main__':
    unittest.main()