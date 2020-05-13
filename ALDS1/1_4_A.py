from collections import deque

def linearSearch3(n, S, q, T): #重複を消しているのでとても速いはず．
    count = 0
    S = list(set(S))
    n = len(S)
    d = deque(T)
    #print(S)
    for _ in range(q):
        t = d.pop()
        for s in range(n):
            if t==S[s]:
                count += 1
                break
    return count


def linearSearch2(n, S, q, T): #dequeを使用して，若干早いはず
    count = 0
    d = deque(T)
    for _ in range(q):
        t = d.pop()
        for s in range(n):
            if t==S[s]:
                count += 1
                break
    return count

def linearSearch(n, S, q, T): #ふつう
    count = 0
    for t in range(q):
        for s in range(n):
            if T[t]==S[s]:
                count += 1
                break
    return count

if __name__ == "__main__":
    n = int(input())
    S = list(map(int, input().split()))
    q = int(input())
    T = list(map(int, input().split()))
    print(linearSearch(n, S, q, T))