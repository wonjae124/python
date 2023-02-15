# 아이디어 : 나누는 수를 찾기 위해, 제곱근을 이용함. 나눠지는 경우면, 약수가 존재하므로 출력 X, 나눠지지 않으면 출력 O
# 시간복잡도 : O(N^1/2)
# 자료구조 : 나머지 : %, 몫 : //, 나누기 : /, 정수들어가면 정수 반환, 실수들어가면 실수 반환

import sys


input = sys.stdin.readline
M, N  = map(int,input().split())

for i in range(M,N+1):
    if i==1: #소수의 정의, 1을 제외한 자연수 중에, 1과 자기 자신만을 약수로 가지는 수 
        continue
    for j in range(2, int(i**0.5)+1): # i=3이면 j는 2, i=4,6,7,8이면 j는 2,3, i=9,10,11,12,13,14,15이면 j는 2,3,4이다.
        if i%j == 0:
            break
    else:
        print(i)