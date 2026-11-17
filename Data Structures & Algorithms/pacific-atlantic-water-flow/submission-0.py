class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pac, atl = set(), set()

        def dfs( r, c, visit, prevHeight):

            if ((r,c) in visit or r < 0 or
                c < 0 or r== rows or c == cols or
                heights[r][c] < prevHeight):
                return 
            
            visit.add((r,c))
            
            dx = [0, 1, 0, -1]
            dy = [1, 0, -1, 0]

            for i in range(4):
                dfs(r + dx[i], c + dy[i], visit, heights[r][c])
        
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])
        
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows-1][c])
        
        res = []

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        
        return res