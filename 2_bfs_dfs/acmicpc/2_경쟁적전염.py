# https://www.acmicpc.net/problem/18405

from collections import deque

n, k = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

disease_dict = {}
for key in range(1, k+1):
    disease_dict[key] = deque()

for i, row in enumerate(graph, 1):
    for j, value in enumerate(row, 1):
        if value != 0:
            disease_dict[value].append((i,j))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while s:
    for key in range(1, k+1):
        temp_queue = deque()
        while disease_dict[key]:
            x_, y_ = disease_dict[key].popleft()
            for delta_x, delta_y in zip(dx, dy):
                next_x, next_y = x_ + delta_x, y_ + delta_y
                if 0 < next_x < n+1 and 0 < next_y < n+1 and graph[next_x-1][next_y-1] == 0:
                    graph[next_x-1][next_y-1] = key
                    temp_queue.append((next_x, next_y))
        disease_dict[key] = temp_queue
    s -= 1

print(graph[x-1][y-1])