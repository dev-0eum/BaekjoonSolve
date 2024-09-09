# 좋은 예제 & 설명
# https://velog.io/@falling_star3/%EB%B0%B1%EC%A4%80Python-1260%EB%B2%88-DFS%EC%99%80BFS

# N M V
N,M,V= map(int,input().split()) #?

#행렬 만들기
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range (M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1
'''
print(graph)
[[0, 0, 0, 0, 0], 
 [0, 0, 1, 1, 1], Vertex 1 & 인접 노드 = 2,3,4와 인접
 [0, 1, 0, 0, 1], Vertex 2 & 1,4 노드와 인접
 [0, 1, 0, 0, 1], V3
 [0, 1, 1, 1, 0]] V4
'''

# Stack & Queue
# to store data = visted list
visited1 = [0]*(N+1)
visited2 = visited1.copy()

