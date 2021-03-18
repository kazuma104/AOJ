def solve():
    while True:
        n,x = map(int, input().split())
        if n == 0 and x == 0:
            break
        else:
            count = 0
            for i in range(1,n+1):
                for j in range(i+1,n+1):
                    for k in range(j+1,n+1):
                        if x == i+j+k:
                            count += 1
            print(count)

if __name__ == '__main__':
    solve()