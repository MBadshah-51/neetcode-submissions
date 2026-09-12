class Solution:
    def wordExists(self, board, word, row, col, index):
        if word[index] != board[row][col]:
            return False

        if index == len(word) - 1:
            return True

        temp = board[row][col]
        board[row][col] = "#"

        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]

        for i in range(4):
            nrow = row + dx[i]
            ncol = col + dy[i]

            if 0 <= nrow < len(board) and 0 <= ncol < len(board[0]) \
                and board[nrow][ncol] != "#":
                if self.wordExists(board, word, nrow, ncol, index + 1):
                    board[row][col] = temp
                    return True
        
        board[row][col] = temp
        return False
        

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] \
                    and self.wordExists(board, word, i, j, 0):
                    return True
        
        return False
                
                