import sys, heapq

input = sys.stdin.readline

n, m = tuple(map(int, input().split()))

board = [
    list(input().rstrip())
    for _ in range(n)
]

start = [-1, -1]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'S':
            start[0] = i
            start[1] = j
            break

    if start[0] != -1 and start[1] != -1:
        break

q = [(0, 0, start[0], start[1])]

dys = [1, 0, -1, 0]
dxs = [0, 1, 0, -1]

def in_range(y, x):
    return 0 <= x < m and 0 <= y < n

visited = [
    [False] * m
    for _ in range(n)
]
visited[start[0]][start[1]] = True

def existNearG(y, x):
    for dy, dx in zip(dys, dxs):
        ny = y + dy
        nx = x + dx

        if in_range(ny, nx) and board[ny][nx] == 'g':
            return True

    return False


while q:
    passG, nearG, y, x = heapq.heappop(q)
    if board[y][x] == 'F':
        print(passG, nearG)
        break

    for dy, dx in zip(dys, dxs):
        ny = y + dy
        nx = x + dx

        if in_range(ny, nx) and not visited[ny][nx]:
            visited[ny][nx] = True
            if board[ny][nx] == 'g':
                heapq.heappush(q, [passG + 1, nearG, ny, nx])
            elif board[ny][nx] == '.':
                heapq.heappush(q, [passG, nearG + int(existNearG(ny, nx)), ny, nx])
            else:
                heapq.heappush(q, [passG, nearG, ny, nx])