def solve():
    r,c = map(int, input().split())
    hoji = [list(map(int, input().split())) for _ in range(r)]

    List = []
    for i in range(c):
        Sum = 0
        for j in range(r):
            Sum += hoji[j][i]
        List.append(Sum)
    hoji.append(List)

    for i in range(r+1):
        hoji[i].append(sum(hoji[i]))
    [print(*x) for x in hoji]

if __name__ == '__main__':
    solve()