# 알고스팟
from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
dist = [[1e9] * m for _ in range(n)]
dq = deque()
dq.append((0, 0))
dist[0][0] = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

while dq:
    x, y = dq.popleft()
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            cost = dist[x][y] + graph[nx][ny]
            if cost < dist[nx][ny]:
                dist[nx][ny] = cost
                if graph[nx][ny] == 0:
                    dq.appendleft((nx, ny))
                else:
                    dq.append((nx, ny))

print(dist[n-1][m-1])