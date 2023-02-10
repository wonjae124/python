import sys

input = sys.stdin.readline

N, M = map(int,input().split())
rs = []
chk = [False]*(N+1)

def recur(num):
    if num == M:
        print(' '.join(map(str,rs))) # 결과를 문자열로 바꾼걸 프린트로 바꾸어서 조인
        return
    for i in range(1, N+1): # for문을 통해 현재 레벨을 돈다
        if chk[i] == False: 
            chk[i]=True
            rs.append(i) # 결과에 i값 추가
            recur(num+1) # 한 층 더 깊이 들어간다. 
            chk[i]=False
            rs.pop()
            
            
recur(0)