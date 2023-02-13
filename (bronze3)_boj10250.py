# 아이디어 : 입장하는 순서에 따라서, 세로로 먼저 할당한다
# 처음 N번째 왔다치면, 층 수(H)로 나눈다. 그리고, 나머지는 층(YY)에 배분하고
# 몫은1을 더한 방 번호로 XX를 부여한다.   
# H=6, W=12, N=10
# ex) XX=10//6+1=2, YY=10%6=4이므로 str(YY)+str(XX)번호를 출력한다.
# 4층, 02호실
# 수학문제는 약간 나누어 떨어지는 경우의 예외처리를 잘해야한다. 
import sys


T = int(sys.stdin.readline())

for i in range(T):
    H, W, N = map(int,sys.stdin.readline().split())
    if N%H != 0:
        XX = int(N//H)+1
        YY = int(N%H)
    else:
        XX = int(N//H)
        YY = H
    # 중간에 0을 붙이면 문제 틀린다. N가 1499일 때, 에러로 29050이 나옴. 원래 2950이 맞다
    print(str(YY)+'0'+str(XX))