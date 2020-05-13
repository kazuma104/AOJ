if __name__ == "__main__":
    S = {} #特定の値があるか見るときにはlistより，dictが速い（ハッシュテーブル）
    ans = []
    for i in range(int(input())):
        order = input().split()
        if order[0] == "find":
            if order[1] in S:
                ans.append("yes")
            else:
                ans.append("no")
        else:
            S[order[1]]=i

    for j in ans:
        print(j)