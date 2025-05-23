# 일요일의 데이트
import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
dist = [[[float('inf')] * m for _ in range(n)] for _ in range(2)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

from collections import deque
garbage_near = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == '.':
            for d in range(4):
                ni, nj = i + dx[d], j + dy[d]
                if 0 <= ni < n and 0 <= nj < m:
                    if graph[ni][nj] == 'g':
                        garbage_near[i][j] = 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'S':
            start = (i, j)
        elif graph[i][j] == 'F':
            finish = (i, j)

heap = []
heapq.heappush(heap, (0, 0, start[0], start[1]))
visited = [[(float('inf'), float('inf')) for _ in range(m)] for _ in range(n)]
visited[start[0]][start[1]] = (0, 0)

while heap:
    g, ng, x, y = heapq.heappop(heap)
    if (x, y) == finish:
        print(g, ng)
        break
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            new_g = g
            new_ng = ng
            if graph[nx][ny] == 'g':
                new_g += 1
            elif garbage_near[nx][ny]:
                new_ng += 1
            if (new_g, new_ng) < visited[nx][ny]:
                visited[nx][ny] = (new_g, new_ng)
                heapq.heappush(heap, (new_g, new_ng, nx, ny))