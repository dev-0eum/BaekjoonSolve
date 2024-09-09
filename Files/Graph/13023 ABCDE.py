import sys
num,relation = map(int,sys.stdin.readline().split())

#행렬 만들기
graph = [[0]*(num+1) for _ in range(num+1)]
for i in range (relation):
    a,b = map(int,input().split())
    
    for x in graph[a]:
        if x == 1:
            graph[a][x] = 1
    graph[a][b] = graph[b][a] = 1

'''
[0] 1
[1] 2
[2] 3
[3] 0 -> 1
[4] 1 -> 2,0
'''

print(graph)

if graph[0][1] == 1 and graph[1][2] == 1 and graph[2][3] == 1 and graph[3][4] == 1:
    print(1)
else:
    print(0)