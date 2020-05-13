def countingSort(A, B, k):
    C = [0]*(k+1)
    for j in range(len(A)):
        C[A[j]] += 1
    for i in range(1,k+1):
        C[i] += C[i-1]
    for j in reversed(range(0,len(A))): #jは7~0にかわる
        B[C[A[j]]-1] = A[j]
        C[A[j]] -= 1

if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    B = [0]*n
    k = max(A)
    countingSort(A, B, k)
    print(*B)