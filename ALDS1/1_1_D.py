if __name__ == "__main__":
    n = int(input())

    maxv = -float("inf") #maxvは，Ri-minvが最大の時
    minv = int(input()) #minvは，Riが最小値
    for i in range(n-1):
        R = int(input())
        maxv = max(maxv, R-minv)
        minv = min(minv, R)
    
    print(maxv)
