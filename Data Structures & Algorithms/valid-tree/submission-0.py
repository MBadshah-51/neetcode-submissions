class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        visited = [False] * n
        
        def dfs(node, parent):
            is_tree = True
            for neighbor in adj[node]:
                if neighbor != parent:
                    if visited[neighbor]:
                        return False
                    visited[neighbor] = True
                    is_tree = dfs(neighbor, node)
            return is_tree
        
        visited[0] = True
        is_tree = dfs(0,-1)

        for visit in visited:
            if not visit:
                return False
        
        return is_tree