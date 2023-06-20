class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 예외처리
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        n = len(grid)
        dirs = [[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0]]
        q = collections.deque()
        # 큐에 거리계산을 같이 넣어서 따로 배열 필요 없음.
        # 대신 왔던 곳도 다시 큐에 넣을 수 있을 듯.
        q.append((0,0,1))
        while len(q):
            x0, y0, cnt = q.popleft()
            if x0 == n-1 and y0 == n-1:
                return cnt
            for dx,dy in dirs:
                x = x0 + dx
                y = y0 + dy
                if x>=0 and x<n and y>=0 and y<n and grid[x][y]==0:
                    grid[x][y] = 1
                    q.append((x,y,cnt+1))
        return -1