#DFS
def dfs(v):
    print(v, end=' ')
    Visited[v]=True
    for i in range(1,N+1):
        if Visited[i] == False and s[v][i]==True:
            dfs(i)
            
            


def bfs(V):
    queue = [V] # 리스트 형태이다.
    print(type(queue))
    Visited[V] = True
    
    
    while(queue): # 먼저 들어온 큐를 먼저 나가게 만든다, 즉 재귀적으로 bfs를 부르는일이 없다.
        v = queue[0] # 리스트의 값을 저장하므로 정수를 가진다
        print(v)
        print(v,end=' ')
        del queue[0]
        for i in range(1,N+1):
            if not Visited[i] and s[v][i]:
                queue.append(i)
                Visited[i]=True        
                
                
                
N, M, V = map(int,input().split())

array=[]


# for i in range(M):
#     array.append(list(map(int,input().split())))
    # array[i]로 받으면 list indext out of range 발생. 아직 인덱스가 비었기 떄문임
    

Visited = [False]*(N+1) # 방문자 리스트 노드의 개수+1

s = [[0]*(N+1) for i in range(N+1)] # 노드의 개수에+1로 출발지 목적지까지 지칭하는 행, 열 번호 사용

for i in range(M):
    x, y=map(int,input().split())
    s[x][y]=1
    s[y][x]=1
    
    

#dfs(V)
bfs(V)
