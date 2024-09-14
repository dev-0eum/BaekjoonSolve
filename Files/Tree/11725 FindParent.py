import sys

cnt = int(sys.stdin.readline())
tree=[[] for _ in range(cnt+1)]
visited = [0 for _ in range(cnt+1)]

for _ in range(cnt-1):
    n1, n2 = map(int,sys.stdin.readline().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

def dfs(v):
    for i in tree[v]:
        if visited[i] == 0:
            visited[i] = v
            dfs(i)

dfs(1)
for target in range(2,cnt+1):
    print(visited[target])
