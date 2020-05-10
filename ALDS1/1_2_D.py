cnt = 0

def insertionSort(A, N, g):
    global cnt
    for i in range(g,N):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j -= g
            cnt += 1
        A[j+g] = v

def shellSort(A, N):
    g = 1
    G = [1]
    m = 1
    while (3*g+1) < N:
        g = 3*g+1
        G.append(g)
        m += 1
    G = list(reversed(G))

    for i in G:
        insertionSort(A, N, i)

    print(m)
    print(*G)
    print(cnt,*A,sep="\n")
    

if __name__ == "__main__":
    n = int(input())
    #一行ずづの入力として，https://note.com/azura35/n/ndf3194de0a74を参考．
    A = [int(input()) for x in range(n)]

    shellSort(A, n)