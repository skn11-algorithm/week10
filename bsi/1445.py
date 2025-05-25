import sys
import heapq

input = sys.stdin.readline

def solve():
    width, height = map(int, input().split())
    maze = []
    start_pos = None
    flower_pos = None

    for i in range(width):
        row = input().strip()
        maze.append(row)
        for j in range(height):
            if row[j] == 'S':
                start_pos = (i, j)
            elif row[j] == 'F':
                flower_pos = (i, j)
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def garbage(a, b):
        if maze[a][b] == 'g':
            return False
        
        for i, j in directions:
            na, nb = a + i, b + j
            if 0<= na < width and 0 <= nb < height and maze[na][nb] == 'g':
                return True
            return False


    pq = [(0, 0, start_pos[0], start_pos[1])]
    visited = {}

    while pq:
        garbage_count, way_count, a, b = heapq.heappop(pq)

        if (a, b) == flower_pos:
            print(garbage_count, way_count)
            return
        
        if (a, b) in visited:
            prev_garbage, prev_way = visited[(a, b)]
            if (prev_garbage < garbage_count or (prev_garbage == garbage_count and prev_way <= way_count)):
                continue

        visited[(a, b)] = (garbage_count, way_count)

        for dx, dy in directions:
            nx, ny = a + dx, b+dy

            if not (0<= nx < width and 0 <= ny < height):
                continue

            new_garbage = garbage_count
            new_way = way_count

            if maze[nx][ny] == 'g':
                new_garbage += 1
            elif maze[nx][ny] in '.SF' and garbage(nx, ny):
                if not (maze[nx][ny] in 'SF'):
                    new_way += 1
            
            if (nx, ny) not in visited:
                heapq.heappush(pq, (new_garbage, new_way, nx, ny))
            else:
                prev_gabage, prev_way = visited[(nx, ny)]
                if (new_garbage < prev_garbage or (new_garbage == prev_garbage and new_way < prev_way)):
                    heapq.heappush(pq, (new_garbage, new_way, nx, ny))


solve()