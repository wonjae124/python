#아이디어 : 숫자를 뒤집어서 저장하지는 않고, 과정에서 바로 int로 형변환해서 크기 비교

import sys

input = sys.stdin.readline
N, M = map(str,input().split())
N = N[::-1]
M = M[::-1]

if  int(N)>int(M):
    print(N)
else:
    print(M)

