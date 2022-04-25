# https://www.acmicpc.net/problem/14502

from itertools import combinations
from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
graph = []
empty_lst = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j, value in enumerate(graph[-1]):
        if value == 0:
            empty_lst.append((i, j))

cand_wall_lst = list(combinations(empty_lst, 3))

def dfs(i, j, n, m, graph_temp):
    if not(-1<i<n and -1<j<m) or graph_temp[i][j] == 1 or graph_temp[i][j] == 2:
        return False

    if graph_temp[i][j] == 0:
        graph_temp[i][j] = 2
        dfs(i - 1, j, n, m, graph_temp)
        dfs(i, j - 1, n, m, graph_temp)
        dfs(i + 1, j, n, m, graph_temp)
        dfs(i, j + 1, n, m, graph_temp)
        return True
    return False


answer = -1
for walls in cand_wall_lst:
    graph_temp = deepcopy(graph)

    for x, y in walls:
        graph_temp[x][y] = 1

    for i in range(n):
        for j in range(m):
            if graph_temp[i][j] == 2:
                dfs(i - 1, j, n, m, graph_temp)
                dfs(i, j - 1, n, m, graph_temp)
                dfs(i + 1, j, n, m, graph_temp)
                dfs(i, j + 1, n, m, graph_temp)

    cnt = 0
    for row in graph_temp:
        for value in row:
            if value == 0:
                cnt += 1
    answer = max(answer, cnt)
    # break
print(answer)
