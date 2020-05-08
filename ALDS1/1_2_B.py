def selectionSort(A, N):
    count = 0
    for i in range(N):
        minj = i
        for j in range(i,N):
            if A[j] < A[minj]:
                minj = j
        if A[i] != A[minj]:
            A[i], A[minj] = A[minj], A[i]
            count += 1
    return [A, count]

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    Sort = selectionSort(A, N)
    print(*Sort[0])
    print(Sort[1])