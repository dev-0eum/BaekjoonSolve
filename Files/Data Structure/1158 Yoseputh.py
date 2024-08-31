import sys

num, th = map(int, sys.stdin.readline().split())
tmp = th
line = [x for x in range(1, num+1)]
answer = []

while num != 0:
    th = th % num
    if th == 0:
        th = num

    answer.append(line[th-1])
    line.pop(th-1)

    num -= 1
    th = th + tmp -1

print(f"<{', '.join(map(str,answer))}>")
