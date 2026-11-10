class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]

        ans = 0

        def bfs(i, j):

            from collections import deque
            que = deque()
            que.append((i, j))

            drow = [0, -1, 0, 1]
            dcol = [-1, 0, 1, 0]

            while que:
                row, col = que.popleft()

                for x in range(4):
                    new_row = row + drow[x]
                    new_col = col + dcol[x]

                    if 0 <= new_row < m and 0 <= new_col < n \
                        and grid[new_row][new_col] == "1" \
                        and not visited[new_row][new_col]:

                        visited[new_row][new_col] = True
                        que.append((new_row, new_col))
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and \
                    not visited[i][j]:
                    visited[i][j] = True
                    ans += 1
                    bfs(i, j)
        
        return ans




