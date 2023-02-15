# 아이디어 : 예외) 입력의 마지막값은 처리 안하게끔, for문 마지막은 입력받은 개수 -1
# 시간복잡도 : O(n^1/2)

# 자료구조 : 베르트랑 공준, 에라토스테네스의 체 = 2부터 시작해서 배수를 구하고, 그 배수에 해당하는 수를 소수에서 제외

# 2를 제외한 2의 배수를 구해서 전부 지운다.

# 3을 제외한 3의 배수를 구해서 전부 지운다.

# 4는 체크할 필요 없다. 2의 배수를 구할때 이미 체크했다.

# 5를 제외한 5의 배수를 구해서 전부 지운다.

# …

# n의 제곱근보다 큰 정수중 가장 작은 정수까지 이것을 반복하면 된다.

# 예를들어 120이하의 소수를 구할 경우, 120이 아닌 11까지만 반복해주면 된다.

# 120의 제곱근보다 큰 정수중 가장 작은 정수가 11이기 때문이다.

# https://itholic.github.io/kata-bertrands-postulate/
import sys

input = sys.stdin.readline

def prime(k):
    if k ==1:
        return 0
    for i in range(2,int(k**0.5)+1):
        print(i)
        if k%i==0:
            return 0
    else:
        return 1
    
prime_list=[]

for i in range(2,2*123456+1):
    if prime(i):
        prime_list.append(i) # 값의 범위만큼, 소수 리스트 생성

        
while True:
    n = int(input())
    
    if n==0: # while 종료 조건
        break
    cnt=0
    
    for i in prime_list:
        if i > 2*n: 
            break
        elif n< i <=2*n: 
            cnt += 1
            
    print(cnt)