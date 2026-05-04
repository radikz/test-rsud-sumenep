import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

target_path = os.path.join(current_dir, '..', 'python', 'soal1')

sys.path.append(os.path.abspath(target_path))

from soal1 import max_tri_sum

class TestMaxTriSum(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(max_tri_sum([3,2,6,8,2,3]), 17)
    def test_examples1(self):
        self.assertEqual(max_tri_sum([2,1,8,0,6,4,8,6,2,4]), 18)
    def test_examples2(self):
        self.assertEqual(max_tri_sum([-7,12,-7,29,-5,0,-7,0,0,29]), 41)

    def test_edge_cases(self):
        self.assertEqual(max_tri_sum([1,1,1,2,2,3]), 6)
    def test_edge_cases1(self):
        self.assertEqual(max_tri_sum([-5,-4,-3,-2,-1]), -6)   # -1-2-3 
    def test_edge_cases2(self):
        self.assertEqual(max_tri_sum([0,0,0,1,-1]), 0)        # 1+0+(-1)
    def test_edge_cases2(self):
        self.assertEqual(max_tri_sum([10,10,10,10,10]), 10) 
    def test_edge_cases3(self):
        self.assertEqual(max_tri_sum([10,10,10,10,30]), 40)   

if __name__ == '__main__':
    unittest.main()