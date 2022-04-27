# https://www.acmicpc.net/problem/16234

from collections import deque

# 동 북 서 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

n, l, r = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


def bfs(i, j, visited, graph, l, r, n):
    queue = deque()
    queue.append((i, j, graph[i][j]))
    cord_lst = []
    total = 0
    cnt = 0

    while queue:
        x, y, value = queue.popleft()
        cord_lst.append([x, y])
        cnt += 1
        total += value
        for delta_x, delta_y in zip(dx, dy):
            next_x, next_y = x + delta_x, y + delta_y
            if -1 < next_x < n and -1 < next_y < n and (next_x, next_y) not in visited \
                and l <= abs(graph[x][y] - graph[next_x][next_y]) <= r:
                queue.append((next_x, next_y, graph[next_x][next_y]))
                visited.add((next_x, next_y))
    return cord_lst, total, cnt


day_cnt = 0
while True:
    border_lst = []
    average_lst = []
    visited = set()

    flag_no_change = True
    for i in range(n):
        for j in range(n):
            if (i, j) not in visited:
                visited.add((i, j))
                border_open_lst, total, cnt = bfs(i, j, visited, graph, l, r, n)
                value = total // cnt
                if cnt != 1:
                    flag_no_change = False
                border_lst.append(border_open_lst)
                average_lst.append(value)

    if flag_no_change:
        print(day_cnt)
        break
    else:
        day_cnt += 1
        for border, value in zip(border_lst, average_lst):
            for i, j in border:
                graph[i][j] = value

