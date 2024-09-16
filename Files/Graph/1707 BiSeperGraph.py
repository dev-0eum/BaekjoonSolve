import sys
from collections import deque

def bfs(start):
    global visited, graph, group
    q = deque()
    q.append(start) # before: only check starting with VERTEX 1
    visited[start] = 2

    while q:
        # print("visited: ",visited)
        x = q.popleft()
        # print("x: ",x)

        if visited[x] == 1:
            group = 2
        elif visited[x] == 2:
            group = 1
        # print("group: ",group)

        # next level
        for i in graph[x]:
            # print("i: ",i)
            if not visited[i]:
                q.append(i)
                visited[i] = group
            elif visited[i] == visited[x]:
                return False # before: "NO"
    return True # before: "YES"

# test case num
K = int(sys.stdin.readline()) 
for i in range(K):
    # print("case ",i+1)
    V, E = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]

    for _ in range(E):
        a, b = map(int,sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    # print(graph)
    group = 1
    for i in range(1, V + 1):
        if not visited[i]:  # 방문한 정점이 아니면, bfs 수행
            result = bfs(i)
            if not result:
                break

    # print(bfs()) --> 
    print('YES' if result else "NO")