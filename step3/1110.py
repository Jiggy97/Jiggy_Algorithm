N = int(input())
num = N
cnt = 0

while True:
    a = num // 10
    b = num % 10
    num = (10*b) + ((a+b) % 10)
    cnt += 1

    if num == N:
        break
print(cnt)
