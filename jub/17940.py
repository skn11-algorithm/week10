import heapq
INF = int(1e9)
BASE = 10**6

def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist <= distance[now]:
            for pos, c in graph[now]:
                cost = dist + c

                if cost < distance[pos]:
                    distance[pos] = cost
                    heapq.heappush(q, (cost, pos))


N, M = map(int, input().split())
company = [int(input()) for _ in range(N)]
tmp = [list(map(int, input().split())) for _ in range(N)]
graph = [[] * N for _ in range(N)]
result = [[] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if tmp[i][j] != 0:
            if company[i] == company[j]:
                graph[i].append((j, tmp[i][j]))
            else:
                graph[i].append((j, tmp[i][j] + BASE))

distance = [INF for _ in range(N)]

dijkstra(0, distance)

count, time = distance[M] // BASE, distance[M] % BASE
print(count, time)
