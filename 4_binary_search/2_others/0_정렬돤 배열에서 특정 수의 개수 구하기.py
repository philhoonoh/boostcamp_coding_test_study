# M1

# from bisect import bisect_left, bisect_right
# import sys
#
# n, x = map(int, sys.stdin.readline().rstrip().split(' '))
# arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))
#
# left = bisect_left(arr, x)
# right = bisect_right(arr, x)
#
# if right-left == 0:
#     print(-1)
# else:
#     print(right-left)

# M2

import sys

def binary_search_right(arr, x):
    lower = 0
    upper = len(arr) - 1

    while lower <= upper:
        mid = (upper+lower) // 2
        if arr[mid] <= x:
            lower = mid + 1
        else: # arr[mid] >= x
            upper = mid - 1
    return lower - 1

def binary_search_left(arr, x):
    lower = 0
    upper = len(arr) - 1

    while lower <= upper:
        mid = (upper + lower) // 2
        if arr[mid] < x:
            lower = mid + 1
        else:  # arr[mid] >= x
            upper = mid - 1
    return lower - 1

n, x = map(int, sys.stdin.readline().rstrip().split(' '))
arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))

left = binary_search_left(arr, x)
right = binary_search_right(arr, x)
result = right - left

if result == 0:
    print(-1)
else:
    print(result)