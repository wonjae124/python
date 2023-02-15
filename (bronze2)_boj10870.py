# 피보나치수5, 아이디어 : f0과 f1은 정해줘야겠다. 0과 1로 말이다
# n번째 피보나치수를 구하면 된다. fn = fn-1+fn-2
# 자료구조 : 점화식으로 만들어야해서, n-2의 인덱스까지 계산필요. 따라서, for문 range(2,n+2) 필요

import sys
input = sys.stdin.readline

n = int(input())
f = [0]*(n+2)

if n==0:
    print(0)
elif n==1:
    f[1]=1
    print(1)
else:
    f[1]=1
    for i in range(2,n+2):
        f[i]=f[i-1]+f[i-2]
    print(f[-2])