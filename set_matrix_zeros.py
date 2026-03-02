class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows=len(matrix)
        cols=len(matrix[0])
        zeros=[]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    zeros.append((i,j))
        for i,j in zeros:
            for col in range(cols):
                matrix[i][col]=0
            for row in range(rows):
                matrix[row][j]=0
