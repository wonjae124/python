## 1번
# N = list(input())
# alp = 'abcdefghijklmnopqrstuvwxyz'
# dic = {}
# print(N)

# # str.index(찾을 문자 or 문자열, 시작위치, 끝위치)
# for i in alp:
#     if i in N:
#         print(N.index(i),end=' ')
    
#     else:
#         print("-1",end=' ')
        
## 2번        
# N = input()
# alp = 'abcdefghijklmnopqrstuvwxyz'
# # string.find(찾을 문자열 or 문자), 첫 번째에 위치한 순서를 출력, 만약 찾는 문자가 없으면 -1 출력
# for x in alp:
#     print(N.find(x), end= ' ')

## 3번, 딕셔너리 사용법

N = input()
alp = 'abcdefghijklmnopqrstuvwxyz'
dic = {}
for i in range(len(N)):
    if N[i] not in dic.keys():
        dic[N[i]]=i

for i in alp:
    if i in N:
        print(str(dic[i]), end= ' ')
    else:
        print("-1",end=" ")