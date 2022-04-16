num = input()
length = len(num)
half = length//2
left = sum([int(i) for i in num[0:half]])
right = sum([int(i) for i in num[half:]])

if left == right:
    print("LUCKY")
else:
    print("READY")