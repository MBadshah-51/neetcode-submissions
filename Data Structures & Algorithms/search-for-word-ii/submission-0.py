class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1
        self.refs = 0

class Solution:
    def __init__(self):
        self.node = TrieNode()
        self.ans = []

    def insertWord(self, word, i):
        temp = self.node
        temp.refs += 1
        for ch in word:
            if ch not in temp.children:
                temp.children[ch] = TrieNode()
            temp = temp.children[ch]
            temp.refs += 1
        temp.idx = i

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])

        for i, word in enumerate(words):
            self.insertWord(word, i)

        
        def searchWord(row, col, node):

            if row <0 or col < 0 or\
                row == rows or col == cols or \
                board[row][col] not in node.children:
                    return 0

            temp = board[row][col]
            board[row][col] = '#'
            prev = node
            node = node.children[temp]
            found = 0

            if node.idx != -1:
                self.ans.append(words[node.idx])
                node.idx = -1
                found += 1

            dx = [-1, 0, 1, 0]
            dy = [0, -1, 0, 1]

            for i in range(4):
                new_row = row + dx[i]
                new_col = col + dy[i]

                found += searchWord(new_row, new_col, node)

            board[row][col] = temp
            node.refs -= found
            if not node.refs:
                del prev.children[board[row][col]]

            return found

        for i in range(rows):
            for j in range(cols):
                if board[i][j] in self.node.children :
                    self.node.refs -= searchWord(i, j, self.node)
        
        return list(self.ans)
        


        