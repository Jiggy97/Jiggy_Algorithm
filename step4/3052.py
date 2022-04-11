num = []

for i in range(10):
    n = int(input())
    num.append(n % 42)

num = set(num)
# 중복을 제거 해주는 필터 역할
print(len(num))
# len 은 길이를 출력

