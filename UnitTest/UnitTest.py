import unittest
from Solution import spiralOrder

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = spiralOrder

    # Divided Tests into EP and BVA 
    # EP
    def test_matrix_with_negative_values(self):
        matrix = [[1, -2, 3],
                  [4, -5, 6],
                  [7, -8, 9]]
        expected = [1, -2, 3, 6, 9, -8, 7, 4, -5]
        self.assertEqual(self.solution(matrix), expected)
        print("Passed Test case 8: Matrix with negative values") 

    def test_matrix_with_irregular_dimensions(self):
        matrix = [[1, 2, 3],
                  [4, 5],
                  [6, 7, 8, 9]]
        expected = [1, 2, 3, 5, 9, 8, 7, 6, 4]
        self.assertEqual(self.solution(matrix), expected)
        print("Passed Test case 10: Matrix with irregular dimensions") 
    
    def test_matrix_with_uneven_dimensions(self):
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9],
                  [10, 11, 12]]
        expected = [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]
        self.assertEqual(self.solution(matrix), expected)
        print("Passed Test case 11: Matrix with uneven dimensions") 
    
    def test_matrix_with_repeating_elements(self):
        matrix = [[1, 2, 3],
                  [4, 1, 6],
                  [7, 8, 1]]
        expected = [1, 2, 3, 6, 1, 8, 7, 4, 1]
        self.assertEqual(self.solution(matrix), expected)
        print("Passed Test case 12: Matrix with repeating elements")    # BVA

    def test_3x3_matrix(self):
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(self.solution(matrix), expected)
        print("Passed Test case 1: 3x3 matrix") 

    def test_4x5_matrix(self):
        matrix = [[1,  2,  3,  4,  5],
                  [6,  7,  8,  9,  10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20]]
        expected = [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
        self.assertEqual(self.solution(matrix), expected)
        print("Passed Test case 2: 4x5 matrix") 
    
    def test_2x2_matrix(self):
        matrix = [[1, 2],
                  [3, 4]]
        expected = [1, 2, 4, 3]
        self.assertEqual(self.solution(matrix), expected)
        print("Passed Test case 3: 2x2 matrix") 
    
    def test_empty_matrix(self):
        matrix = []
        expected = []
        self.assertEqual(self.solution(matrix), expected)
        print("Passed Test case 4: Empty matrix") 
    
    def test_single_row_matrix(self):
        matrix = [[1, 2, 3, 4, 5]]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution(matrix), expected)
        print("Passed Test case 5: Matrix with a single row") 
    
    def test_single_column_matrix(self):
        matrix = [[1], [2], [3], [4], [5]]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution(matrix), expected)
        print("Passed Test case 6: Matrix with a single column") 
    
    def test_1x1_matrix(self):
        matrix = [[42]]
        expected = [42]
        self.assertEqual(self.solution(matrix), expected)
        print("Passed Test case 7: 1x1 matrix") 
    
    def test_matrix_with_zero_values(self):
        matrix = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(self.solution(matrix), expected)
        print("Passed Test case 9: Matrix with zero values")

if __name__ == '__main__':
    unittest.main()
