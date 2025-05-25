import sys
import heapq

input=sys.stdin.readline
INF=sys.maxsize
T=int(input().rstrip()) # 테스트 케이스
directions = [(-1,0), (1,0), (0,-1), (0,1)] 

for _ in range(T):
    K,W,H=map(int,input().rstrip().split()) # 클링온 전투선 클래스 개수, 평면의 폭, 평면 높이

    klingon={}
    # 클링온 클래스에 따른 무력화하는데 걸리는 시간
    for i in range(K):
        cls,down_time=input().rstrip().split()
        # 클래스(키) : 무력화시간(값)
        klingon[cls]=int(down_time)
    klingon["E"] = 0 

    # 클링온과 엔터프라이즈호 위치. 엔터프라이즈호 = E
    arr=[list(input().rstrip()) for _ in range(H)]
    
    # 무력화시간 담을 배열
    cost=[[INF]*W for _ in range(H)]

    # E 위치
    for i in range(H):
        for j,a in enumerate(arr[i]):
            if a=='E':
              E_node=(i,j)  
    
    # 다익스트라 ---------------------------------
    heap=[]
    heapq.heappush(heap,(0,E_node[0],E_node[1])) #무력화시간, 시작x,시작y
    cost[E_node[0]][E_node[1]]=0

    while heap:
        down,x,y=heapq.heappop(heap)

        if x==0 or x==H-1 or y==0 or y == W-1 :
            print(down)
            break

        # 새로운 비용보다 원래 비용이 적다면 continue
        if cost[x][y]<down:
            continue
        
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<H and 0<=ny<W:
                add_class=arr[nx][ny]
                new_down=down+klingon[add_class]
                if cost[nx][ny]>new_down:
                    cost[nx][ny]=new_down
                    heapq.heappush(heap,(new_down,nx,ny))


## EX) w=3, h=4
## 0,0 0,1 0,2
## 1,0 1,1 1,2
## 2,0 2,1 2,2
## 3,0 3,1 3,2
## 가장자리 : x==0 or x==H-1 or y==0 or y == W-1