'''
알고스팟 - 상하좌우 미로 뚫어 탈출!!!
입력 : 미로크기 가로M 세로 N / 미로의 상태를 나타내는 0(빈방) 1(벽)
출력 : 도착지까지 이동할 때 부숴야 하는 벽의 '최소' 개수
아이디어 : 가중치 0 또는 1인 최단 경로 탐색? -> 우선순위 큐 사용해서 최솟값 뽑기

출발은 (1,1) 도착은 (n,m)
'''

import sys
import heapq
input = sys.stdin.readline

m, n = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]
minist_destroy = [[float('inf')] * m for _ in range(n)]  

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dijkstra():
    heap = [] # 최소 힙으로 비용, 위치 저장
    heapq.heappush(heap, (0, 0, 0))  # (여태 부순 벽 수, x, y)
    minist_destroy[0][0] = 0

    while heap:
        cost, x, y = heapq.heappop(heap)

        if minist_destroy[x][y] < cost:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m: # 미로 안쪽 좌표에서 
                ncost = cost + maze[nx][ny]  # 벽이면 1, 아니면 0 추가

                if ncost < minist_destroy[nx][ny]:
                    minist_destroy[nx][ny] = ncost
                    heapq.heappush(heap, (ncost, nx, ny))

dijkstra()
print(minist_destroy[n-1][m-1])
