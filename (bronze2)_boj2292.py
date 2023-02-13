# 아이디어 : 범위 안에 있는지를 확인할 때는, 한 쪽에(~보다 크다)에 맞춘다. 초기값과 증감수를 확인한다
# 등호에 위치한 값은 제출 전에 미리, 검증
import sys

input = sys.stdin.readline

N = int(input())
answer=1
cnt=2

while N>=cnt:
    cnt+=6*answer
    answer+=1
    
print(answer)


