def solve1():
    cards = [[False for i in range(13)] for j in range(4)]
    pattern = ["S", "H", "C", "D"]

    N = int(input())
    for _ in range(N):
        ch, rank = input().split()
        rank = int(rank)
        cards[pattern.index(ch)][rank-1] = True

    for i in range(4):
        for j in range(13):
            if cards[i][j] == False:
                print(pattern[i], j+1)

def solve2():
    cards = [False for i in range(52)]
    pattern = ["S", "H", "C", "D"]
    
    N = int(input())
    for _ in range(N):
        ch, rank = input().split()
        rank = int(rank)
        cards[pattern.index(ch)*13+(rank-1)] = True

    for i in range(52):
        if cards[i] == False:
            print(pattern[i//13],(i%13)+1)
            
if __name__ == "__main__":
    solve2()