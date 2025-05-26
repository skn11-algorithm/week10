'''
백도어
입력 : 분기점 수 N 분기점 잇는 길 수 M / 분기점 적이 시야에 보이는지 0 1 / 정수 a b t ( a b 지나는 시간 t)
출력 : 안들키고 가는 시간
아이디어 : 출발지와 도착지가 하나씩으로 정해져있고 최단 거리를 찾는 문제 -> 다익스트라!


'''

import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline

N,M = map(int, input().split())
arr = list(map(int, input().strip().split()))
arr[-1] = 0 # 넥서스에는 방문이 가능함 

# 양방향 그래프
connect = [[] for _ in range(N)]
for i in range(M):
    a, b, t = map(int, input().split())
    connect[a].append((t, b))
    connect[b].append((t, a))


def dijkstra(start, end):
    dis_list = [INF for _ in range(N)]
    dis_list[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        dis, node = heapq.heappop(pq)
        #갱신된 게 이미 더 작을 경우에는 넘어감
        if dis > dis_list[node]:
            continue

        # 다음 노드의 거리가 새롭게 생긴 다음 노드의 거리보다 크고 /// 다음 노드가 방문할 수 있는 노드인 경우에 거리 업데이트하고 pq에 넣어줌
        for next_cost, next_node in connect[node]:
            if dis_list[next_node] > dis_list[node]+next_cost and not arr[next_node]:
                dis_list[next_node] = dis_list[node]+next_cost
                heapq.heappush(pq, (dis_list[next_node], next_node))

    #print(dis_list)
    return dis_list[end]

num = dijkstra(0, N-1)
if num==INF:
    print(-1)
else:
    print(num)