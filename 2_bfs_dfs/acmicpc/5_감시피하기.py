# https://github.com/ndb796/python-for-coding-test

from itertools import combinations
from copy import deepcopy

n = int(input())
graph = []
x_cord = []
for i in range(n):
    graph.append(list(map(str, input().split())))
    for j, value in enumerate(graph[-1]):
        if value == 'X':
            x_cord.append((i, j))

wall_cand_lst = list(combinations(x_cord, 3))

def dfs(i, j, n, temp_graph, k):

    if k == 0:
        next_i = i
        next_j = j + 1
    if k == 1:
        next_i = i
        next_j = j - 1
    if k == 2:
        next_i = i - 1
        next_j = j
    if k == 3:
        next_i = i + 1
        next_j = j

    if not (-1 < next_i < n and -1 < next_j < n):
        return True
    elif -1 < next_i < n and -1 < next_j < n:
        if temp_graph[next_i][next_j] == 'S':
            return False
        elif temp_graph[next_i][next_j] == 'O':
            return True
        elif temp_graph[next_i][next_j] == 'T':
            return True
        elif temp_graph[next_i][next_j] == 'X':
            return dfs(next_i, next_j, n, temp_graph, k)


def search(n, graph_temp):
    for i in range(n):
        for j in range(n):
            if graph_temp[i][j] == 'T':
                for k in range(4):
                    # False equal to Fail (Teacher Found Student Case)
                    if not dfs(i, j, n, graph_temp, k):
                        return False
    return True

answer_flag = False
for walls in wall_cand_lst:
    graph_temp = deepcopy(graph)

    for x, y in walls:
        graph_temp[x][y] = 'O'

    if search(n, graph_temp):
        answer_flag = True

    if answer_flag:
        break

if answer_flag:
    print("YES")
else:
    print("NO")




