# PROJECT 4 Tests
#
# Name: Tyra Krivonak and Shriya Nimmagadda
# S. Einakian

import unittest
from calcdoku import validate_cols, validate_rows, transpose, validate_cages, validate_all

class TestFuncs(unittest.TestCase):
    
    def test_transpose(self):
        grid1 = [[1,3,4,2,5],[1,2,3,4,5],[1,1,1,3,3],[5,4,3,2,2],[1,2,3,5,4]]
        col = transpose(grid1)
        self.assertListEqual(col,[[1,1,1,5,1],[3,2,1,4,2],[4,3,1,3,3],[2,4,3,2,5],[5,5,3,2,4]])

        grid2 = [[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4],[5,5,5,5,5]]
        col = transpose(grid2)
        self.assertListEqual(col,[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])

        grid3 = [[1,2,3,4,5],[2,3,4,5,1],[3,4,5,1,2],[4,5,1,2,3],[5,1,2,3,4]]
        col = transpose(grid3)
        self.assertListEqual(col, [[1,2,3,4,5],[2,3,4,5,1],[3,4,5,1,2],[4,5,1,2,3],[5,1,2,3,4]])

    def test_validate_rows(self):
        grid1 = [[1,3,4,2,5],[1,2,3,4,5],[1,1,1,3,3],[5,4,3,2,2],[1,2,3,5,4]]
        self.assertFalse(validate_rows(grid1))
        
        grid2 = [[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4],[5,5,5,5,5]]
        self.assertFalse(validate_rows(grid2))

        grid3 = [[1,2,3,4,5],[2,3,4,5,1],[3,4,5,1,2],[4,5,1,2,3],[5,1,2,3,4]]
        self.assertTrue(validate_rows(grid3))
        
    def test_validate_cols(self):
        grid1 = [[1,3,4,2,5],[1,2,3,4,5],[1,1,1,3,3],[5,4,3,2,2],[1,2,3,5,4]]
        self.assertFalse(validate_cols(grid1))
        
        grid2 = [[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4],[5,5,5,5,5]]
        self.assertTrue(validate_cols(grid2))

        grid3 = [[1,2,3,4,5],[2,3,4,5,1],[3,4,5,1,2],[4,5,1,2,3],[5,1,2,3,4]]
        self.assertTrue(validate_cols(grid3))

    def test_validate_cages(self):
        grid1 = [[3,5,2,1,4],[5,1,3,4,2],[2,4,1,5,3],[1,2,4,3,5],[4,3,5,2,1]]
        cages1 = [[9],[9,0,5,6],[7,1,2],[10,3,8,13],[14,4,9,14,19],[3,7],[8,10,11,16],[13,12,17,21,22],[5,15,20],[6,18,23,24]]
        self.assertTrue(validate_cages(grid1, cages1))

        grid2 = [[1,2,3,4,4],[3,1,4,5,2],[2,5,1,3,4],[5,4,2,1,3],[4,3,5,2,1]]
        cages2 =[[7],[4,0,1,6],[8,2,7,12],[14,3,4,8],[15,5,10,11,15],[14,9,13,14,18,19,24],[11,16,20,21],[9,17,22,23]]
        self.assertFalse(validate_cages(grid2, cages2))

        grid3 = [[1,2,3,4,5],[3,1,4,5,2],[2,5,1,3,4],[5,4,2,1,3],[4,3,5,2,1]]
        cages3 =[[7],[4,0,1,6],[8,2,7,12],[14,3,4,8],[15,5,10,11,15],[14,9,13,14,18,19,24],[11,16,20,21],[9,17,22,23]]
        self.assertTrue(validate_cages(grid3, cages3))

    def test_validate_all(self):
        grid1 = [[3,5,2,1,4],[5,1,3,4,2],[2,4,1,5,3],[1,2,4,3,5],[4,3,5,2,1]]
        cages1 = [[9],[9,0,5,6],[7,1,2],[10,3,8,13],[14,4,9,14,19],[3,7],[8,10,11,16],[13,12,17,21,22],[5,15,20],[6,18,23,24]]
        self.assertTrue(validate_all(grid1, cages1))
        
        grid2 = [[1,2,3,4,4],[3,1,4,5,2],[2,5,1,3,4],[5,4,2,1,3],[4,3,5,2,1]]
        cages2 =[[7],[4,0,1,6],[8,2,7,12],[14,3,4,8],[15,5,10,11,15],[14,9,13,14,18,19,24],[11,16,20,21],[9,17,22,23]]
        self.assertFalse(validate_all(grid2, cages2))        
        
        grid3 = [[1,2,3,4,5],[3,1,4,5,2],[2,5,1,3,4],[5,4,2,1,3],[4,3,5,2,1]]
        cages3 =[[7],[4,0,1,6],[8,2,7,12],[14,3,4,8],[15,5,10,11,15],[14,9,13,14,18,19,24],[11,16,20,21],[9,17,22,23]]
        self.assertTrue(validate_all(grid3, cages3))
        
if __name__ == '__main__':
   unittest.main()
