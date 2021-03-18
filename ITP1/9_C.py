def solve():
    n = int(input())
    p1,p2 = 0,0
    for _ in range(n):
        S,T = input().split()
        if S == T:
            p1 += 1
            p2 += 1
        elif S > T:
            p1 += 3
        else:
            p2 += 3
    print(p1,p2)

if __name__ == '__main__':
    solve()