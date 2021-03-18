def solve():
    List = []
    while True:
        S = input()
        if S == "-": break
        m = int(input())
        for _ in range(m):
            h = int(input())
            S = S[h:len(S)] + S[0:h]
        List.append(S)
        
    [print(List[i]) for i in range(len(List))]

if __name__ == '__main__':
    solve()