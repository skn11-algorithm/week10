# 백도어
import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sight = list(map(int, input().split()))
sight[-1] = 0

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, input().split())
    if sight[a] == 0 and sight[b] == 0:
        graph[a].append((b, t))
        graph[b].append((a, t))

INF = float('inf')
dist = [INF] * n
dist[0] = 0
q = [(0, 0)]

while q:
    cost, now = heapq.heappop(q)
    if cost > dist[now]:
        continue
    for nxt, c in graph[now]:
        if dist[nxt] > cost + c:
            dist[nxt] = cost + c
            heapq.heappush(q, (dist[nxt], nxt))

print(dist[n - 1] if dist[n - 1] != INF else -1)
