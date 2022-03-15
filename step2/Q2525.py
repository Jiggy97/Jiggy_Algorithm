H, M = map(int, input().split())
O = int(input())

if H == 23:
    H = -1
    if M + O >= 60 and M + O < 120:
        newM = M + O - 60
        print(H + 1, newM)

    elif M + O >= 120:
        newM = M + O - 120
        print(H + 2, newM)

    else:
        print(H, M + O)

else:
    if M + O >= 60 and M + O < 120:
        newM = M + O - 60
        print(H + 1, newM)

    elif M + O >= 120:
        newM = M + O - 120
        print(H + 2, newM)

    else:
        print(H, M + O)
