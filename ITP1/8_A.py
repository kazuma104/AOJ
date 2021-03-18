def solve():
    S = input()
    T = ""
    for i in range(len(S)):
        if S[i] >= 'a':
            T += S[i].upper()
        else:
            T += S[i].lower()
    
    print(T)

if __name__ == '__main__':
    solve()