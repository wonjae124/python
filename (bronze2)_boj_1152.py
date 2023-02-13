# 아이디어 : 문자열 입력받은걸 단어로 쪼갠다. 그리고 그 단어의 개수를 센다.
# 복잡도 : ?
# 자료구조 split(sep='구분자',maxsplit=분할횟수)으로 쪼갠다

import sys

input = sys.stdin.readline
# split()함수는 리스트로 만드는 함수이다. 따라서, 감싸줄 필요 없다. 한 번 더 리스트를 감싸면 이중리스트가 된다.

N = input().split()
print(len(N))