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


import sys
import heapq
input = sys.stdin.readline

m, n = map(int, input().split()) # 1. 미로의 가로 세로 길이를 받아주고 
maze = [list(map(int, input().strip())) for _ in range(n)] #2. 열 기준으로 행의 요소 하나하나씩 미로 정보를 받습니다.
minist_destroy = [[float('inf')] * m for _ in range(n)]  #3. 최소로 부순 벽의 개수는 나중에 업데이트 하기 위해 무한대로 초기화 

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dijkstra():
    heap = [] # 4. 최소 힙으로 비용, 위치 저장하도록 배열 만들어줌
    heapq.heappush(heap, (0, 0, 0))  # 5. 시작점을 q에 넣기 (여태 부순 벽 수, x, y)
    minist_destroy[0][0] = 0 # 6. 0,0 까지 벽을 0개 부쉈다고 초기화 

    while heap: # 6. 적게 부순 경로부터 우선 탐색을 시작 
        cost, x, y = heapq.heappop(heap)

        if minist_destroy[x][y] < cost: # 7. 만약 최소 값보다 많은 벽을 부수면 무시하고 코드진행
            continue

        for i in range(4): # 8. (i가 0~3까지 탐색하며) 상하좌우 탐색  
            nx = x + dx[i] 
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m: # 9. 미로 안쪽 좌표, 즉 n*m 에서만 탐색하는 조건 내에서 
                newcost = cost + maze[nx][ny]  # 배열값이 1 부수는 비용 그대로 1, 아니면 0 추가

                if newcost < minist_destroy[nx][ny]: # 10. 부수는거에 따라 최소한 벽 부순 횟수 업데이트 해줍니다 
                    minist_destroy[nx][ny] = newcost
                    heapq.heappush(heap, (newcost, nx, ny))

dijkstra()
print(minist_destroy[n-1][m-1]) # 11. 배열값이기 때문에 출력은 -1 해서 벽 부순 최소횟수를 구해줍니다!!
