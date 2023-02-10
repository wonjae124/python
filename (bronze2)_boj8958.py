# O가 계속 나오면, cnt에 1을 추가로 더한다.
# 만약 X가 나오면 종료하고, 최종 cnt를 rst 점수에 합산한다
# 시간복잡도?
# 자료구조: 값을 쪼개서 문자열로 저장하기 위해서는, 리스트 값을 문자열로 바꾸고 별도로 리스트에 담아야한다.

import sys

input = sys.stdin.readline
N = int(input())
arr = [input().rstrip() for _ in range(5)]

for i in range(N):
    result = 0
    cnt = 0
    lst = list(arr[i])
    for j in range(len(lst)):
        if lst[j] == 'O':
            cnt+=1
            result+=cnt    
        else: 
            cnt=0
            result+=cnt
            
