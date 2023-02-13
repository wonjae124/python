# 문자열간에 +로 합칠 수 있다. int와 str은 서로 지원하지 않는 연산임

import sys

input = sys.stdin.readline

N = int(input())
cnt = N
line = 1
while cnt>line:
    cnt-=line
    line+=1

if line % 2 == 0:
    up = cnt
    down = line-cnt+1
elif(line%2) == 1:
    up = line-cnt+1
    down = cnt

print(str(up)+'/'+str(down),sep='')