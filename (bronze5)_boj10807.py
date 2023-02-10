import sys

input = sys.stdin.readline

N = int(input())
list = [i for i in map(int,input().split())]
V = int(input())
cnt=0
#1
# for i in range(0, N):
#     if V == list[i]:
#         cnt+=1

#2
cnt = list.count(V)
        
print(cnt)   