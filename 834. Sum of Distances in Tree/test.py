import unittest
import solution

'''
CREATED Test Cases
- python standard library "unittest"
- import within module requires import filename
- import outside module requires from modulename import filename
'''

class TestSolution(unittest.TestCase):
    def test(self):
        self.assertEqual(solution.Solution().sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]), 
                         [8,12,6,10,10,10], 
                         "EXPECTED [8,12,6,10,10,10]")
        self.assertEqual(solution.Solution().sumOfDistancesInTree(1, []), 
                         [0], 
                         "EXPECTED [0]")
        self.assertEqual(solution.Solution().sumOfDistancesInTree(2, [[1,0]]), 
                         [1,1], 
                         "EXPECTED [1,1]")

if __name__ == '__main__':
    unittest.main()