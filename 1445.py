'''
일요일 아침의 데이트 
입력 : 50 >= 숲이 세로 N 가로 M  >= 3  / 시작 S 꽃 F 쓰레기 g 깨끗 .
출력 : 지나가는 쓰레기 최소 개수
아이디어 :쓰레기를 지나는 경우에는 쓰레기 주변 칸으로 우선순위를 두고 더 좋은 경로로 탐색하기 

'''

from collections import deque
import sys
input = sys.stdin.readline


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
MAX = float('inf') 

N, M = map(int, input().split()) 
forest = [input().strip() for _ in range(N)] 

garbage = set()   # 쓰레기 좌표
adjacent = set()  # 쓰레기 근처 칸

# 시작, 도착, 쓰레기, 쓰레기 근처 칸 체크
for i in range(N):
    for j in range(M):
        if forest[i][j] == 'S':
            sx, sy = j, i  
        elif forest[i][j] == 'F':
            fx, fy = j, i 
        elif forest[i][j] == 'g':
            garbage.add((j, i)) 
            for d in range(4):
                ni, nj = i + dy[d], j + dx[d]
                if 0 <= ni < N and 0 <= nj < M:
                    adjacent.add((nj, ni))

# 쓰레기(g), 시작(S), 도착(F) 위치는 쓰레기 근처 칸에서 제외
adjacent -= garbage
adjacent.discard((sx, sy))
adjacent.discard((fx, fy))

# 각 위치에서 (쓰레기 밟은 수, 쓰레기 근처 밟은 수) 저장
visited = [[(MAX, MAX) for _ in range(M)] for _ in range(N)]
visited[sy][sx] = (0, 0) 

# BFS 탐색 시작: 큐에 (현재 위치 x, y, 쓰레기 수, 근처 쓰레기 수)
q = deque([(sx, sy, 0, 0)])

while q:
    x, y, g_cnt, adj_cnt = q.popleft()

    # 도착지점에 도달했어도 큐 안의 다른 경로가 더 나을 수 있으므로 탐색은 계속
    if (x, y) == (fx, fy):
        continue

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]

        if 0 <= nx < M and 0 <= ny < N:
            ng = g_cnt + 1 if (nx, ny) in garbage else g_cnt
            nadj = adj_cnt + 1 if (nx, ny) in adjacent else adj_cnt

            # 현재 경로가 이전보다 더 나은 경로일 경우에만 갱신 및 큐에 추가
            if visited[ny][nx] > (ng, nadj):
                visited[ny][nx] = (ng, nadj)
                q.append((nx, ny, ng, nadj))

print(*visited[fy][fx])
