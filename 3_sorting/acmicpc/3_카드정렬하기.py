# https://www.acmicpc.net/problem/1715

import heapq

n = int(input())
card_lst = []
for _ in range(n):
    card_lst.append(int(input()))

if n == 1:
    print(0)
else:
    heapq.heapify(card_lst)
    total = 0
    while len(card_lst) > 1:
        min_1 = heapq.heappop(card_lst)
        min_2 = heapq.heappop(card_lst)
        heapq.heappush(card_lst, min_1 + min_2)
        total += min_1
        total += min_2

    print(total)
