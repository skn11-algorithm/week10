import sys
import heapq

input=sys.stdin.readline

INF=1e8
M,N=map(int,input().rstrip().split()) # 가로크기(열), 세로크기(행)
arr=[list(map(int, input().rstrip())) for _ in range(N)]

dx=[1,0,-1,0]
dy=[0,1,0,-1]

distance = [[INF]*M for _ in range(N)]
heap=[]
heapq.heappush(heap,(0,0,0)) # 비용, x(행), y(열)
distance[0][0] = 0

while heap:
    cost,x,y=heapq.heappop(heap)

    if distance[x][y]<cost:
        continue

    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<N and 0<=ny<M :
            new_cost=cost+arr[nx][ny]
            if new_cost<distance[nx][ny]:
                distance[nx][ny]=new_cost
                heapq.heappush(heap,(new_cost,nx,ny))
                
print(distance[N-1][M-1])
                


