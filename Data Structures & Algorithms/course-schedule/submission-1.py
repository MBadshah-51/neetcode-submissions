class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0] * numCourses

        adj = [[] for _ in range(numCourses)]

        from collections import deque
        que = deque()

        for edge in prerequisites:
            inDegree[edge[1]] += 1
            adj[edge[0]].append(edge[1])
        
        for i in range(numCourses):
            if inDegree[i] == 0:
                que.append(i)
        
        count = 0
        while que:
            subject = que.popleft()
            count += 1

            for x in adj[subject]:
                inDegree[x] -= 1
                if inDegree[x] == 0:
                    que.append(x)

        if count == numCourses:
            return True
        return False


