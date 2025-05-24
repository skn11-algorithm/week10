import sys
import heapq

input=sys.stdin.readline
INF=int(1e9)
N,M=map(int,input().rstrip().split()) # 지하철역 수, 도착지

company=[]
for _ in range(N):
    company.append(int(input().rstrip()))
subway=[list(map(int,input().rstrip().split())) for _ in range(N)]

# (환승 횟수, 시간, 현재역, 현재 회사) 우선순위 큐
heap=[]
heapq.heappush(heap,(0,0,0,company[0]))

# 방문 체크: [역][회사] = (환승 수, 최소 시간)
visited = [[(INF, INF) for _ in range(2)] for _ in range(N)]
visited[0][company[0]] = (0, 0)

while heap:
    transfers, time, node, current_company = heapq.heappop(heap)
    
    # 목적지 도달 시 바로 출력
    if node == M:
        print(transfers, time) # 환승횟수, 총비용
        break
    
    for next_node in range(N):
        move_time = subway[node][next_node]
        if move_time == 0:
            continue  # 연결 안 된 경우
        
        next_company = company[next_node]
        next_transfers = transfers + (current_company != next_company)
        next_time=time+move_time 
           
          # 기존 방문 기록보다 환승 수가 적거나, 같고 시간이 짧을 경우에만 진행
        if visited[next_node][next_company][0] > next_transfers or (
            visited[next_node][next_company][0] == next_transfers and
            visited[next_node][next_company][1] > next_time
        ):
            visited[next_node][next_company] = (next_transfers, next_time)
            heapq.heappush(heap, (next_transfers, next_time, next_node, next_company))
