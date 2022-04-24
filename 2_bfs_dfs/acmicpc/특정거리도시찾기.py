# N : 도시의 개수 , M : 도로의 개수, K : 거리 정보, X: 출발 도시의 번호
# https://www.acmicpc.net/problem/18352

from collections import deque

n, m, k, x = map(int, input().split())

array = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    array[start].append(end)

q = deque()
q.append((x, 0))
visited = set()
answer = []
while q:
    start_, level = q.popleft()

    if level == k:
        answer.append(start_)
    elif level > k:
        break

    visited.add(start_)
    for next_ in array[start_]:
        if next_ not in visited:
            q.append((next_, level+1))
            visited.add(next_)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)