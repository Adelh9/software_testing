import unittest
from Solution import spiralOrder

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = spiralOrder

    # Divided Tests into EP and BVA 
    # EP
    def test_spiralOrder_ep(self):
        # Test case 8: Matrix with negative values
        matrix8 = [[1, -2, 3],
                   [4, -5, 6],
                   [7, -8, 9]]
        expected8 = [1, -2, 3, 6, 9, -8, 7, 4, -5]
        self.assertEqual(self.solution(matrix8), expected8)
        print("Passed Test case 8: Matrix with negative values") 


        # Test case 10: Matrix with irregular dimensions
        matrix10 = [[1, 2, 3],
                    [4, 5],
                    [6, 7, 8, 9]]
        expected10 = [1, 2, 3, 5, 9, 8, 7, 6, 4]
        self.assertEqual(self.solution(matrix10), expected10)
        print("Passed Test case 10: Matrix with irregular dimensions") 

        # Test case 11: Matrix with uneven dimensions
        matrix11 = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9],
                    [10, 11, 12]]
        expected11 = [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]
        self.assertEqual(self.solution(matrix11), expected11)
        print("Passed Test case 11: Matrix with uneven dimensions") 

        # Test case 12: Matrix with repeating elements
        matrix12 = [[1, 2, 3],
                    [4, 1, 6],
                    [7, 8, 1]]
        expected12 = [1, 2, 3, 6, 1, 8, 7, 4, 1]
        self.assertEqual(self.solution(matrix12), expected12)
        print("Passed Test case 12: Matrix with repeating elements") 

    # BVA
    def test_spiralOrder_bva(self):
        # Test case 1: 3x3 matrix
        matrix1 = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]
        expected1 = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(self.solution(matrix1), expected1)
        print("Passed Test case 1: 3x3 matrix") 

        # Test case 2: 4x5 matrix
        matrix2 = [[1,  2,  3,  4,  5],
                   [6,  7,  8,  9,  10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20]]
        expected2 = [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
        self.assertEqual(self.solution(matrix2), expected2)
        print("Passed Test case 2: 4x5 matrix") 

        # Test case 3: 2x2 matrix
        matrix3 = [[1, 2],
                   [3, 4]]
        expected3 = [1, 2, 4, 3]
        self.assertEqual(self.solution(matrix3), expected3)
        print("Passed Test case 3: 2x2 matrix") 

        # Test case 4: Empty matrix
        matrix4 = []
        expected4 = []
        self.assertEqual(self.solution(matrix4), expected4)
        print("Passed Test case 4: Empty matrix") 

        # Test case 5: Matrix with a single row
        matrix5 = [[1, 2, 3, 4, 5]]
        expected5 = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution(matrix5), expected5)
        print("Passed Test case 5: Matrix with a single row") 

        # Test case 6: Matrix with a single column
        matrix6 = [[1], [2], [3], [4], [5]]
        expected6 = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution(matrix6), expected6)
        print("Passed Test case 6: Matrix with a single column") 

        # Test case 7: 1x1 matrix
        matrix7 = [[42]]
        expected7 = [42]
        self.assertEqual(self.solution(matrix7), expected7)
        print("Passed Test case 7: 1x1 matrix") 

        # Test case 9: Matrix with zero values
        matrix9 = [[0, 0, 0],
                   [0, 0, 0],
                   [0, 0, 0]]
        expected9 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(self.solution(matrix9), expected9)
        print("Passed Test case 9: Matrix with zero values") 

if __name__ == '__main__':
    unittest.main()