# def printlist(li): #[1, 2, 3]を1 2 3の様に出力
#     for i in li:
#         if i != li[-1]:
#             print(i,end=" ")
#         else:
#             print(i)
#
#pythonにはアンパックと呼ばれる配列の先頭にアスタリスクをつけて綺麗に表示できる．

def insertionSort(A, N):
    for i in range(1,N):
        print(*A)
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = v
    print(*A)

N = int(input())
A = list(map(int, input().split()))

if __name__ == "__main__":
    insertionSort(A, N)