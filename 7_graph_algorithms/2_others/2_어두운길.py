import sys

n, m = map(int, sys.stdin.readline().rstrip().split())


edges_lst = []
total_cost = 0
for _ in range(m):
    a, b, cost = map(int, sys.stdin.readline().rstrip().split())
    edges_lst.append((cost, a, b))
    total_cost += cost


parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if b > a:
        parent[b] = a
    else:
        parent[a] = b

edges_lst.sort()

activate_cost = 0
for cost, a, b in edges_lst:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        activate_cost += cost

print(total_cost - activate_cost)