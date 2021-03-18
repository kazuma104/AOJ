def solve():
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    p1,p2,p3 = 0,0,0
    dis = [0]*n
    for i in range(n):
        dis[i] = abs(x[i]-y[i])
        p1 += dis[i]
        p2 += dis[i]**2
        p3 += dis[i]**3
    p2 = p2**(1/2)
    p3 = p3**(1/3)

    print(p1,p2,p3,max(dis),sep="\n")

if __name__ == '__main__':
    solve()