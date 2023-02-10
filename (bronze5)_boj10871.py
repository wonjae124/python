import sys

input = sys.stdin.readline

N, X = map(int,input().split())
A = [i for i in map(int,input().split())]
# 1.
# for i in range(0,N):
#     if X>A[i]:
#         print(A[i],end=' ')

# 2.
result = [str(i) for i in A if i<X]
print(' '.join(result))