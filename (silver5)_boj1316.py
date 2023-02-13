# 아이디어, 그룹단어, 문자의 개수가 연속하는 경우 
# 문자의 개수가 연속하지 않는 경우에는 컷트하기?
# 특정 문자의 간격?



import sys

input = sys.stdin.readline

N = int(input())
answer = N
for i in range(N):
    M = input()
    for j in range(0,len(M)-1): # j+1까지 비교해야 하므로, 길이는 하나 전까지로 줄여야 한다.
        if M[j] == M[j+1]:
            continue
        elif M[j] in M[j+1:]: # 연속되지는 않더라도, 뒤에 현재의 값과 겹치는 값이 있으면 그룹 단어 X
            answer-=1
            break
        
print(answer)    
