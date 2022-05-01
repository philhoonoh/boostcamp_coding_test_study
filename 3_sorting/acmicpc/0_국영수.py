# https://www.acmicpc.net/problem/10825

n = int(input())
student_lst = []
for _ in range(n):
    name, kor, eng, mat = input().split()
    student_lst.append([str(name), int(kor), int(eng), int(mat)])

student_lst.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for student in student_lst:
    print(student[0])