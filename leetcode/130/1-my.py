class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        visited = [[False]*n for _ in range(m)]
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        lst = [] # 뒤집을 리스트. 

        def dfs(x, y):
            # ok : 뒤집어도 되는 지
            ok = True
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if nx<0 or nx>=m or ny<0 or ny>=n: # 뒤집기 불가
                    del lst[:]
                    ok = False
                elif board[nx][ny] == "O" and not visited[nx][ny]:
                    visited[nx][ny] = True
                    lst.append((nx, ny))
                    ok &= dfs(nx, ny)
            return ok

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    if not visited[i][j]:
                        visited[i][j] = True
                        del lst[:]
                        lst.append((i, j))
                        if dfs(i, j):
                            for (x, y) in lst:
                                board[x][y] = "X"
        return board