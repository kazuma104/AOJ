def solve():
    s = input()
    p = input()
    s += s
    print("Yes" if p in s else "No")

if __name__ == '__main__':
    solve()