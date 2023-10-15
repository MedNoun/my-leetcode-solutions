class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(3):
            for j in range(3):
                occ = {}
                for k in range(i*3,i*3+3):
                    for m in range(j*3,j*3+3):
                        num = board[k][m]
                        element = occ.get(num)
                        if(element and num != "."):
                            return False
                        else:
                            occ[num] = 1  
        for line in board:
            occ = {}
            for el in line:
                element = occ.get(el)
                if(element and el != "."):
                    return False
                else:
                    occ[el] = 1
        for col in zip(*board):
            occ = {}
            for el in col:
                element = occ.get(el)
                if(element and el != "."):
                    return False
                else:
                    occ[el] = 1 
        
        return True  