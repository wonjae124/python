import sys

input = sys.stdin.readline

chk = [int(i) for i in range(1,31)]
arr = [int(input().rstrip()) for _ in range(28)]
rst = [str(x) for x in chk if x not in arr ]
print('\n'.join(rst))
