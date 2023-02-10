# 아이디어, 나누는건데 중첩이 안되야함. 일단 리스트를 저장한 후에, 중첩된 값을 없애버리게끔 set형태로 바꾸자.
# 복잡도, N^2
# 자료구조, set함수는 중첩 삭제

arr = [int(input().rstrip()) for _ in range(10)]
rst = []
set_rst = []
for i in range(10):
    rst.append(arr[i]%42)
set_rst = set(rst)
print(len(set_rst))
