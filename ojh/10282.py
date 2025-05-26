import sys
import heapq

input=sys.stdin.readline
INF=sys.maxsize

def dijkstra(start,distance):
    heap=[]
    heapq.heappush(heap,(0,start)) #전염시간, 시작 위치
    distance[start]=0

    while heap:
        time,x=heapq.heappop(heap)

        # 새로운 비용보다 원래 비용이 적다면 continue
        if distance[x]<time:
            continue
        
        for nx,t in connect[x]:   
            new_time=time+t
            if distance[nx]>new_time:
                distance[nx]=new_time
                heapq.heappush(heap,(new_time,nx))

T=int(input().rstrip()) # 테스트 케이스
for _ in range(T):
    n,d,c=map(int,input().rstrip().split()) # 컴퓨터 개수, 의존성 개수, 해킹당한 컴퓨터 번호
    
    connect=[[] for _ in range(n+1)]
    distance=[INF]*(n+1)

    for _ in range(d):
        a,b,s=map(int,input().rstrip().split()) # a가 b를 의존, s초후 a도 감염
        connect[b].append([a,s])

    dijkstra(c,distance)
    cnt=0
    ans=0
    for i in distance:
        if i!=INF:
            cnt+=1
            ans=max(ans,i)
    print(cnt,ans)
   

