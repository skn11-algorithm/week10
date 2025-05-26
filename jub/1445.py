from collections import deque
import sys
input = sys.stdin.readline
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
MAX = float('inf')

N, M = map(int, input().split())
map_list = [input().strip() for _ in range(N)]

garbage = set()
adj_garbage = set()

for i in range(N) :
  for j in range(M) :
    if map_list[i][j] == 'S' :
      sx, sy = j, i
    elif map_list[i][j] == 'F' :
      fx, fy = j, i
    elif map_list[i][j] == 'g' :
      garbage.add((j, i))
      for k in range(4) :
        ai, aj = i + dy[k], j + dx[k]
        if -1 < ai < N and -1 < aj < M :
          adj_garbage.add((aj, ai))

adj_garbage.discard((sx, sy))
adj_garbage.discard((fx, fy))
adj_garbage -= garbage

visited = [[(MAX, MAX) for _ in range(M)] for _ in range(N)]
visited[0][0] = (0, 0)
q = deque([(sx, sy, 0, 0)])

while q :
  x, y, g, adj_g = q.popleft()
  if (x, y) == (fx, fy) :
    continue
  for k in range(4) :
    ax, ay = x + dx[k], y + dy[k]
    ag = g + 1 if (ax, ay) in garbage else g
    a_adj_g = adj_g + 1 if (ax, ay) in adj_garbage else adj_g
    if -1 < ax < M and -1 < ay < N and visited[ay][ax] > (ag, a_adj_g) :
      visited[ay][ax] = (ag, a_adj_g)
      q.append((ax, ay, ag, a_adj_g))

print(*visited[fy][fx])
