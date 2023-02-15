#아이디어 : 제곱근한 위치까지, 나누어 떨어지는지 확인(나머지 0)하고, 나누어지지 않으면 COUNT하자
#시간복잡도 : O(n^1/2)
#자료구조 : %는 나머지 연산자로 정수가 인수일시 정수 반환 실수일시 실수 반환, 제곱근 2*0.5는 1.414로 실수반환, for문은 정수만 순환 가능, 따라서 제곱근은 int()로 정수변환

import sys


input=sys.stdin.readline
N = int(input())
cnt=0
T = input().split()
for i in range(N):
    M =int(T[i])
    if M == 1: # continue 쓰면 if-else문 통과한다.
        continue
    # 조건문 True 아님에도 진행 가능한 코드
    for j in range(2,int(M**(0.5))+1):
        if M%j == 0:
            break    
    else: 
        cnt+=1
        
print(cnt)