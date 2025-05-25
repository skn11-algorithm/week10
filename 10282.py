'''
해킹
입력 : 테스트 케이스 수 T /N (컴퓨터 수), D (의존성 개수), C (해킹 시작 컴퓨터) D개의 줄에 a b s (b가 a를 감염시키는데 s초 걸림)
출력 : 마지막 컴퓨터가 감염되는 데 걸리는 시간 (최대 소요 시간)
아이디어 : 역방향 그래프???? 다익스트라 알고리즘

'''

import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = sys.maxsize  

def dijkstra(start_node, distances, graph):
    # 시작 노드를 우선순위 큐에 넣고 거리 0으로 초기화
    heap = []
    heappush(heap, (0, start_node))
    distances[start_node] = 0

    while heap:
        current_time, current_node = heappop(heap)

        # 현재 노드에서 갈 수 있는 모든 인접 노드 탐색
        for next_node, time_needed in graph[current_node]:
            new_time = current_time + time_needed

            # 현재 저장된 거리보다 더 짧으면 갱신하고 큐에 넣기
            if new_time < distances[next_node]:
                distances[next_node] = new_time
                heappush(heap, (new_time, next_node))


test_cases = int(input())

for _ in range(test_cases):
    n, d, c = map(int, input().split())

    graph = [[] for _ in range(n + 1)]  # 인접 리스트 그래프 (1번부터 n번까지)
    distances = [INF] * (n + 1)         # 각 컴퓨터까지 걸리는 최소 시간 초기화

    # 의존성 정보 입력
    for _ in range(d):
        a, b, s = map(int, input().split())
        # b -> a로 해킹 전파 가능하며 s초 걸림
        graph[b].append((a, s))

    dijkstra(c, distances, graph)

    infected_count = 0
    max_time = 0

    # 감염된 컴퓨터 개수와 가장 늦게 감염된 시간 계산
    for time in distances:
        if time != INF:
            infected_count += 1
            if time > max_time:
                max_time = time

    print(infected_count, max_time)
