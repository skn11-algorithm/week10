# 해킹
import heapq
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))  # b → a
    
    dist = [float('inf')] * (n + 1)
    dist[c] = 0
    hq = [(0, c)]

    while hq:
        time, now = heapq.heappop(hq)
        if dist[now] < time:
            continue
        for nxt, t in graph[now]:
            if dist[nxt] > time + t:
                dist[nxt] = time + t
                heapq.heappush(hq, (dist[nxt], nxt))
    
    cnt = sum(1 for x in dist if x != float('inf'))
    max_time = max([x for x in dist if x != float('inf')])
    print(cnt, max_time)
