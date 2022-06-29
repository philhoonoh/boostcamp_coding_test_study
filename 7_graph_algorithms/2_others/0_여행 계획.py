import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

direction = list(map(int, input().split()))


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    if find_parent(parent, a) != find_parent(parent, b):
        if a < b:
            parent[b] = a
        else:
            parent[a] = b


parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            if find_parent(parent, i+1) != find_parent(parent, j+1):
                union_parent(parent, i+1, j+1)


default = parent[direction[0]]
cnt = 0
for i in range(m):
    if default == parent[direction[i]]:
        cnt += 1
    else:
        break

if cnt == m:
    print('YES')
else:
    print('NO')
