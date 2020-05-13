def binarySearch(n, S, t):
    left = 0
    right = n
    while left < right:
        mid = (left+right)//2
        if t == S[mid]:
            return 1
        elif t < S[mid]:
            right = mid
        else:
            left = mid+1
    return 0

if __name__ == "__main__":
    n = int(input())
    S = list(map(int, input().split()))
    q = int(input())
    T = list(map(int, input().split()))
    count = 0
    for t in T:
        count += binarySearch(n, S, t)
    print(count)