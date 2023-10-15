class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        last=len(matrix)-1
        for l in range(0,last//2+1):
            for c in range(l,last - l):
                moving = matrix[l][c]
                for i in range(4):
                    l,c = c,last-l
                    to = matrix[l][c]
                    matrix[l][c] = moving
                    moving = to