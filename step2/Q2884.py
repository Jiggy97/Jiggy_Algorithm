H, M = map(int, input().split())
if M >= 45:
    print(H, M - 45)
else:
    M = 45 - M
    if H == 0:
        H = 24
        print(H - 1, 60 - M)
    else:
        print(H - 1, 60 - M)
