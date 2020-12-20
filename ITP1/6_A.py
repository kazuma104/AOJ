n = int(input())
a = list(map(int, input().split()))

for i, elem in enumerate(a[::-1]):
    if i>0:
        print(" ", end = "")
    print(elem, end = "")
print()