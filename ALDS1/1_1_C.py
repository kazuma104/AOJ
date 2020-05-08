from math import sqrt

def isprime(x):
    if x == 2:
        return True
    if x<2 or x%2==0:
        return False
    
    i = 3
    while i <= sqrt(x):
        if x % i == 0:
            return False
        i = i + 2

    return True

if __name__ == "__main__":
    n = int(input())
    Sum = 0
    for i in range(n):
        Sum += isprime(int(input()))
    print(Sum)