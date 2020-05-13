def partition(A, p, r):
    x = A[r-1]
    i = p
    for j in range(r-1):
        if A[j] <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r-1] = A[r-1], A[i]
    return i

if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    q = partition(A, 0, n)
    print(*A[:q],"["+str(A[q])+"]",*A[q+1:])