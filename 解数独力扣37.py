import pysnooper

class Solution(object):
    def solveSudoku(self, board):
        def check(i, j): #已经在该处放入了某值，然后check此行此列此块
            checkList = []
            for c in board[i]:
                if c.isdigit() and c in checkList:
                    return False
                else:
                    checkList.append(c)
            checkList = []
            for ii in range(9):
                c = board[ii][j]
                if c.isdigit() and c in checkList:
                    return False
                else:
                    checkList.append(c)
            checkList = []
            for ii in range(i//3 * 3, i//3*3+3):
                for jj in range(j//3*3, j//3*3+3):
                    c = board[ii][jj]
                    if c.isdigit() and c in checkList:
                        return False
                    else:
                        checkList.append(c)
            return True

        def choices(i, j): #输出一个list，里面含可供选用的数字的字符, ['1','5']
            result = []
            if board[i][j] != '.': #说明已经有数字了
                return result
            result = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            for c in board[i]:  #行
                if c in result:
                    result.remove(c)
            for ii in range(9):  #列
                c = board[ii][j]
                if c in result:
                    result.remove(c)
            for ii in range(3): #块
                for jj in range(3):
                    c = board[ii+i//3*3][jj+j//3*3]
                    if c in result:
                        result.remove(c)
            return result



        ''' 检验整个board是否合法
        for i in range(9):
            for j in range(9):
                if not check(i, j):
                    print( i, j, False)
        '''
        ''' 检验choice函数是否正常
        print(choice(1,6))
        '''



sol = Solution()
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
sol.solveSudoku(board)

