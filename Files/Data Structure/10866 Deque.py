import sys
from collections import deque

cnt = int(sys.stdin.readline())
dq = deque()

for _ in range(cnt):
    line = sys.stdin.readline().split()
    cmd = line[0]

    if cmd == "push_front":
        dq.appendleft(line[1])
    elif cmd == "push_back":
        dq.append(line[1])
    elif cmd == "pop_front":
        if len(dq) != 0:
            print(dq.popleft())
        else:
            print(-1)
    elif cmd == "pop_back":
        if len(dq) != 0:
            print(dq.pop())
        else:
            print(-1)
    elif cmd == "size":
        print(len(dq))
    elif cmd == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif cmd == "front":
        if len(dq) != 0:
            print(dq[0])
        else:
            print(-1)
    elif cmd == "back":
        if len(dq) != 0:
            print(dq[-1])
        else:
            print(-1)