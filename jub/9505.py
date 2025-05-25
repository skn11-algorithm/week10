import sys
import heapq

INF = sys.maxsize
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    k, w, h = map(int, sys.stdin.readline().rstrip().split())
    class_dict = {}
    for _ in range(k):
        name, time = sys.stdin.readline().rstrip().split()
        time = int(time)
        class_dict[name] = time
    class_dict["E"] = 0
    start_row, start_col = 0, 0
    nodes = []
    for i in range(h):
        position = sys.stdin.readline().rstrip()
        for j in range(w):
            if position[j] == "E":
                start_row, start_col = i, j
        nodes.append(position)

    def Dijkstra(start_row, start_col):
        distances = [[INF for _ in range(w)] for _ in range(h)]
        distances[start_row][start_col] = 0
        pq = []
        heapq.heappush(pq, [0, start_row, start_col])

        while pq:
            cur_cost, cur_row, cur_col = heapq.heappop(pq)

            if cur_row == 0 or cur_row == h-1 or cur_col == 0 or cur_col == w-1: return cur_cost

            if distances[cur_row][cur_col] < cur_cost: continue

            for x, y in zip(dx, dy):
                next_row, next_col = cur_row + y, cur_col + x
                if next_row < 0 or next_col < 0 or next_row >= h or next_col >= w: continue

                next_cost = class_dict[nodes[next_row][next_col]]
                if distances[next_row][next_col] > cur_cost + next_cost:
                    distances[next_row][next_col] = cur_cost + next_cost
                    heapq.heappush(pq, [cur_cost + next_cost, next_row, next_col])

        return -1
    answer = Dijkstra(start_row, start_col)
    print(answer)