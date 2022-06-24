import sys

n, c = map(int, sys.stdin.readline().rstrip().split(' '))
arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

def is_possible(arr, mid, c):
    cur_ = arr[0]
    cnt = 1
    for house in arr[1:]:
        if house >= cur_ + mid:
            cnt += 1
            cur_ = house
        if cnt >= c:
            return True
    return False

# C 3
# 1 2 4 8 9
# L U M
# 0 10 5
# 0 4 2
# 3 4 3
# 4 4 4
# 4 3 4

def binary_search(arr, c):
    lower = 0
    upper = 1000000000

    while lower <= upper:
        mid = (lower + upper) // 2
        if not is_possible(arr, mid, c):
            upper = mid - 1
        else:
            lower = mid + 1

    return lower - 1

arr.sort()
result = binary_search(arr, c)
print(result)