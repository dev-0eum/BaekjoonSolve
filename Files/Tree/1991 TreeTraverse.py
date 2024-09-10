# import sys
# cnt = int(sys.stdin.readline())

# answer = ''
# visited = [0 for _ in range(cnt)]
# graph = dict()
# # ord('A') = ascii num = 65

# for i in range(ord('A'), ord('A')+cnt):
#     # visited.append(chr(i))
#     line = sys.stdin.readline().split()
#     graph[chr(i)] = line
# print(graph)

# # 전위 root-L-R
# def prefix(start):
#     global answer
#     answer += graph[start][0] # root
#     visited[ord(start)-ord('A')] = 1 # memo
#     print("visited: ",visited)
#     print(graph[start][1], visited[ord(start)-ord('A')])

#     if graph[start][1] != '.' and visited[ord(graph[start][1])-ord('A')] != 1:
#         prefix(graph[start][1])
#     elif graph[start][2] != '.'and visited[ord(graph[start][2])-ord('A')] != 1:
#         prefix(graph[start][2])
#     return answer

# # 중위 L-root-R
# def infix():
#     pass

# # 후위 L-R-root
# def postfix():
#     pass

# print()
# print(prefix('A'))

import sys
tree = {}

for _ in range(int(sys.stdin.readline())):
    root,left,right = sys.stdin.readline().split()
    tree[root] = [left,right]

def infix(root):
    if root != '.':
        print(root, end="")
        infix(tree[root][0])
        infix(tree[root][1])
def prefix(root):
    if root != '.':
        prefix(tree[root][0])
        print(root, end="")
        prefix(tree[root][1])
def postfix(root):
    if root != '.':
        postfix(tree[root][0])
        postfix(tree[root][1])
        print(root, end="")

infix('A')
print()
prefix('A')
print()
postfix('A')