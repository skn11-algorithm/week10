import sys
from collections import deque

input = sys.stdin.readline

def solve():
    width, height = map(int, input().split())
    maze = []
    for _ in range(height):
        maze.append(input().strip())
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    distance = [[float('inf')] * width for _ in range(height)]
    distance[0][0] = 0

    dq = deque([(0, 0)])

    while dq:
        x, y = dq.popleft()

        if x == height-1 and y == width - 1:
            return distance[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < height and 0 <= ny < width:
                cost = distance[x][y] + int(maze[nx][ny])

                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost

                    if maze[nx][ny] == '0':
                        dq.appendleft((nx, ny))
                    else:
                        dq.append((nx, ny))
    return distance[height-1][width-1]

print(solve())