import copy

def bubbleSort(C, N):
    for i in range(N):
        for j in reversed(range(i+1,N)):
            if C[j][1] < C[j-1][1]:
                C[j],C[j-1] = C[j-1],C[j]
    return C

def selectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i,N):
            if C[j][1] < C[minj][1]:
                minj = j
        if C[i] != C[minj]:
            C[i], C[minj] = C[minj], C[i]
    return C

if __name__ == "__main__":
    N = int(input())
    A = input().split()
    B = copy.copy(A)
    bubble = bubbleSort(A, N)
    selection = selectionSort(B, N)
    print(*bubble)
    print("Stable")
    print(*selection)
    if bubble == selection:
        print("Stable")
    else:
        print("Not stable")