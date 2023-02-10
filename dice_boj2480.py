import sys

input = sys.stdin.readline

N,M,K = map(int,input().split())
result = int(0)

if N==M and N==K:
    result=10000+N*1000
elif N==M and N!=K:
    result=1000+N*100
elif N==K and M!=N:
    result=1000+N*100
elif N!=M and M==K:
    result=1000+M*100
elif N!=M and M!=K and N!=K:
    result=max(N,M,K)*100
else:
    print("no")

print(result)