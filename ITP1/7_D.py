def solve():
    n,m,l = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(m)]
    res = [[0]*l for _ in range(n)]

    for i in range(n):
        for j in range(l):
            for k in range(m):
                res[i][j] += a[i][k] * b[k][j] 
    [print(*res[i]) for i in range(n)]

if __name__ == '__main__':
    solve()