def solve():
    while True:
        x = input()
        if x == "0":
            break
        else:
            Sum = 0
            for i in range(len(x)):
                Sum += int(x[i])
            print(Sum)

# for d in x:
#     Sum += int(d) こちらのほうが賢いか．

if __name__ == '__main__':
    solve()