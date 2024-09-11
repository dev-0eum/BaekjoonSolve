import sys

cnt = int(sys.stdin.readline())
tree={}
for x in range(1,cnt+1):
    tree[x]=[0,0]

for _ in range(cnt-1):
    root, child = map(int,sys.stdin.readline().split())
    if tree[root][0] == 0:
        tree[root][0] = child
    else:
        tree[root][1] = child

# for x in range(cnt-1):
#     print()

print(tree)