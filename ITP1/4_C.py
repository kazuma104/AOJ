for _ in range(10**9):
    a,op,b = input().split()
    a = int(a)
    b = int(b)
    if op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/":
        print(a//b)
    elif op == "?":
        break