# 아이디어,  소수 구하는 아스~체, 그리고 입력값을 반으로 쪼갠 a,b를 구해서, a는 +1, b는 -1해서 소수가 맞으면 출력하게 만든다
# 자료구조 : 골드바흐 파티션(2보다 큰 모든 짝수는 두 소수의 합)
import sys

input = sys.stdin.readline

def prime(a):
    if a == 1:
        return 0
    for i in range(2,int(a**0.5)+1):
        if a%i == 0:
            return 0  
    else:
        return 1
    

n = int(input())

for _ in range(n):
    m = int(input())
    a,b=m//2,m//2 # 파티션 구하기
    while(1):
        if prime(a) and prime(b):
            print(a,b)
            break
        else:
            a-=1 
            b+=1