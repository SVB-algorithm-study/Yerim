from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 시작이 1일때 예외처리
        if grid[0][0] == 1:
            return -1
        # 이동방향 - 십자, 대각선
        dx = [0, 0, 1, -1, 1, 1, -1, -1]
        dy = [1, -1, 0, 0, 1, -1, -1, 1]
        n = len(grid)
        # 거리계산
        visited = [[0]*n for _ in range(n)]
        visited[0][0] = 1
        queue = deque([(0,0)])
        while queue:
            x, y = queue.popleft()
            dist = visited[x][y]
            if (x, y) == (n-1, n-1):
                return dist
            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if grid[nx][ny] == 0 and visited[nx][ny] == 0:
                        visited[nx][ny] = dist+1
                        queue.append((nx,ny))
        return -1