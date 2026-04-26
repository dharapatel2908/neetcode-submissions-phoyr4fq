class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapping = {i:[] for i in range(numCourses)}
        for a, b in prerequisites:
            mapping[b].append(a)

        state = [0]* numCourses

        def dfs(course):
            if state[course] ==1:
                return False
            if mapping[course] == 2:
                return True
            
            state[course] =1
           
            for next_course in mapping[course]:
                if not dfs(next_course):
                    return False
            
            state[course] =2
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True