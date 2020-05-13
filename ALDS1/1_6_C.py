def partition(A, p, r):
    x = A[r-1][2]
    print(x)
    i = p
    for j in range(r-1):
        if A[j][2] <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r-1] = A[r-1], A[i]
    return i

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        print(q)
        quickSort(A, p, q-1)
        quickSort(A, p+1, r)

if __name__ == "__main__":
    n = int(input())
    A = [input() for x in range(n)]
    print(A)
    quickSort(A, 0, n)
    print(*A)