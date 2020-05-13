def exhaustitveSearch2(n, q, A, m): #Accepted(A使ってない)
    ans = [False]*2000
    for i in range(2**n):
        qsum = 0
        for j in range(n):
            if((i>>j)&1):
                qsum += q[j]
        ans[qsum] = True

    for mi in m:
        print("yes") if ans[mi] else print("no")


def exhaustitveSearch(n, q, A, m): #runtime Error
    ans = []
    for mi in m:
        flag = False
        for i in range(2**n):
            qsum = 0
            for j in range(n):
                if((i>>j)&1):
                    qsum += q[j]
            if mi == qsum:
                flag = True
                break
        if flag:
            ans.append("yes")
        else:
            ans.append("no")
    [print(x) for x in ans]

if __name__ == "__main__":
    n = int(input())
    q = list(map(int, input().split()))
    A = int(input())
    m = map(int, input().split())
    exhaustitveSearch2(n, q, A, m)