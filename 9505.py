'''
엔터프라이즈호 탈출
입력 : 우주선의 크기 N×M, 우주선 내부 지도, 시작점(S), 도착점(F), 장애물(X)
출력 : 시작점에서 도착점까지의 최소 이동 횟수
아이디어 : 너비 우선으로 BFS 을 활용하여 최단 경로 구하기, 장애물은 통과할 수 없으며, 상하좌우로만 이동 가능

'''

import sys
import heapq
INF = sys.maxsize 

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

t = int(sys.stdin.readline().rstrip())  # 테스트 케이스 개수

for _ in range(t):
    k, w, h = map(int, sys.stdin.readline().rstrip().split())
    # k: 타일 종류 수, w: 우주선 너비, h: 우주선 높이

    class_dict = {}  # 각 타일의 소요 시간 저장
    for _ in range(k):
        name, time = sys.stdin.readline().rstrip().split()
        class_dict[name] = int(time)

    class_dict["E"] = 0  # 시작 위치는 소요 시간 0


    start_row, start_col = 0, 0
    nodes = []  # 우주선 지형 정보 저장

    for i in range(h):
        position = sys.stdin.readline().rstrip()
        for j in range(w):
            if position[j] == "E":  # 시작 위치 저장
                start_row, start_col = i, j
        nodes.append(position)

    def dijkstra(start_row, start_col):
        # 최소 거리 테이블
        distances = [[INF for _ in range(w)] for _ in range(h)]
        distances[start_row][start_col] = 0

        pq = []
        heapq.heappush(pq, [0, start_row, start_col])  # (비용, y, x)

        while pq:
            cur_cost, cur_row, cur_col = heapq.heappop(pq)

            # 현재 위치가 가장자리면 탈출 성공 (종료 조건)
            if cur_row == 0 or cur_row == h-1 or cur_col == 0 or cur_col == w-1:
                return cur_cost

            # 이미 더 짧은 경로로 방문했다면 패스
            if distances[cur_row][cur_col] < cur_cost:
                continue

            # 방향 탐색
            for x, y in zip(dx, dy):
                next_row = cur_row + y
                next_col = cur_col + x

                # 경계 조건 확인
                if next_row < 0 or next_col < 0 or next_row >= h or next_col >= w:
                    continue

                # 다음 위치의 이동 비용
                next_cost = class_dict[nodes[next_row][next_col]]

                # 더 짧은 거리로 갈 수 있으면 갱신
                if distances[next_row][next_col] > cur_cost + next_cost:
                    distances[next_row][next_col] = cur_cost + next_cost
                    heapq.heappush(pq, [cur_cost + next_cost, next_row, next_col])

        # 탈출 경로가 없다면
        return -1

    answer = dijkstra(start_row, start_col)
    print(answer)
