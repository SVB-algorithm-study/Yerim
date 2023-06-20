class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        for p in prerequisites:
            graph[p[0]].append(p[1])
            
        visited = [False]*numCourses # if
        countcycle = [] # check cycle

        def dfs(i):
            if i in countcycle: # cycle!
                return False
            if visited[i]: # ith element is already proved to be not in a cycle
                return True
            countcycle.append(i)
            for nxt in graph[i]:
                if not dfs(nxt):
                    return False
            countcycle.pop()
            visited[i] = True
            return True # checked every edge -> no cycle
        
        for i in range(numCourses):
            # if not visited[i]:
            if not dfs(i):
                return False
        return True





