def solve():
    res = [0]*26
    while True:
        # if S == "": break|||vscodeでする場合はtry,exceptがうまく働かない．
        try:
            S = input()
        except EOFError:
            break
        S = S.lower()

        for d in S:
            diff = ord(d)-ord("a")
            if 0 <= diff and diff <=26:
                res[diff] += 1
        
    for i in range(26):
        print(chr((i+ord("a"))), ":", res[i])

if __name__ == '__main__':
    solve()