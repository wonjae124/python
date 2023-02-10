import sys

input = sys.stdin.readline

N,M = map(int,input().split())
vst = [False]*(N+1)
rst = []

def recur(input):
    if len(rst) == M: # rst에 들어있는 값이 M개일 때 출력 필요. 만약, input==M이면 input=3, M=2이면 (3,1)은 print하지 못함.
        print(' '.join(rst))
        return
    
    for i in range(input+1,N+1): # 아래 recur의 시작점 정의 
        if not vst[i]:
            vst[i]=True
            rst.append(str(i))
            recur(i) # 순환 도는 시작점이 맨 처음부터가 아니어야 함. 오름차순이니깐, 부모 노드보다 값이 1 커야 한다.
            vst[i]=False
            rst.pop()
                     

recur(0)