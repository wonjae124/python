import sys
import math 
input = sys.stdin.readline


A,B,V = map(int,input().split())

V=V-A # 마지막 날에, 낮시간에 일을 끝마칠 것이므로 먼저, A만큼 줄여주고 출력할 때, 1을 더해준다.
print(math.ceil(V/(A-B))+1) # 낮시간+밤시간을 포함한 일을 하는지 확인, math 패키지로, ceil 이용해 올림