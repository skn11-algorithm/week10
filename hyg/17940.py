import sys, collections, heapq

def bfs():
    q = collections.deque()
    vis = [-1] * n
    q.append(0)
    vis[0] = 0
    while q:
        now  = q.popleft()
        for (next, next_dist) in adj1[now]:
            if vis[next] == -1:
                if arr[next] != arr[now]:
                    vis[next] = vis[now] + 1
                    q.append(next)
                else:
                    vis[next] = vis[now]
                    q.appendleft(next)
    return vis[m]

def dijkstra(num):
    inf = 9876543210
    
    d = [[inf] * (num + 1) for _ in range(n)]
    d[0][0] = 0
    q = []
    heapq.heappush(q, (0, 0, 0))
    while q:
        cur_dist, cur_cnt, cur = heapq.heappop(q)
        if d[cur][cur_cnt] < cur_dist:
            continue
        for (next, next_dist) in adj2[cur]:
            if arr[next] != arr[cur]:
                if cur_cnt + 1 <= num:
                    if d[next][cur_cnt + 1] > cur_dist + next_dist:
                        d[next][cur_cnt + 1] = cur_dist + next_dist
                        heapq.heappush(q, (cur_dist + next_dist, cur_cnt + 1, next))
            else:
                if d[next][cur_cnt] > cur_dist + next_dist:
                    d[next][cur_cnt] = cur_dist + next_dist
                    heapq.heappush(q, (cur_dist + next_dist, cur_cnt, next))
    return d[m][num]

n, m = map(int, sys.stdin.readline().split())
arr = [0] * n
for i in range(n):
    arr[i] = int(sys.stdin.readline())
temp = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

adj1 = [[] for _ in range(n)]
adj2 = [[] for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        if temp[i][j]:
            adj2[i].append((j, temp[i][j]))
            adj2[j].append((i, temp[i][j]))
            if arr[i] != arr[j]:
                adj1[i].append((j, 1))
                adj1[j].append((i, 1))
            else:
                adj1[i].append((j, 0))
                adj1[j].append((i, 0))
                
val = bfs()
res = dijkstra(val)
print(val, res)