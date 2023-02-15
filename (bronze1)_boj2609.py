
# 자료구조 : 최대공약수, 유클리드 호제법, a와 b를 나눈 나머지 r이면(a>b), a와 b의 최대 공약수는 b와 r의 최대공약수와 같다
# 최소공배수, a와 b의 곱으로 나온 값에 a와 b의 최대공약수 나누기

import sys

input = sys.stdin.readline

def gcd(a,b):
    while(b>0): # 나머지가 0이 될 때까지 실행한다.
        a,b=b,a%b
    return a

def lcm(a,b):
    return (a*b) //gcd(a,b)

a,b = map(int,input().split())

print(gcd(a,b),lcm(a,b),sep='\n')