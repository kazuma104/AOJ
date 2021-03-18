def solve():
    while True:
        m,f,r = map(int, input().split())
        if m == -1 and f == -1 and r == -1:
            break
        else:
            res = m+f
            if m == -1 or f == -1:
                print("F")
            elif res >= 80:
                print("A")
            elif res >= 65:
                print("B")
            elif res >= 50:
                print("C")
            elif res >= 30:
                if r >= 50:
                    print("C")
                else:
                    print("D")
            else:
                print("F")
                


if __name__ == '__main__':
    solve()