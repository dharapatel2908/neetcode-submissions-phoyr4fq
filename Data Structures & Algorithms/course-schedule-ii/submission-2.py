class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = {i:[] for i in range(numCourses)}
        for src,dest in prerequisites:
            indegree[src].append(dest)
        visited = set()
        completed = set()
        result =[]
    
        def dfs(src):
            
            if src in visited:
               
                return False
            if src in completed:
                return True
            visited.add(src)
            for dest in  indegree[src]:
                if not dfs(dest):
                    
                    return False
            visited.remove(src)
            completed.add(src)
            result.append(src)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return result
            


