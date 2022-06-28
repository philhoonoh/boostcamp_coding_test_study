import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n+1)]

INF = int(1e9)
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

start = 1
q = []
distance[start] = 0
heapq.heappush(q, (0, start))

while q:
    dist, cur_node = heapq.heappop(q)

    if distance[cur_node] < dist:
        continue

    for next_node in graph[cur_node]:
        cost = dist + 1
        if distance[next_node] > cost:
            distance[next_node] = cost
            heapq.heappush(q, (cost, next_node))

max_distance = max([x for x in distance if x != INF and x != 0])

cnt = 0
for index, value in enumerate(distance):
    if value == max_distance:
        cnt += 1

for index, value in enumerate(distance):
    if value == max_distance:
        break

print(index, max_distance, cnt)