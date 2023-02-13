# 아이디어 : 입력받은 문자열을 리스트로 변경해, 문자로 쪼갠다음에, for문에 돌려서 해당 인덱스의 리스트 원소를 5번 나오게 만들기
# 복잡도 : ?
# 자료구조, for문

import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    M, K = input().split()    
    for j in range(len(K)):
        print(K[j]*int(M),end='')
    print()
    
    