def solve():
    while True:
        n = int(input())
        if n == 0: break
        sd = 0
        s = list(map(int, input().split()))
        ave = sum(s)/n
        for d in s:
            sd += (d-ave)**2/n
        print(sd**0.5)

if __name__ == '__main__':
    solve()