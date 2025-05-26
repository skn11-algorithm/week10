from collections import deque
n,m = map(int,input().split())
data = []
for i in range(m):
    data.append(list(map(int,input())))
visited = [[-1] * n for i in range(m)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 0

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] == -1:
                if data[nx][ny] == 1:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
                else:
                    q.appendleft((nx,ny))
                    visited[nx][ny] = visited[x][y]
        
bfs(0,0)
print(visited[m-1][n-1])