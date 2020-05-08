def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)

if __name__ == "__main__":
    x, y = map(int, input().split())
    print(gcd(x, y))