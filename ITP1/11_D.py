def solve():
    class Dice:
        def __init__(self, surface):
            self.Roll = surface

        def S(self):
            self.Roll[0], self.Roll[1], self.Roll[5], self.Roll[4] = self.Roll[4], self.Roll[0], self.Roll[1], self.Roll[5]

        def E(self):
            self.Roll[0], self.Roll[2], self.Roll[5], self.Roll[3] = self.Roll[3], self.Roll[0], self.Roll[2], self.Roll[5]

        def N(self):
            self.Roll[0], self.Roll[4], self.Roll[5], self.Roll[1] = self.Roll[1], self.Roll[0], self.Roll[4], self.Roll[5]

        def W(self):
            self.Roll[0], self.Roll[3], self.Roll[5], self.Roll[2] = self.Roll[2], self.Roll[0], self.Roll[3], self.Roll[5]

        def shift(self):
            self.Roll[1], self.Roll[2], self.Roll[3], self.Roll[4], self.Roll[5], self.Roll[0] = self.Roll[0], self.Roll[1], self.Roll[2], self.Roll[3], self.Roll[4], self.Roll[5]

    n = int(input())
    dice = [0]*n
    for i in range(n):
        surface = list(map(int, input().split()))
        dice[i] = Dice(surface)
    flag = True
    for i in range(n-1):
        for j in range(i+1,n):
            if set(dice[i].Roll) == set(dice[j].Roll):
                top = dice[j].Roll.index(dice[i].Roll[0])
                if top == 1:
                    dice[j].N()
                elif top == 2:
                    dice[j].W()
                elif top == 3:
                    dice[j].E()
                elif top == 4:
                    dice[j].S()
                elif top == 5:
                    dice[j].N()
                    dice[j].N()
                
                front = dice[j].Roll.index(dice[i].Roll[1])
                if front == 2:
                    dice[j].W()
                    dice[j].S()
                    dice[j].E()
                elif front == 3:
                    dice[j].E()
                    dice[j].S()
                    dice[j].W()
                elif front == 4:
                    dice[j].E()
                    dice[j].N()
                    dice[j].N()
                    dice[j].W()
                for _ in range(6):
                    if dice[i].Roll == dice[j].Roll:
                        flag = False
                    dice[j].shift()
                else:
                    pass
            else:
                pass
    print("Yes" if flag else "No")

if __name__ == '__main__':
    solve()