import sys

input = sys.stdin.readline
N = input()

lst = list(N)
sum=0
dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
for i in range(len(lst)):
    for j in dial: #j는 쪼갠 dial의 문자열 'WXYZ'
        if lst[i] in j: # lst[i]는 'WA'중, 'W'이다. 
            sum+=dial.index(j)+3 #문자열의 인덱스를 반환한다. 'WXYZ'가 있는 문자열, str.index(str중에 찾고 있는 문자열 or 문자)
print(sum)