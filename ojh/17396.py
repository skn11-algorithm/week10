import sys
import heapq

input=sys.stdin.readline

INF=sys.maxsize
N,M=map(int,input().rstrip().split()) 
arr = list(map(int, input().rstrip().split()))
arr[-1] = 0 # 편의상 마지막 분기점을 0

# 양방향 그래프 연결
connect = [[] for _ in range(N)]
for i in range(M):
    a, b, t = map(int, input().split())
    connect[a].append((t, b))
    connect[b].append((t, a))

def dijkstra(start, end):
    distance = [INF for _ in range(N)]
    distance[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        dis, node = heapq.heappop(pq)
 
        if dis > distance[node]:
            continue

        for next_cost, next_node in connect[node]:
            if distance[next_node] > distance[node]+next_cost and not arr[next_node]:
                distance[next_node] = distance[node]+next_cost
                heapq.heappush(pq, (distance[next_node], next_node))

    return distance[end]

num = dijkstra(0, N-1)
if num==INF:
    print(-1)
else:
    print(num)