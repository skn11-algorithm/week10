import sys
import heapq

input = sys.stdin.readline
N,M = map(int, input().split())

arr = list(map(int, input().strip().split()))
arr[-1] = 0

INF = sys.maxsize

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
        if dis > dis_list[node]:
            continue
        for next_cost, next_node in connect[node]:
            if dis_list[next_node] > dis_list[node]+next_cost and not arr[next_node]:
                dis_list[next_node] = dis_list[node]+next_cost
                heapq.heappush(pq, (dis_list[next_node], next_node))

    return dis_list[end]

num = dijkstra(0, N-1)
if num==INF:
    print(-1)
else:
    print(num)