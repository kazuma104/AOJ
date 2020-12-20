def solve():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(n)]
    b = [int(input()) for i in range(m)]
    ans = [0 for i in range(n)]
    
    for i in range(n):
        for j in range(m):
            ans[i] += a[i][j] * b[j]
        print(ans[i])    

if __name__ == '__main__':
    solve()