import sys

input = sys.stdin.readline


T = int(input())

for _ in range(T):
    k,n = int(input()),int(input())
    f0 = [x for x in range(1,n+1)] # 0층부터, 본인 방의 n호실까지 1부터 시작해서 인덱스 값으로 채우기
    for k in range(k): # 0층부터 본인 아래층 k-1층 
        for i in range(1,n): # 인덱스로 보면 본인 방까지
            # print(f0[i],f0[i-1]) 
            f0[i]+=f0[i-1] # # i-1을 통해, 맨 앞 방을 포함, 층별 각 호실의 사람 수 변경
    print(f0[-1])