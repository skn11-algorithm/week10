'''
지하철 ⭐⭐⭐
입력 : 지하철역수 N 도착지 번호 M / 회사정보 0(a)또는 1(b) / 지하철역 연결상태 0인경우 연결x 이상이면 이동시간
출력 : 최적경로 시 환승 횟수, 총 소요 시간 
아이디어 : 최적경로? 조건이 2개인 다익스트라 
'''

import sys
import heapq
INF = sys.maxsize

input = sys.stdin.readline
TRANSFER_WEIGHT = 10**6  # 환승 시 우선순위를 뒤로 밀기 위한 큰 값

def dijkstra(start, end, n, graph, company):
    # 각 역까지의 최소 환승 횟수와 최소 소요 시간 초기화
    min_transfer = [INF] * n
    min_time = [INF] * n

    min_transfer[start] = 0
    min_time[start] = 0

    # 우선순위 큐: (환승 횟수, 소요 시간, 현재 역)
    pq = []
    heapq.heappush(pq, (0, 0, start))

    while pq:
        transfers, time, station = heapq.heappop(pq)

        # 더 나은 경로가 이미 있다면 무시
        if transfers > min_transfer[station]:
            continue
        if transfers == min_transfer[station] and time > min_time[station]:
            continue

        # 연결된 역들 확인
        for cost, next_station in graph[station]:
            # 환승이 발생하는 경우, 소요 시간에 큰 값을 추가해서 우선순위 밀기
            is_transfer = company[station] != company[next_station]
            total_time = time + cost + (TRANSFER_WEIGHT if is_transfer else 0)
            total_transfers = transfers + (1 if is_transfer else 0)

            # 새로운 경로가 더 좋은 경우 갱신
            if total_transfers < min_transfer[next_station]:
                min_transfer[next_station] = total_transfers
                min_time[next_station] = total_time
                heapq.heappush(pq, (total_transfers, total_time, next_station))
            elif total_transfers == min_transfer[next_station] and total_time < min_time[next_station]:
                min_time[next_station] = total_time
                heapq.heappush(pq, (total_transfers, total_time, next_station))

    return min_transfer[end], min_time[end]

def solve():
    n, m = map(int, input().split())
    company = [int(input()) for _ in range(n)]

    # 인접 리스트로 그래프 구성 (연결된 역과 시간)
    graph = [[] for _ in range(n)]
    for i in range(n):
        times = list(map(int, input().split()))
        for j in range(n):
            if times[j] > 0:
                graph[i].append((times[j], j))

    # 다익스트라 실행
    transfers, total_time = dijkstra(0, m, n, graph, company)

    if transfers == INF:
        print(-1)  # 도달 불가능
    else:
        print(transfers, total_time % TRANSFER_WEIGHT)  # 환승 횟수, 실제 소요 시간 출력

# 실행
if __name__ == "__main__":
    solve()
