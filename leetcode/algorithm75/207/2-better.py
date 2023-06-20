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
            
        countcycle = set() # check cycle ---- SET IS SIGNIFICANTLY FASTER THAN LIST FOR CHECKING IF "AN OBJECT IS PRESENT IN THE SET" -> O(1)

        def dfs(i):
            if i in countcycle: # cycle!
                return False

            countcycle.add(i)

            for nxt in graph[i]:
                if not dfs(nxt):
                    return False

            countcycle.remove(i)
            graph[i] = []
            return True # checked every edge -> no cycle
        
        for i in range(numCourses):
            if not dfs(i):
                return False
                
        return True





