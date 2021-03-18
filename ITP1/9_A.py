def solve():
    cnt = 0
    W = input()
    while True:
        T = input()
        if T == "END_OF_TEXT": break
        T = T.lower()
        L = T.split()
        cnt += L.count(W)
    print(cnt)

if __name__ == '__main__':
    solve()
    #https://note.nkmk.me/python-str-search/
    #単語を検索、個数をカウント