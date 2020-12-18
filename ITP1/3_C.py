for _ in range(10000):
    a,b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a,b) if a<b else print(b,a)