def solve():
    x1,y1,x2,y2 = map(float, input().split())
    print(((x2-x1)**2+(y2-y1)**2)**0.5)

if __name__ == '__main__':
    solve()