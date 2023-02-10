import sys

input = sys.stdin.readline

N = int(input())
array = [i for i in map(int,input().split())]

maximum = max(array)
minumum = min(array)

print(minumum,maximum)