from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return 0


import unittest

class TestSolution(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution().maxProfit([1,2,3,0,2]), 
                         3, 
                         "EXPECTED 3")
        self.assertEqual(Solution().maxProfit([1]), 
                         0, 
                         "EXPECTED 0")

if __name__ == '__main__':
    unittest.main()