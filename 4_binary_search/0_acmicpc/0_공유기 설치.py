n, m = map(int, input().split(' '))
house = []
for _ in range(n):
    house.append(int(input()))

house.sort()
lower = 1
upper = house[-1]

def is_possible(mid, house, m):
    cnt = 1
    cur_house = house[0]
    for i in range(1, len(house)):
        if house[i] - cur_house >= mid:
            cnt += 1
            cur_house = house[i]
    if cnt >= m:
        return True
    return False

while lower <= upper:
    mid = (lower + upper) // 2
    if not is_possible(mid, house, m):
        upper = mid - 1
    else:
        lower = mid + 1

print(lower-1)