def dfs(start):
    visited[start]=True
    print(start,end=' ')
    
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            

N,M,V=map(int,input().split())
graph=[[] for _ in range(N+1)] #?

for _ in range(N):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in graph:
    i.sort()

print(graph)
    
visited=[False]*(N+1)
dfs(V)
