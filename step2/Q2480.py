a, b, c = map(int, input().split())

def treebingo(x):
    price = 10000 + x*1000
    return price
def twobingo(x):
    price = 1000 + x*100
    return price
def nobingo(x):
    price = x*100
    return price

if a == b:
    if a == c:
        print(treebingo(a))
    else:
        print(twobingo(a))
elif a == c:
    print(twobingo(a))
elif b == c:
    print(twobingo(b))
else:
    biggest = max(a, b, c)
    print(nobingo(biggest))
