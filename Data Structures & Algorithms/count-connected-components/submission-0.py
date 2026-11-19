class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        visited = [False] * n
        adj = [[] for _ in range(n)]
        
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        def dfs(node):

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)

        count = 0
        for i in range(len(visited)):
            if not visited[i]:
                count += 1
                visited[i] = True
                dfs(i)
        
        return count
