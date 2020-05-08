def bubbleSort(A, N):
    count = 0
    for i in range(N):
        for j in reversed(range(i+1,N)):
            if A[j] < A[j-1]:
                A[j],A[j-1] = A[j-1],A[j]
                count += 1
    return A, count

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    Sort = bubbleSort(A, N)
    print(*Sort[0])
    print(Sort[1])