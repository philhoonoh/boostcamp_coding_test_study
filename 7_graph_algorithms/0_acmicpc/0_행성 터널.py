import sys

n = int(sys.stdin.readline().rstrip())

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

coord_lst = []
for _ in range(n):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    coord_lst.append((x,y,z))

x_lst = []
y_lst = []
z_lst = []
for index, (x, y, z) in enumerate(coord_lst, 1):
    x_lst.append((x, index))
    y_lst.append((y, index))
    z_lst.append((z, index))

x_lst.sort()
y_lst.sort()
z_lst.sort()


edge_lst = []
for i in range(1, len(x_lst)):
    cost = x_lst[i][0] - x_lst[i-1][0]
    a = x_lst[i][1]
    b = x_lst[i-1][1]
    edge_lst.append((cost, a, b))

for i in range(1, len(y_lst)):
    cost = y_lst[i][0] - y_lst[i - 1][0]
    a = y_lst[i][1]
    b = y_lst[i - 1][1]
    edge_lst.append((cost, a, b))

for i in range(1, len(z_lst)):
    cost = z_lst[i][0] - z_lst[i - 1][0]
    a = z_lst[i][1]
    b = z_lst[i - 1][1]
    edge_lst.append((cost, a, b))

edge_lst.sort()

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


total_cost = 0
for cost, a, b in edge_lst:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost

print(total_cost)