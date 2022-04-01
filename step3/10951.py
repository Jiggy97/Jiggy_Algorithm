while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break

# while문을 사용할 때는 항상 반복이 끝이 있도록 설계 한다.