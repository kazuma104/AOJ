from collections import deque

if __name__ == "__main__":
    n, q = map(int, input().split())
    process = deque()
    for _ in range(n):
        name, time = input().split()
        time = int(time)
        process.append([name,time])
    t = 0
    ans = []
    while len(process):
        p = process.popleft()
        if p[1]-q > 0:
            p[1] -= q
            t += q
            process.append(p)
        else:
            t += p[1]
            ans.append([p[0],t])
    for a in ans:
        print(*a)