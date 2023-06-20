class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        ans = 0

        def dfs(x, y):
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if 0<=nx<m and 0<=ny<n:
                    if grid[nx][ny]=="1" and not visited[nx][ny]:
                        visited[nx][ny] = True
                        dfs(nx, ny)

        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and not visited[i][j]:
                    visited[i][j] = True
                    ans += 1
                    dfs(i, j)
        return ans