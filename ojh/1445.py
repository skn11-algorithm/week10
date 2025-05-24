import sys
import heapq

input=sys.stdin.readline


# ── 입력 ──────────────────────────────────
N,M=map(int,input().rstrip().split()) # 세로크기(행),가로크기(열)
arr=[list(input().rstrip()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j]=='F': fx,fy=i,j
        elif arr[i][j]=='S': sx,sy=i,j

# ── 쓰레기 인접 여부 미리 표시 ────────────────
near=[[False]*M for _ in range(N)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]

for x in range(N):
    for y in range(M):
        if arr[x][y]=='g':
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<N and 0<=ny<M :
                    if arr[nx][ny] in ['.', 'S', 'F']:
                        near[nx][ny]=True 

# ── 다익스트라 ──────────────────────────────
INF=(1e8,1e8)
distance = [[INF]*M for _ in range(N)]
heap=[]
heapq.heappush(heap,(0,0,sx,sy)) # g 개수, 인접g개수, x(행), y(열)
distance[sx][sy] = (0,0)

while heap:
    gCnt,aCnt,x,y=heapq.heappop(heap)
    if (gCnt,aCnt)>distance[x][y]:
        continue

    if (x,y) == (fx,fy): # 도착
        break

    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<N and 0<=ny<M :
            if arr[nx][ny] == 'g' :
                addG=1
            else:
                addG=0
            
            addA=0
            
            if arr[nx][ny] not in ['S', 'F'] and near[nx][ny]:
                addA = 1

            new_gCnt=gCnt+addG
            new_aCnt=aCnt+addA

            if (new_gCnt,new_aCnt)<distance[nx][ny]:
                distance[nx][ny]=(new_gCnt,new_aCnt)
                heapq.heappush(heap,(new_gCnt,new_aCnt,nx,ny))
                
print(*distance[fx][fy])