import sys

input = sys.stdin.readline

# 그냥 입력 받으면, 자료형은 문자열로 인식함. 따라서, 정수로 감싸야 함
array = [int(input().rstrip()) for i in  range(9)]  
max_idx, max_val = array.index(max(array))+1,max(array)


print(type(max_val))
print(max_idx)