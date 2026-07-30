class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # state = [0]*numCourses
        # print(state)
        indegree= {i:[] for i in range(numCourses)}
        for src, dest in prerequisites:
            indegree[src].append(dest)
        visited = set()
        completed = set()
        def dfs(src):
            if src in visited:
                return False
            if src in completed:
                return True
            visited.add(src)
            for dest in indegree[src]:
                if not dfs(dest):
                    return False
            visited.remove(src)
            completed.add(src)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True