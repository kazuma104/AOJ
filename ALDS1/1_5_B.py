from collections import deque
count = 0

def marge2(A, left, mid, right):
    global count
    L = A[left:mid] + [float("inf")]
    R = A[mid:right] + [float("inf")]
    
    i, j = 0, 0
    for k in range(left, right):
        count += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def marge(A, left, mid, right):#runtime error
    global count
    n1 = mid-left
    n2 = right-mid
    Lque = deque()
    Rque = deque()
    for i in range(n1):
        Lque.append(A[left+i])
    for i in range(n2):
        Rque.append(A[mid+i])
    Lque.append(float("inf"))
    Rque.append(float("inf"))
    print(Lque,Rque)
    L = Lque.popleft()
    R = Rque.popleft()
    for k in range(left,right):
        count += 1
        if L <= R:
            A[k] = L
            L = Lque.popleft()        
        else:
            A[k] = R
            R = Rque.popleft()

def margeSort(A, left, right):
    if left+1 < right:
        mid = (left+right)//2
        margeSort(A, left, mid)
        margeSort(A, mid, right)
        marge(A, left, mid, right)

if __name__ == "__main__":
    n = int(input())
    S = list(map(int, input().split()))
    margeSort(S, 0, n)
    print(*S)
    print(count)