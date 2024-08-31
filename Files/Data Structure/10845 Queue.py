import sys

# Use Stack
cnt = int(sys.stdin.readline())
stack = []

# for _ in range(cnt):
#     line = sys.stdin.readline().split()
#     cmd = line[0]

#     if cmd == "push":
#         stack.append(line[1])

#     elif cmd == "pop":
#         if len(stack):
#             print(stack.pop(0))
#         else:
#             print(-1)

#     elif cmd == "size":
#         print(len(stack))
#     elif cmd == "empty":
#         if len(stack) == 0:
#             print(1)
#         else:
#             print(0)
#     elif cmd == "front":
#         if len(stack)!=0:
#             print(stack[0])
#         else:
#             print(-1)
#     elif cmd == "back":
#         if len(stack) != 0:
#             print(stack[-1])
#         else:
#             print(-1)


# Use deque
from collections import deque
dq = deque()

for _ in range(cnt):
    line = sys.stdin.readline().split()
    cmd = line[0]

    if cmd == "push":
        dq.append(line[1])

    elif cmd == "pop":
        if len(dq) != 0:
            print(dq.popleft())
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