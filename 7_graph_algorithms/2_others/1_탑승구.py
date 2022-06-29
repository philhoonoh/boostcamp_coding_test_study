import sys

g = int(sys.stdin.readline().rstrip())
p = int(sys.stdin.readline().rstrip())


planes = []
for _ in range(p):
    planes.append(int(input()))


parent = [0] * (g+1)
for i in range(1, g+1):
    parent[i] = i


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


cnt = 0
for plane in planes:
    parent_node = find_parent(parent, plane)
    if parent_node == 0:
        print(cnt)
        break
    else:
        union_parent(parent, parent_node, parent_node-1)
        cnt += 1