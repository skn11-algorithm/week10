import sys
import heapq
input = sys.stdin.readline

def solve():
    # 입력 받기
    N, M = map(int, input().split())
    
    # 각 역을 운영하는 회사 정보
    companies = []
    for _ in range(N):
        companies.append(int(input()))
    
    # 역 간의 연결 정보 및 시간
    graph = []
    for i in range(N):
        row = list(map(int, input().split()))
        graph.append(row)
    
    # 다익스트라를 위한 거리 배열
    # dist[i] = (환승횟수, 소요시간)
    dist = [(float('inf'), float('inf'))] * N
    dist[0] = (0, 0)  # 출발지는 환승 0회, 시간 0
    
    # 우선순위 큐: (환승횟수, 소요시간, 현재역)
    pq = [(0, 0, 0)]
    
    while pq:
        transfer_cnt, time, current = heapq.heappop(pq)
        
        # 이미 더 좋은 경로가 있다면 건너뛰기
        if (transfer_cnt, time) > dist[current]:
            continue
        
        # 목적지에 도달했다면 결과 반환
        if current == M:
            return transfer_cnt, time
        
        # 인접한 모든 역 확인
        for next_station in range(N):
            if graph[current][next_station] > 0:  # 연결되어 있는 경우
                # 다음 역으로 이동하는 시간
                next_time = time + graph[current][next_station]
                
                # 환승 여부 확인
                next_transfer_cnt = transfer_cnt
                if companies[current] != companies[next_station]:
                    next_transfer_cnt += 1
                
                # 더 좋은 경로인지 확인
                if (next_transfer_cnt, next_time) < dist[next_station]:
                    dist[next_station] = (next_transfer_cnt, next_time)
                    heapq.heappush(pq, (next_transfer_cnt, next_time, next_station))
    
    return dist[M]

# 결과 출력
transfer_cnt, total_time = solve()
print(transfer_cnt, total_time)




# 이 문제는 "지하철" 문제로, 환승 횟수를 최소화하고 그 중에서 시간이 가장 짧은 경로를 찾는 문제입니다.
# 문제 분석:

# N개의 지하철역, 0번에서 M번으로 이동
# 각 역은 A회사(0) 또는 B회사(1)가 운영
# 환승: 다른 회사의 역으로 이동할 때마다 1회
# 목표: 환승 횟수 최소, 그 중에서 소요시간 최소

# 이 문제는 우선순위가 있는 다익스트라 알고리즘으로 해결할 수 있습니다. (환승 횟수, 소요시간)을 상태로 관리하여 환승 횟수를 우선적으로 최소화하고, 같은 환승 횟수라면 시간을 최소화합니다.지하철 (백준 17940) - 우선순위 다익스트라 풀이코드 import sys
# import heapq
# input = sys.stdin.readline

# def solve():
#     # 입력 받기
#     N, M = map(int, input().split())
    
#     # 각 역을 운영하는 회사 정보
#     companies = []
#     for _ in range(N):
#         companies.append(int(input()))
    
#     # 역 간의 연결 정보 및 시간
#  해결 방법 설명:

# 우선순위 다익스트라: (환승횟수, 소요시간) 튜플을 사용하여 환승횟수를 우선적으로 최소화
# 상태 관리:

# dist[i] = (환승횟수, 소요시간): 각 역까지의 최적 경로 정보
# 우선순위 큐에서 환승횟수가 작은 것을 먼저 처리


# 환승 판단:

# 현재 역과 다음 역의 운영 회사가 다르면 환승 1회 추가
# companies[current] != companies[next_station]


# 경로 비교:

# Python의 튜플 비교를 활용: (환승횟수, 시간) 순으로 비교
# 환승횟수가 적으면 우선, 같으면 시간이 적은 것 선택



# 시간 복잡도: O(N² log N)
# 공간 복잡도: O(N²)
# 핵심 아이디어:

# 일반적인 최단경로 문제와 달리 두 가지 기준(환승횟수, 시간)을 동시에 고려
# 환승횟수가 우선순위이므로 튜플의 첫 번째 요소로 배치
# 다익스트라 알고리즘의 완화 조건을 (환승횟수, 시간) 튜플 비교로 변경