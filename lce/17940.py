# 지하철
import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
company = [int(input()) for _ in range(n)]
graph = [[] for _ in range(n)]
for i in range(n):
    times = list(map(int, input().split()))
    for j in range(n):
        if times[j] != 0:
            graph[i].append((j, times[j]))

INF = float('inf')
dist = [[INF, INF] for _ in range(n)]  # [환승 횟수, 소요 시간]
dist[0] = [0, 0]
pq = []
heapq.heappush(pq, (0, 0, 0))  # (환승 횟수, 소요 시간, 현재 역)

while pq:
    cnt, time, now = heapq.heappop(pq)
    if dist[now][0] < cnt or (dist[now][0] == cnt and dist[now][1] < time):
        continue
    for nxt, t in graph[now]:
        next_cnt = cnt + (company[now] != company[nxt])
        next_time = time + t
        if dist[nxt][0] > next_cnt or (dist[nxt][0] == next_cnt and dist[nxt][1] > next_time):
            dist[nxt] = [next_cnt, next_time]
            heapq.heappush(pq, (next_cnt, next_time, nxt))

print(dist[m][0], dist[m][1])
