import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
circum = []
graph = [[] for _ in range(N+1)]

# make graph that means adjacent vertex
for _ in range(N):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
#print(graph)

# 순환선 결정(DFS) --> make Circum Point
for start in range(1,N+1): # 각 vertex에 대해 
    flag=2
    #print()
    #print("NODE: ",start)
    visited = [0 for _ in range(N+1)]
    stack=[]
    stack.append(start)
    while stack:
        x = stack.pop()
        visited[x]=1

        for i in graph[x]:
            #print(i)
            if i==start:
                flag -= 1
            if not visited[i]:
                stack.append(i)
        #print(stack)
        #print("visited: ",visited)

    # Circum Point 발견 
    if flag<0:
        circum.append(start)

#print("circum: ",circum)
# closest distance to Circum Point(BFS)
for d in range(1,N+1):
    if d in circum:
        print(0,end=" ")
    else:
        #print()
        #print("from: ",d)
        distance=0
        q = deque()
        visited = [-1 for _ in range(N+1)]
        q.append(d)
        while q:
            x = q.popleft()
            visited[x] = 1
            distance += 1
            for i in graph[x]:
                #print("i: ",i)
                if i in circum:
                    visited[i] = 0
                    print(distance,end=" ")
                elif visited[i] == 0:
                    visited[i] = distance
                    q.append(i)
                visited[i] = distance
        print(visited)
