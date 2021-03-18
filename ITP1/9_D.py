def solve():
    S = input()
    q = int(input())
    for _ in range(q):
        Input = input().split()
        a,b = int(Input[1]),int(Input[2]) 
        if Input[0] == "print":
            print(S[a:(b+1)])
        elif Input[0] == "reverse":
            S = S[:a] + (S[a:b+1])[::-1] + S[b+1:]
        elif Input[0] == "replace":
            S = S[:a] + Input[3] + S[b+1:]

if __name__ == '__main__':
    solve()
    #reverseが難しかった．