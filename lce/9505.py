# 엔터프라이즈호 탈출
import sys
import heapq
input = sys.stdin.readline

T = int(input())

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):
    k, m, n = map(int, input().split())
    
    # 문자 → 비용 맵
    cost_map = {}
    for _ in range(k):
        ch, c = input().split()
        cost_map[ch] = int(c)
    cost_map['E'] = 0  # 시작점은 무조건 비용 0

    # 지도 입력
    grid = [list(input().strip()) for _ in range(n)]
    dist = [[float('inf')] * m for _ in range(n)]

    # 시작점 찾기
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'E':
                sx, sy = i, j

    # 다익스트라
    hq = []
    dist[sx][sy] = 0
    heapq.heappush(hq, (0, sx, sy))

    while hq:
        cur_cost, x, y = heapq.heappop(hq)

        # 외곽 도달하면 종료
        if x == 0 or x == n - 1 or y == 0 or y == m - 1:
            print(cur_cost)
            break

        if dist[x][y] < cur_cost:
            continue

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                next_cost = cur_cost + cost_map[grid[nx][ny]]
                if next_cost < dist[nx][ny]:
                    dist[nx][ny] = next_cost
                    heapq.heappush(hq, (next_cost, nx, ny))